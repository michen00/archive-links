import sys
import markdown
from weasyprint import HTML

def convert_md_to_pdf(input_file, output_file):
    # Read the markdown file
    with open(input_file, 'r') as f:
        md_content = f.read()

    # Convert markdown to HTML
    html = markdown.markdown(
        md_content,
        extensions=['tables', 'fenced_code']
    )

    # Add CSS for styling
    html_doc = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Academic Literature on Airport Economics</title>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }}
            h1 {{ color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }}
            h2 {{ color: #2c3e50; margin-top: 30px; border-bottom: 1px solid #ddd; padding-bottom: 5px; }}
            h3 {{ margin-top: 25px; }}
            details {{ margin-bottom: 15px; padding: 10px; background-color: #f8f9fa; border-radius: 5px; border: 1px solid #ddd; }}
            summary {{ font-weight: bold; cursor: pointer; }}
            hr {{ margin: 30px 0; border: 0; border-top: 1px solid #eee; }}
            a {{ color: #3498db; text-decoration: none; }}
            a:hover {{ text-decoration: underline; }}
            .keywords {{ font-style: italic; margin-top: 10px; }}
        </style>
    </head>
    <body>
        {html}
    </body>
    </html>
    """

    # Generate PDF
    HTML(string=html_doc).write_pdf(output_file)
    print(f"PDF successfully created as '{output_file}'")

if __name__ == "__main__":
    convert_md_to_pdf('/tmp/academic_sources/academic_sources.md', '/tmp/academic_sources/academic_sources.pdf')
