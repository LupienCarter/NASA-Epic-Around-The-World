import requests

DEFAULT_DATE = "2016-03-08"


def retrieve_epic_photos(date, api_key):
    """Request one date's photos. Returns a list of dicts, or [] on any problem."""
    url = f"https://api.nasa.gov/EPIC/api/natural/date/{date}"
    try:
        response = requests.get(url, params={"api_key": api_key}, timeout=10)
    except requests.RequestException:
        print("Could not reach the EPIC API. Check your internet connection.")
        return []

    if response.status_code != 200:
        print(f"Request failed with status code {response.status_code}.")
        return []

    return response.json()


def label_region(longitude):
    """Return which part of Earth faces the camera for this longitude."""
    if -120 <= longitude < -30:
        return "Americas"
    elif -30 <= longitude < 60:
        return "Africa and Europe"
    elif 60 <= longitude < 150:
        return "Asia"
    else:
        return "Pacific"


def count_photos_by_region(photos):
    """Return a dict of how many photos fall in each region."""
    counts = {}
    for photo in photos:
        region = label_region(photo["centroid_coordinates"]["lon"])
        counts[region] = counts.get(region, 0) + 1
    return counts


def display_region_report(date, api_key):
    """Retrieve photos, count them by region, and print the report."""
    photos = retrieve_epic_photos(date, api_key)
    if not photos:
        print(f"No EPIC photos available for {date}.")
        return

    counts = count_photos_by_region(photos)

    print(f"\nEPIC took {len(photos)} photos on {date}.\n")
    print("Photos per region:")
    for region, count in counts.items():
        print(f"  {region}: {count}")

    print("\nTimeline:")
    year, month, day = date.split("-")
    for photo in photos:
        time = photo["date"].split(" ")[1]
        region = label_region(photo["centroid_coordinates"]["lon"])
        link = (f"https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}"
                f"/png/{photo['image']}.png?api_key={api_key}")
        print(f"  {time}  {region:<18} {link}")

    busiest = max(counts, key=counts.get)
    print(f"\nMost photographed region: {busiest}")


# Main program
api_key = "DEMO_KEY"
date = input(f"Enter a date (YYYY-MM-DD) or press Enter for {DEFAULT_DATE}: ").strip()
if date == "":
    date = DEFAULT_DATE
display_region_report(date, api_key)
