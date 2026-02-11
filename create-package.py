#!/usr/bin/env python3
"""
Create a WordPress plugin package zip file
"""
import os
import zipfile
from pathlib import Path

def create_plugin_zip():
    """Create the plugin zip file with all necessary files"""

    # Plugin directory name (what will be the folder name in WordPress)
    plugin_folder = "gsap-scroll-animations"

    # Output zip file name
    zip_filename = f"{plugin_folder}.zip"

    # Files and folders to include
    include_items = [
        "gsap-scroll-animations.php",
        "ANIMATION-DEMO.html",
        "ANIMATION-EXAMPLES.html",
        "README.md",
        "readme.txt",
        "LICENSE",
        "assets/",
        "lib/"
    ]

    # Create zip file
    print(f"Creating {zip_filename}...")

    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for item in include_items:
            if item.endswith('/'):
                # It's a directory
                folder = item.rstrip('/')
                if os.path.exists(folder):
                    for root, dirs, files in os.walk(folder):
                        for file in files:
                            file_path = os.path.join(root, file)
                            arcname = os.path.join(plugin_folder, file_path)
                            print(f"  Adding: {file_path}")
                            zipf.write(file_path, arcname)
            else:
                # It's a file
                if os.path.exists(item):
                    arcname = os.path.join(plugin_folder, item)
                    print(f"  Adding: {item}")
                    zipf.write(item, arcname)
                else:
                    print(f"  Warning: {item} not found, skipping")

    # Get file size
    file_size = os.path.getsize(zip_filename)
    file_size_kb = file_size / 1024

    print(f"\n✓ Package created successfully!")
    print(f"  File: {zip_filename}")
    print(f"  Size: {file_size_kb:.2f} KB")
    print(f"\nReady to upload to WordPress!")

if __name__ == "__main__":
    create_plugin_zip()
