import requests, json
from pprint import pprint

# Set the content type to JSON.
headers = {"Content-Type": "application/json"}

# Crawl all URLs inside the target URL.
payload = {
    "url": "https://www.amazon.com/",
    "filters": {
        "crawl": [".*"],
        "process": [".*"],
        "max_depth": 1
    },
    "scrape_params": {
        "user_agent_type": "desktop",
    },
    "output": {
        "type_": "sitemap"
    }
}

# Create a job and store the JSON response.
response = requests.request(
    'POST',
    'https://ect.oxylabs.io/v1/jobs',
    auth=('USERNAME', 'PASSWORD'),  # Your credentials go here.
    headers=headers,
    json=payload,
)

# Write the decoded JSON response to a .json file.
with open('job_sitemap.json', 'w') as f:
    json.dump(response.json(), f)
    f.close()

# Print the decoded JSON response.
pprint(response.json())
