import requests

#### THIS CODE SOLELY EXISTS FOR TO SEE WHAT THE OUTPUT OF THE JOKE API IS
#### NOT CONNECTED TO MAIN.PY

limit = 1
api_url = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(limit)
response = requests.get(api_url, headers={'X-Api-Key': 'frEz+k/OaaH4fYcwSsIxUg==myHIK3hhq76k9s6G'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)
