import requests

with open("url_list.txt", 'w') as txt:
    txt.write("""http://imgs.xkcd.com/comics/python.png\n""")


class Downloader:
    def __init__(self, urls_text):
        self.urls = urls_text

    @property
    def image_list(self):
        with open(self.urls, 'r') as txt:
            return [i for i in txt]

    def download_png(self, image_name, image_url):
        response = requests.get(image_url)
        with open(f"{image_name}.png", 'wb') as im:
            im.write(response.content)

    def download_jpeg(self, image_name, image_url):
        response = requests.get(image_url)
        with open(f"{image_name}.jpeg", 'wb') as im:
            im.write(response.content)


obj_1 = Downloader("url_list.txt")
print(obj_1.image_list[0])
obj_1.download_png("image_3", obj_1.image_list[0])
