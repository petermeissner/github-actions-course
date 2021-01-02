import requests


url = "https://api.github.com/repos/petermeissner/github-actions-course/dispatches"
requests.post(
  url=url, 
  headers={"accept": "application/vnd.github.v3+json"},
  data={"event_type": "manual_trigger"}
)

