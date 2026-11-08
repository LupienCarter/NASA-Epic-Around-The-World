# NASA-Epic-Around-The-World

This python program uses NASA's EPIC API to show where on Earth the camera was facing throughout one day.

## What it does?
1. Requests the 'natural; collection from the EPIC API for a date
(default 2016-03-08, or the date the user enters.)
2. Uses each photo's centroid longitude to label a region: Americas, Africa
and Europe, Asia, or Pacific.
3. Counts photos per region and prints a timeline with times, regions
and images links.
4. Reports which region was photographed most.

## How to run
1. Install Python 3 and the 'requests' library: 'pip install request'
2. Run: 'python epic_around_the_world.py'
3. Enter a date (YYYY-MM-DD) or  press Enter for the default.

## Program design
1. 'get_photos(date)' : retrieves data from the API.
2. 'get_region(longitude)' : classifies a longitude into a region.
3. 'build_image_link(photo)' : builds the image URL from the date and image name.
4. 'count_regions(photos)' : builds a dictionary of photo counts per region.
5. 'print_results(...)' : formats and displays the output.

## API Key
The code uses 'DEMO_KEY' . For heavier use, get a free key at 
https://api.nasa.gov/ and replace it.

## Data Source
NASA EPIC API: https://epic.gsfc.nasa.gov/about/api

## Decomposition Diagram
This diagram shows how the program is broken into functions. 'Main()' collects the date
, the calls 'get_photos()' to retrieve data from the API. The photos are passed to 
'count_regions()', which uses 'get_regions()' to label each photo, and finally 'print_results()' displays
the output, using 'build_image_links()' for each photo's link.
<img width="960" height="720" alt="Around the world_" src="https://github.com/user-attachments/assets/b5d63188-0fc7-4876-a638-8f6a03853eff" />
