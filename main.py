import requests
import json

def handler():
    try:
        with open("endpoints.json") as f:
            endpoints = json.load(f)
    except Exception as e:
        print("Failed to load endpoints:", e)
        return

    for url in endpoints:
        try:
            resp = requests.get(url)
            print(f"Pinged {url}, status: {resp.status_code}")
        except Exception as e:
            print(f"Failed to ping {url}: {e}")

# Run the handler when the script is triggered
if __name__ == "__main__":
    handler()
