import requests
import os

BASE_URL = "http://127.0.0.1:8080"

IMAGE_PATH = "test.jpg"

if not os.path.exists(IMAGE_PATH):
    print(f"ERROR: fail {IMAGE_PATH} not found!")
    exit(1)

# 1. POST /upload
print("Downloading image...")
with open(IMAGE_PATH, "rb") as f:
    files = {
        "image": (os.path.basename(IMAGE_PATH), f, "image/jpeg")
    }

    response = requests.post(f"{BASE_URL}/upload", files=files)
    response.raise_for_status()

data = response.json()
image_url = data["image_url"]
print(f"✅ [UPLOAD] Image URL: {image_url}")

filename = image_url.split("/")[-1]
print(f"📄 Filename: {filename}")

# 2. GET /image/<filename>
print("Request img inf (text/plain)...")
headers = {
    "Accept": "text/plain"
}

response = requests.get(f"{BASE_URL}/image/{filename}", headers=headers)
response.raise_for_status()

print(f"✅ [GET as text] Response JSON: {response.json()}")

# 2b. GET /image/<filename>
print("\n🖼️  Requesting image...")
headers = {
    "Accept": "image/jpeg"
}

response = requests.get(f"{BASE_URL}/image/{filename}", headers=headers)
response.raise_for_status()

# Save img
saved_image_path = f"downloaded_{filename}"
with open(saved_image_path, "wb") as f:
    f.write(response.content)

print(f"✅ [GET as image] Img save as: {saved_image_path}")
print(f"   File size: {len(response.content)}")


# 3. DELETE /delete/<filename>
print("\n Deleting img...")
response = requests.delete(f"{BASE_URL}/delete/{filename}")
response.raise_for_status()

print(f"✅ [DELETE] Response JSON: {response.json()}")

print("\n✅ All operations done!")