"""Run the Actor with the Apify client and print a few fields per row."""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("clearfetch/tiktok-profile-scraper").call(run_input={"profiles": ["nasa", "tiktok"], "maxVideosPerSource": 5})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("type"), item.get("username") or item.get("authorUsername"), item.get("followers") or item.get("playCount"))
