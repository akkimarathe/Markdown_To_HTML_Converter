import markdown
import os
import logging
from database import save_conversion_history

# Logging setup
logging.basicConfig(filename="logs/conversion.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

def convert_markdown_to_html(md_content, filename):
    """Converts Markdown content to HTML and saves it to a file."""
    try:
        html_content = markdown.markdown(md_content)

        output_dir = "frontend/output/"
        os.makedirs(output_dir, exist_ok=True)
        
        output_filename = filename.replace(".md", ".html")
        output_path = os.path.join(output_dir, output_filename)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        logging.info(f"Converted {filename} to {output_path}")
        save_conversion_history(filename, output_path)  # Save in DB

        return output_filename

    except Exception as e:
        logging.error(f"Error converting {filename}: {str(e)}")
        return None
