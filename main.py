# Purpose: Read the monthly folders for photos and generate HTML file
# 1. Loop through all the monthly folder directories
# 2. If no HTML file found
# 3. Get the name of all the image files in the folder
# 4. Insert the image names into a HTML file

import os
import re

# Define the # of photos to show per row here
num_of_photos_per_row = 6

folders = os.listdir(os.getcwd())
for folder in folders:
    if folder not in [".DS_Store", "venv", ".idea", "main.py"]:
        images = os.listdir(f"{os.getcwd()}/{folder}")
        image_count = 0
        html_exist = False
        html_row_content = ""
        html_container_content = ""
        html_text = ""
        images.sort()
        for image in images:
            html_match = re.search("^.*\.(html)$", image)
            if html_match:
                html_exist = True
                break
            image_match = re.search("^.*\.(jpg)$", image)
            if image_match:
                image_count += 1
                html_row_content += f"<div class='col-2'><img src='{image}' class='img-fluid' /></div>"
            if image_count == num_of_photos_per_row:
                html_container_content += f"<div class='row g-0'>{html_row_content}</div>"
                image_count = 0
                html_row_content = ""
        html_container_content += f"<div class='row g-0'>{html_row_content}</div>"
        if not html_exist:
            html_text = f"<!doctype html><html lang='en'><head><meta name='viewport' content='width=device-width, initial-scale=1'><title>Unforgotten</title><link href='https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We' crossorigin='anonymous'></head><body><div class='container-fluid p-0'>{html_container_content}</div></body></html>"

            f = open(f"{os.getcwd()}/{folder}/Unforgotten_{folder.replace(' ', '')}.html", "w")
            f.write(html_text)
            f.close()
            html_text = ""
