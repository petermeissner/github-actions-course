import requests


token = open('github_token.txt', 'r').read().replace("\n", "")

url = "https://api.github.com/repos/petermeissner/github-actions-course/actions/workflows/05_repository_dispatch.yml/dispatches"
r = requests.post(
  url=url, 
  headers=
    {
      "Accept": "application/vnd.github.v3+json",
      "Authorization": "token " + token
    },
  json={"ref": "master"}
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
