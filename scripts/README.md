# Updating list of food days
`parse_wiki_page.py` parses the wiki page and prints JSON formatted results. Diff them with `data.js` to see what changed and verify things look fine. Then overwrite the cache variable in `data.js` with the results.

Note: make sure that the countries listed all have flags in `images/flags/`

# Generating images of food days
`generate_image_links.py` will read `data.js` and find which food days are missing images. The ones that are missing will hit Google image search and grab the first image. The new set of images will be printed out - overwrite the `img_cache` variable in `data.js`.

`generate_picture_table.py` will create a local html file that you can open to visually verify the images and make sure they are appropriate.

# Uploading images
Using direct links to images will lead to link rot, so `upload_imgur.py#upload_to_imgur` will take images in `images.txt` (copy/paste json from `data.js` - `img_cache`) and upload them to imgur, writing the new images to `images2.txt`. if you get rate limited, wait a bit, then try again after moving `images2.txt` to `images.txt`

Some food days may have disappeared, so delete them from imgur since they're no longer needed. Use `find_unused_links.py` to generate the list of imgur links to delete, saving them to a file called `unused.txt`, then use `upload_imgur.py#remove_from_imgur` to delete them. Use `find_unused_links.py#without_unused_links` to get the `img_cache` with the unused links removed and copy them back over to `data.js`

