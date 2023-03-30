import requests, json
from pprint import pprint

# Store the JSON response containing parsed results.
parsed_results = requests.request(
    'GET',
    'https://ect.oxylabs.io/v1/jobs/{id}/aggregate/1',  # Replace {id] with the job ID.
    auth=('USERNAME', 'PASSWORD'),  # Your credentials go here.
)

# Write the decoded JSON response to a .json file.
with open('parsed_results_1.json', 'w') as f:
    json.dump(parsed_results.json(), f)
    f.close()

# Print the decoded JSON response.
pprint(parsed_results.json())
