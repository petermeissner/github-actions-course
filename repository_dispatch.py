import requests


token = open('github_token.txt', 'r').read().replace("\n", "")

url = "https://api.github.com/repos/petermeissner/github-actions-course/dispatches"
r = requests.post(
  url=url, 
  headers=
    {
      "Accept": "application/vnd.github.v3+json",
      "Authorization": "token " + token
    },
  json = {
    "event_type": "manual_trigger",
    "client_payload": {
      "msg": "Peter was here ... buh!"
    }
  }
)

print("\n == URL ==")
print(r.request.url)

print("\n == HEADERS ==")
print(r.request.headers)


print("\n == REQUEST BODY ==")
print(r.request.body)


print("\n == RESPONSE ==")
try:
  print(r.json())
except:
  print(r.raw.headers['Status'])
