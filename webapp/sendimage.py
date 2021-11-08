import requests
url = 'http://127.0.0.1:5000/detection'
my_img = {'image': open('boars.jpg', 'rb')}
r = requests.post(url, files=my_img)

# convert server response into JSON format.
print(r.json())