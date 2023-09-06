import requests

BASE = "http://127.0.0.1:5000/"


data = [{"likes": 10, "name": "prajwal", "views": 100},
        {"likes": 23, "name": "pop", "views": 200},
        {"likes": 67, "name": "soap", "views": 400},
        {"likes": 56, "name": "asdw", "views": 300}
]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()

response = requests.get(BASE + 'video/2')
print(response.json())
