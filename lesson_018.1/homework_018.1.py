import requests

BASE_URL = "https://images-api.nasa.gov"

search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",
    "media_type": "image",
    "page_size": 20
}

response = requests.get(search_url, params=search_params)
response.raise_for_status()

data = response.json()

items = data["collection"]["items"]

nasa_ids = []
for item in items:
    try:
        nasa_id = item["data"][0]["nasa_id"]
        nasa_ids.append(nasa_id)
    except (KeyError, IndexError):
        continue

print(f"Found nasa_id: {len(nasa_ids)}")

asset_url_template = f"{BASE_URL}/asset/{{nasa_id}}"

downloaded = 0
for nasa_id in nasa_ids:
    if downloaded >= 2:
        break

    asset_url = asset_url_template.format(nasa_id=nasa_id)
    asset_response = requests.get(asset_url)
    asset_response.raise_for_status()
    asset_data = asset_response.json()

    try:
        files = asset_data["collection"]["items"]
    except KeyError:
        continue

    jpg_url = None
    for file in files:
        href = file.get("href", "")
        if href.lower().endswith(".jpg"):
            jpg_url = href
            break

    if not jpg_url:
        continue

    print(f"Download: {jpg_url}")

    img_response = requests.get(jpg_url)
    img_response.raise_for_status()

    filename = f"mars_photo{downloaded + 1}.jpg"

    with open(filename, "wb") as f:
        f.write(img_response.content)

    print(f"Save as {filename}")

    downloaded += 1

print("Ready")
