"""Command-line interface for archiving URLs."""

import asyncio
import logging
import sys
from pathlib import Path
from typing import Optional

import typer

from archiver.archiver import URLArchiver

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
    ]
)

logger = logging.getLogger(__name__)

app = typer.Typer(help="Archive URLs from a file using multiple archiving services.")


@app.command()
def archive(
    file_path: Path = typer.Argument(..., help="Path to file containing URLs, one per line"),
    max_concurrency: int = typer.Option(5, "--max-concurrency", "-c", help="Maximum number of concurrent URL archiving operations"),
    user_agent: str = typer.Option("Archive Links Client/0.1.0", "--user-agent", "-ua", help="User agent string for HTTP requests"),
    output_json: Optional[Path] = typer.Option(None, "--output", "-o", help="Output file for JSON results (optional)")
):
    """Archive URLs from a file using multiple archiving services.

    Takes a file with one URL per line and archives each URL using multiple services.

    Example:
        archiver archive urls.txt --max-concurrency 3 --output results.json
    """
    if not file_path.exists():
        typer.echo(f"Error: File {file_path} does not exist")
        raise typer.Exit(code=1)

    typer.echo(f"Starting archiving URLs from {file_path}")
    archiver = URLArchiver(user_agent=user_agent, max_concurrency=max_concurrency)

    try:
        # Run the archiver in an event loop
        results = asyncio.run(archiver.archive_urls_from_file(str(file_path)))

        # Print results
        success_count = 0
        failure_count = 0
        total_urls = len(results)

        for url, service_results in results.items():
            url_success = any(r.get("success", False) for r in service_results)
            if url_success:
                success_count += 1
            else:
                failure_count += 1

        typer.echo(f"\nArchiving complete. Results:")
        typer.echo(f"  Total URLs: {total_urls}")
        typer.echo(f"  Successfully archived: {success_count}")
        typer.echo(f"  Failed to archive: {failure_count}")

        # Optionally save results to JSON file
        if output_json:
            import json
            with open(output_json, "w") as f:
                json.dump(results, f, indent=2)
            typer.echo(f"\nResults saved to {output_json}")

        return results

    except Exception as e:
        typer.echo(f"Error: {e}")
        raise typer.Exit(code=1)


def main():
    """Entry point for the CLI."""
    app()


if __name__ == "__main__":
    main()