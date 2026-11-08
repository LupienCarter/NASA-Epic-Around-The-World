import requests

API_KEY = "DEMO_KEY"
BASE_URL = "https://api.nasa.gov/EPIC"
DEFAULT_DATE = "2016-03-08"


def get_photos(date):
    """Request one date's photos. Returns a list, or None if the request failed."""
    url = f"{BASE_URL}/api/natural/date/{date}"
    try:
        response = requests.get(url, params={"api_key": API_KEY}, timeout=10)
    except requests.RequestException:
        print("Could not reach the EPIC API. Check your internet connection.")
        return None

    if response.status_code == 403:
        print("Error 403: the API key is missing or invalid.")
        return None
    if response.status_code == 429:
        print("Error 429: rate limit reached. Try again later or use your own key.")
        return None
    if response.status_code != 200:
        print(f"Unexpected error: status code {response.status_code}.")
        return None

    return response.json()


def get_region(longitude):
    """Label which part of Earth faces the camera, based on longitude."""
    if -120 <= longitude < -30:
        return "Americas"
    elif -30 <= longitude < 60:
        return "Africa and Europe"
    elif 60 <= longitude < 150:
        return "Asia"
    else:
        return "Pacific"


def build_image_link(photo):
    """Build the image URL from the photo's date and image name."""
    year, month, day = photo["date"].split(" ")[0].split("-")
    return f"{BASE_URL}/archive/natural/{year}/{month}/{day}/png/{photo['image']}.png?api_key={API_KEY}"


def count_regions(photos):
    """Return a dictionary of how many photos fall in each region."""
    counts = {}
    for photo in photos:
        region = get_region(photo["centroid_coordinates"]["lon"])
        counts[region] = counts.get(region, 0) + 1
    return counts


def print_results(date, photos, counts):
    """Print the counts, a timeline, and the most photographed region."""
    print(f"\nEPIC took {len(photos)} photos on {date}.\n")

    print("Photos per region:")
    for region, count in counts.items():
        print(f"  {region}: {count}")

    print("\nTimeline:")
    for photo in photos:
        time = photo["date"].split(" ")[1]
        region = get_region(photo["centroid_coordinates"]["lon"])
        print(f"  {time}  {region:<18} {build_image_link(photo)}")

    busiest = max(counts, key=counts.get)
    print(f"\nMost photographed region: {busiest}")


def main():
    date = input(f"Enter a date (YYYY-MM-DD) or press Enter for {DEFAULT_DATE}: ").strip()
    if date == "":
        date = DEFAULT_DATE

    photos = get_photos(date)
    if photos is None:
        return
    if len(photos) == 0:
        print(f"No EPIC photos for {date}. Try a date after June 2015.")
        return

    counts = count_regions(photos)
    print_results(date, photos, counts)


main()
