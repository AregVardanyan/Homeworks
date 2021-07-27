import threading
import json
import requests

list1 = ['1907', '1332', '1740', '1238', '0846', '0202', '1625', '1250', '1119', '1105']
with open("images.json", 'w') as js:
    url_list = []
    for i in list1:
        url_list.append(f"https://cdn.eso.org/images/screen/eso{i}a.jpg")
    json.dump(url_list, js, indent=1)


def foo(j):
    with open("images.json", 'r') as js:
        images = json.load(js)
        response = requests.get(images[j])
        print(f"Getting {images[j]}")
        with open(f"image{j}.jpg", 'wb') as im:
            im.write(response.content)


for j in range(10):
    td = threading.Thread(target=foo, args=(j,))
    td.start()
    td.join()
