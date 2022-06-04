import requests

print("Input handles. example: tourist, slime, Um_nik")
arr = input()
users = list(map(str, arr.split(',')))
results = []

for user in users:
    u = user.replace(' ', '')
    response = requests.get("https://codeforces.com/api/user.status?handle=" +  u  + "&from=1")
    data = response.json()
    count_succes = 0
    if (data['status'] == 'OK'):
        for d in data['result']:
            if (d['verdict'] == 'OK'):
                count_succes += 1
        results.append([u, count_succes])
    else:
        results.append([u, 'Not found'])

for result in results:
    print(result[0] + ": " + str(result[1]))