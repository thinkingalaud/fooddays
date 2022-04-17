# Updating list of food days
`parse_wiki_page.py` parses the wiki page and prints JSON formatted results. Diff them with `data.js` to see what changed and verify things look fine. Then overwrite the cache variable in `data.js` with the results.

# Generating images of food days
`generate_image_links.py` will read `data.js` and find which food days are missing images. The ones that are missing will hit Google image search and grab the first image. The new set of images will be printed out - overwrite the `img_cache` variable in `data.js`.
`generate_picture_table.py` will create a local html file that you can open to visually verify the images and make sure they are appropriate.

# Uploading images
Using direct links to images will lead to link rot, so `upload_imgur.py` will take images in `images.txt` and upload them to imgur, writing the new images to `images2.txt`
