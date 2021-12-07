import requests
import json
import os
import yaml
import requests

token = os.environ.get("GITHUB_TOKEN")
target_repo = os.environ.get("TARGET_REPO")
release = os.environ.get("RELEASE")
repo = os.environ.get("REPO")

with open("./plugin.yml") as yml:
    plugin = yaml.load(yml, Loader=yaml.FullLoader)
    
    headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"token {token}",
    "Content-Type": "application/json"
    }
    body = {
    "event_type": "index-plugin",
    "client_payload": {
        "plugin": plugin,
        "release": release,
        "repo": repo
        }
    }

    uri = f"https://api.github.com/repos/{target_repo}/dispatches"
    resp = requests.post(uri, headers=headers, json=body)

    if resp.status_code != 204:
        raise Exception(f'error calling {uri} - status code: {resp.status_code}')
