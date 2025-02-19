import requests
API_KEY = "WbjHA3yLLrRftuybWgT1"
MODEL_ID = "-_-uoo19/1"
IMAGE_PATH = "Test.webp"
url = f"https://detect.roboflow.com/{MODEL_ID}?api_key={API_KEY}"
with open(IMAGE_PATH, "rb") as image_file:
    files = {"file": image_file}
    response = requests.post(url, files=files)
data = response.json()
num_persons = len(data.get("predictions", []))
print(f"Number of persons detected: {num_persons}")