import requests


url = "https://api.github.com/users/octocat"

response = requests.get(url)

print("Status code:", response.status_code)

if response.status_code == 200:
    data = response.json()

    print("Username:", data["login"])
    print("Name:", data["name"])
    print("Public repositories:", data["public_repos"])
    print("Followers:", data["followers"])
    print("Following:", data["following"])
    print("GitHub URL:", data["html_url"])
else:
    print("Request failed.")