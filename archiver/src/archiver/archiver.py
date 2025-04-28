"""Core module for archiving URLs with multiple services."""

import asyncio
import logging
import re
from typing import Dict, List, Any, Optional
from urllib.parse import urlparse

import aiohttp

from archiver.services import ArchiveServiceBase, InternetArchive, ArchivePh, MementoWeb

logger = logging.getLogger(__name__)


class URLArchiver:
    """Main class for archiving URLs with multiple services."""

    def __init__(
        self,
        services: Optional[List[ArchiveServiceBase]] = None,
        user_agent: str = "Archive Links Client/0.1.0",
        max_concurrency: int = 5
    ):
        """Initialize the URL archiver.

        Args:
            services: List of archiving services to use. If None, all available services will be used.
            user_agent: User agent string to use for requests
            max_concurrency: Maximum number of URLs to process concurrently
        """
        self.services = services or [
            InternetArchive(user_agent=user_agent),
            ArchivePh(user_agent=user_agent),
            MementoWeb(user_agent=user_agent)
        ]
        self.user_agent = user_agent
        self.max_concurrency = max_concurrency

    @staticmethod
    def is_valid_url(url: str) -> bool:
        """Check if a URL is valid.

        Args:
            url: The URL to check

        Returns:
            True if the URL is valid, False otherwise
        """
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except Exception:
            return False

    async def archive_single_url(self, url: str) -> List[Dict[str, Any]]:
        """Archive a single URL with all services.

        Args:
            url: The URL to archive

        Returns:
            List of results, one for each service
        """
        if not self.is_valid_url(url):
            logger.warning(f"Invalid URL: {url}")
            return [{
                "success": False,
                "service": service.name,
                "original_url": url,
                "error": "Invalid URL"
            } for service in self.services]

        url = url.strip()
        results = []

        # Create a single session for all requests
        async with aiohttp.ClientSession() as session:
            tasks = []
            for service in self.services:
                logger.info(f"Archiving {url} with {service.name}")
                tasks.append(service.archive_url(url, session))

            # Wait for all archiving tasks to complete
            results = await asyncio.gather(*tasks, return_exceptions=True)

            # Handle any exceptions that were returned
            for i, result in enumerate(results):
                if isinstance(result, Exception):
                    service_name = self.services[i].name
                    logger.error(f"Error archiving {url} with {service_name}: {result}")
                    results[i] = {
                        "success": False,
                        "service": service_name,
                        "original_url": url,
                        "error": str(result)
                    }

        return results

    async def archive_urls(self, urls: List[str]) -> Dict[str, List[Dict[str, Any]]]:
        """Archive multiple URLs with all services.

        Args:
            urls: List of URLs to archive

        Returns:
            Dictionary mapping URLs to their archival results
        """
        results = {}

        # Process URLs in chunks to avoid overwhelming the services
        sem = asyncio.Semaphore(self.max_concurrency)

        async def archive_with_semaphore(url: str):
            async with sem:
                return url, await self.archive_single_url(url)

        # Create tasks for each URL
        tasks = [archive_with_semaphore(url) for url in urls]

        # Process URLs concurrently with the semaphore limiting concurrency
        for future in asyncio.as_completed(tasks):
            url, url_results = await future
            results[url] = url_results

            # Log the results
            for result in url_results:
                if result.get("success"):
                    logger.info(f"Successfully archived {url} with {result['service']}: {result['archived_url']}")
                else:
                    logger.warning(f"Failed to archive {url} with {result['service']}: {result.get('error')}")

        return results

    async def archive_urls_from_file(self, file_path: str) -> Dict[str, List[Dict[str, Any]]]:
        """Archive URLs from a file.

        Args:
            file_path: Path to a file containing one URL per line

        Returns:
            Dictionary mapping URLs to their archival results
        """
        try:
            with open(file_path, 'r') as f:
                urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]

            if not urls:
                logger.warning(f"No URLs found in {file_path}")
                return {}

            logger.info(f"Archiving {len(urls)} URLs from {file_path}")
            return await self.archive_urls(urls)

        except Exception as e:
            logger.error(f"Error reading URLs from {file_path}: {e}")
            raise