import requests

ACCESS_TOKEN = "your_linkedin_api_token"
profile_url = "https://api.linkedin.com/v2/me"

headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
response = requests.get(profile_url, headers=headers)

if response.status_code == 200:
    print(response.json())  # LinkedIn profile data
else:
    print("Error fetching data:", response.text)
