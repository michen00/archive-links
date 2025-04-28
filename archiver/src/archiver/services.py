"""Services module for handling URL archiving with different services."""

import abc
import asyncio
import logging
import random
import time
from typing import Dict, Optional, Any

import aiohttp

logger = logging.getLogger(__name__)


class ArchiveServiceBase(abc.ABC):
    """Base class for archive services."""

    def __init__(self, user_agent: str = "Archive Links Client/0.1.0"):
        """Initialize the archiver service.

        Args:
            user_agent: The user agent to use for requests
        """
        self.user_agent = user_agent
        self.base_delay = 1  # Initial delay in seconds
        self.max_retries = 5

    @property
    @abc.abstractmethod
    def name(self) -> str:
        """Return the name of the service."""
        pass

    @abc.abstractmethod
    async def archive_url(self, url: str, session: aiohttp.ClientSession) -> Dict[str, Any]:
        """Archive a URL using the service.

        Args:
            url: The URL to archive
            session: The aiohttp client session to use

        Returns:
            Dict containing:
                success: Boolean indicating success
                archived_url: URL of the archived page (if success)
                error: Error message (if not success)
        """
        pass

    async def _make_request(
        self,
        session: aiohttp.ClientSession,
        method: str,
        url: str,
        **kwargs
    ) -> aiohttp.ClientResponse:
        """Make a request with retry logic and exponential backoff.

        Args:
            session: The aiohttp client session
            method: HTTP method (GET, POST, etc.)
            url: URL to request
            **kwargs: Additional arguments to pass to session.request

        Returns:
            The response from the server
        """
        headers = kwargs.get("headers", {})
        if "User-Agent" not in headers:
            headers["User-Agent"] = self.user_agent
        kwargs["headers"] = headers

        retries = 0
        while retries < self.max_retries:
            try:
                return await session.request(method, url, **kwargs)
            except (aiohttp.ClientError, asyncio.TimeoutError) as e:
                retries += 1
                if retries >= self.max_retries:
                    logger.error(f"Failed to request {url} after {self.max_retries} attempts: {e}")
                    raise

                # Exponential backoff with jitter
                delay = self.base_delay * (2 ** retries) + random.uniform(0, 0.5)
                logger.warning(f"Request to {url} failed. Retrying in {delay:.2f}s... ({retries}/{self.max_retries})")
                await asyncio.sleep(delay)


class InternetArchive(ArchiveServiceBase):
    """Internet Archive (Wayback Machine) service."""

    @property
    def name(self) -> str:
        return "Internet Archive"

    async def archive_url(self, url: str, session: aiohttp.ClientSession) -> Dict[str, Any]:
        """Archive a URL using the Wayback Machine.

        Args:
            url: The URL to archive
            session: The aiohttp client session to use

        Returns:
            Dict containing:
                success: Boolean indicating success
                archived_url: URL of the archived page (if success)
                error: Error message (if not success)
        """
        save_url = f"https://web.archive.org/save/{url}"

        try:
            response = await self._make_request(session, "GET", save_url)

            if response.status in (200, 201):
                # Extract the archived URL from the response
                archived_url = str(response.url)
                return {
                    "success": True,
                    "service": self.name,
                    "original_url": url,
                    "archived_url": archived_url
                }
            else:
                return {
                    "success": False,
                    "service": self.name,
                    "original_url": url,
                    "error": f"Failed with status {response.status}"
                }

        except Exception as e:
            return {
                "success": False,
                "service": self.name,
                "original_url": url,
                "error": str(e)
            }


class ArchivePh(ArchiveServiceBase):
    """Archive.ph service."""

    @property
    def name(self) -> str:
        return "Archive.ph"

    async def archive_url(self, url: str, session: aiohttp.ClientSession) -> Dict[str, Any]:
        """Archive a URL using Archive.ph.

        Args:
            url: The URL to archive
            session: The aiohttp client session to use

        Returns:
            Dict containing:
                success: Boolean indicating success
                archived_url: URL of the archived page (if success)
                error: Error message (if not success)
        """
        save_url = "https://archive.ph/submit/"

        try:
            data = {"url": url}
            response = await self._make_request(
                session,
                "POST",
                save_url,
                data=data,
                allow_redirects=True
            )

            if response.status in (200, 201, 302):
                # The archived URL is either in the Location header or in the final URL
                archived_url = str(response.url)

                # If we got redirected to the archived page
                if "archive.ph" in archived_url and url not in archived_url:
                    return {
                        "success": True,
                        "service": self.name,
                        "original_url": url,
                        "archived_url": archived_url
                    }
                else:
                    return {
                        "success": False,
                        "service": self.name,
                        "original_url": url,
                        "error": "Failed to archive URL"
                    }
            else:
                return {
                    "success": False,
                    "service": self.name,
                    "original_url": url,
                    "error": f"Failed with status {response.status}"
                }

        except Exception as e:
            return {
                "success": False,
                "service": self.name,
                "original_url": url,
                "error": str(e)
            }


class MementoWeb(ArchiveServiceBase):
    """Memento Web service as the third archive service."""

    @property
    def name(self) -> str:
        return "Memento Web"

    async def archive_url(self, url: str, session: aiohttp.ClientSession) -> Dict[str, Any]:
        """Archive a URL using Memento Web service.

        Args:
            url: The URL to archive
            session: The aiohttp client session to use

        Returns:
            Dict containing:
                success: Boolean indicating success
                archived_url: URL of the archived page (if success)
                error: Error message (if not success)
        """
        # Using TimeGate protocol to create a memento
        save_url = f"https://timetravel.mementoweb.org/timegate/{url}"

        try:
            response = await self._make_request(
                session,
                "GET",
                save_url,
                allow_redirects=True
            )

            if response.status in (200, 201, 302):
                archived_url = str(response.url)

                return {
                    "success": True,
                    "service": self.name,
                    "original_url": url,
                    "archived_url": archived_url
                }
            else:
                return {
                    "success": False,
                    "service": self.name,
                    "original_url": url,
                    "error": f"Failed with status {response.status}"
                }

        except Exception as e:
            return {
                "success": False,
                "service": self.name,
                "original_url": url,
                "error": str(e)
            }