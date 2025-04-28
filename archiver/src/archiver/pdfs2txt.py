"""Extract URLs from PDF files in a directory."""

import asyncio
import concurrent.futures
import logging
import re
import sys
from pathlib import Path
from typing import List, Set, Dict, Any, Optional

import typer
from PyPDF2 import PdfReader
from rich.console import Console
from rich.progress import Progress, TaskID

# Improved URL regex pattern with better handling of special characters including dashes
URL_PATTERN = re.compile(
    r'https?://[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&//=]*)'
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)
console = Console()

app = typer.Typer(help="Extract URLs from PDF files")


def extract_urls_from_pdf(pdf_path: Path) -> Set[str]:
    """Extract URLs from a PDF file.

    Args:
        pdf_path: Path to the PDF file

    Returns:
        Set of URLs found in the PDF
    """
    urls = set()

    try:
        with open(pdf_path, "rb") as f:
            pdf = PdfReader(f)

            # Process each page
            for page_num, page in enumerate(pdf.pages):
                text = page.extract_text()
                if not text:
                    continue

                # Pre-process text to handle cases where URLs might be broken across lines or contain spaces
                # Replace common PDF artifacts that might break URL detection
                text = re.sub(r'http://\s+', 'http://', text)  # Remove spaces after http://
                text = re.sub(r'https://\s+', 'https://', text)  # Remove spaces after https://
                text = re.sub(r'\s+(?=\.[a-z]{2,})', '', text)  # Remove spaces before domain extensions

                # Find all URLs in the page text
                found_urls = URL_PATTERN.findall(text)
                for url in found_urls:
                    # Clean up URL if needed
                    # Remove trailing punctuation that might have been included
                    if url.endswith(('.', ',', ')', ']', ';', ':', '"', "'", '>')):
                        url = url[:-1]

                    # Remove any remaining whitespace in URLs (PDF extraction sometimes inserts spaces)
                    url = re.sub(r'\s+', '', url)

                    # Validate the URL structure (requires scheme and domain)
                    if re.match(r'^https?://[-a-zA-Z0-9@:%._\+~#=]+\.[a-zA-Z0-9()]{1,6}', url):
                        urls.add(url)

        logger.debug(f"Found {len(urls)} URLs in {pdf_path}")
        return urls

    except Exception as e:
        logger.error(f"Error processing {pdf_path}: {e}")
        return set()


async def process_pdfs(
    dir_path: Path,
    output_file: Path,
    max_workers: int = None
) -> Dict[str, Any]:
    """Process PDF files in a directory to extract URLs.

    Args:
        dir_path: Path to directory containing PDF files
        output_file: Path to output file for URLs
        max_workers: Maximum number of concurrent workers

    Returns:
        Dictionary with processing statistics
    """
    # Find all PDF files in the directory and subdirectories
    pdf_files = list(dir_path.glob('**/*.pdf'))

    if not pdf_files:
        logger.warning(f"No PDF files found in {dir_path}")
        return {"total_pdfs": 0, "processed_pdfs": 0, "total_urls": 0}

    all_urls = set()
    processed_files = 0

    # Use ThreadPoolExecutor for CPU-bound PDF processing
    with Progress() as progress:
        task = progress.add_task("[cyan]Processing PDF files...", total=len(pdf_files))

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit all PDF processing tasks
            future_to_pdf = {
                executor.submit(extract_urls_from_pdf, pdf_file): pdf_file
                for pdf_file in pdf_files
            }

            # Process results as they complete
            for future in concurrent.futures.as_completed(future_to_pdf):
                pdf_file = future_to_pdf[future]
                try:
                    urls = future.result()
                    all_urls.update(urls)
                    processed_files += 1
                    progress.update(task, advance=1, description=f"[cyan]Processed {processed_files}/{len(pdf_files)} PDF files")
                except Exception as e:
                    logger.error(f"Error processing {pdf_file}: {e}")

    # Write all unique URLs to the output file
    with open(output_file, "w") as f:
        for url in sorted(all_urls):
            f.write(f"{url}\n")

    return {
        "total_pdfs": len(pdf_files),
        "processed_pdfs": processed_files,
        "total_urls": len(all_urls)
    }


@app.command()
def extract(
    pdf_dir: Path = typer.Argument(..., help="Directory containing PDF files"),
    output_file: Path = typer.Option(
        Path("extracted_urls.txt"),
        "--output", "-o",
        help="Output file path for the extracted URLs"
    ),
    max_workers: Optional[int] = typer.Option(
        None,
        "--max-workers", "-w",
        help="Maximum number of concurrent workers (default: number of CPU cores)"
    ),
):
    """Extract URLs from PDF files in a directory.

    This command will search for all PDF files in the specified directory (including subdirectories),
    extract URLs from each file, and write all unique URLs to the output file.
    """
    if not pdf_dir.exists():
        typer.echo(f"Error: Directory {pdf_dir} does not exist")
        raise typer.Exit(code=1)

    if not pdf_dir.is_dir():
        typer.echo(f"Error: {pdf_dir} is not a directory")
        raise typer.Exit(code=1)

    typer.echo(f"Extracting URLs from PDF files in {pdf_dir}")

    try:
        results = asyncio.run(process_pdfs(pdf_dir, output_file, max_workers))

        typer.echo(f"\nExtraction complete:")
        typer.echo(f"  Total PDF files found: {results['total_pdfs']}")
        typer.echo(f"  Successfully processed: {results['processed_pdfs']}")
        typer.echo(f"  Total unique URLs extracted: {results['total_urls']}")
        typer.echo(f"\nURLs have been saved to {output_file}")

    except Exception as e:
        typer.echo(f"Error: {e}")
        raise typer.Exit(code=1)


def main():
    """Entry point for the pdfs2txt command."""
    app()


if __name__ == "__main__":
    main()