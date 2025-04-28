# archive-links

A simple archival tool for capturing snapshots of web pages using multiple archival services.

## Features

- Archives URLs using multiple services:
  - Internet Archive (Wayback Machine)
  - Archive.ph
  - Memento Web
- Asynchronous processing for improved performance
- Command-line interface for easy use
- Handles rate limiting with exponential backoff
- Processes URLs concurrently with configurable limits
- Extracts URLs from PDF files for archiving

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/archive-links.git
cd archive-links

# Install the package
pip install -e .
```

## Usage

### Command Line Interface

The package provides simple command-line interfaces for archiving URLs:

```bash
# Archive URLs from a file
archive-links archive urls.txt

# Archive URLs with custom concurrency limit
archive-links archive urls.txt --max-concurrency 3

# Save results to a JSON file
archive-links archive urls.txt --output results.json
```

The URLs file should contain one URL per line. Lines starting with `#` are treated as comments.

### Extract URLs from PDF Files

You can extract URLs from a directory of PDF files:

```bash
# Extract URLs from PDF files in a directory
pdfs2txt extract /path/to/pdf/directory

# Extract URLs and save to a specific file
pdfs2txt extract /path/to/pdf/directory --output extracted_urls.txt

# Control the number of concurrent workers
pdfs2txt extract /path/to/pdf/directory --max-workers 4
```

This will extract all unique URLs from the PDF files and save them to a text file, which can then be used with the archiving tool.

### Python API

You can also use the archiver programmatically in your Python code:

```python
import asyncio
from archiver.archiver import URLArchiver

# Create an archiver instance
archiver = URLArchiver(max_concurrency=5)

# Archive a list of URLs
async def archive_my_urls():
    urls = ["https://example.com", "https://example.org"]
    results = await archiver.archive_urls(urls)
    return results

# Run the asynchronous function
results = asyncio.run(archive_my_urls())
```

## Original Usage (GitHub Actions)

1. clone/fork the repo
2. update and commit `manifest.txt`
3. upload/push to your own GitHub

To push an update to `manifest.txt` on the main branch without triggering the workflow, suffix your commit message with ` [skip ci]`.
