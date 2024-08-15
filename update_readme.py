import requests
import re

# GitHub username
username = 'Yabe12'

# Attempt to fetch contributions data from the GitHub API
response = requests.get(f"https://api.github.com/users/{username}/events")

# Check if the request was successful
if response.status_code == 200:
    contributions_data = response.text

    # Debug: Print the data to verify its contents
    print("Contributions Data:", contributions_data)

    # Attempt to extract the total contributions using regex
    contributions_match = re.search(r'"totalContributions":\s*(\d+)', contributions_data)

    if contributions_match:
        total_contributions = contributions_match.group(1)
        print(f"Total Contributions: {total_contributions}")
    else:
        raise ValueError("Could not find 'totalContributions' in the data. Please check the API response structure.")
else:
    print(f"Failed to fetch data from GitHub API. Status code: {response.status_code}")
