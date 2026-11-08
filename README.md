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
1. 'retrieve_epic_photos(date, api_key)':
requests one date's photos and returns a list of dictionaries, or an empty list on a non-200 status code or no photos
2. 'label_region(longitude)':
turns one longitude into a region name
3. 'count_photos_by_region(photos)':
returns a dictionary of photo counts per region
4. 'display_region_report(date, api_key)':
checks for an empty list, then prints the counts, a timeline with image links, and the busiest region

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
