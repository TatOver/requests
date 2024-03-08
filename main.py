import requests

website = 'https://jsonplaceholder.typicode.com/posts/1'
print(requests.get(website).json())
response = requests.put(website, data = {
    "id": 1,
    "userId": 12,
    "title": "my new post about myself",
    "body": "body for my post Tatsiana"
})

print(response.json())



#headers = {
   # "User-Agent": "OVERONE"
#}
#response = requests.get("https://httpbin.org/get", headers=headers, params={'a':'b'})
#response = requests.post("https://httpbin.org/post",
                        # headers=headers,
                        # params={'a':'b'},
                        # json = {'username': 'Tanya'}
                        # )

#if response.status_code == 200:
   # print('ok')
#response.raise_for_status()

#print(response.text)