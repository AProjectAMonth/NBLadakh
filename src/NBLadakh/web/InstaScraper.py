import requests
import json
from ast import literal_eval

class InstaImage:

    '''Class to store an image's details'''

    def __init__(self, code, low_res_url, embed_code):
        self.code = code
        self.low_res_url = low_res_url
        self.embed_code = embed_code


class InstaScraper:

    '''Class to act as scraper'''

    url = "https://www.instagram.com/{0}/media/"

    custom_headers = {
        'USER-AGENT': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
        'ACCEPT-LANGUAGE': "en-US,en;q=0.8",
        'ACCEPT': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'ACCEPT-ENCODING': "gzip, deflate, br"
    }

    def __init__(self, user_name):
        # print('Initialised for' + user_name)
        self.url = self.url.format(str(user_name))
        self.images = []
        self.extract_data(self.url)

    def get_raw_json(self, url):
        try:
            r = requests.get(url, headers=self.custom_headers)
            raw_json = r.text
            # print('got raw_json')
            return raw_json
        except:
            print('Error in raw_json')
            return 'Error'

    def get_embed_code(self, code):
        oEmbed_api_url = "https://api.instagram.com/oembed/?url=http://instagr.am/p/{}"
        r = requests.get(oEmbed_api_url.format(code), headers=self.custom_headers)
        embed_json = json.loads(r.text)
        # print('Got Embed code')
        eval_str = embed_json["html"]
        eval_str = self.clean(eval_str)
        # print(eval_str)
        return eval_str

    @staticmethod
    def clean(dirty_str):
        dirty_str = dirty_str.replace("//platform", "http://platform")
        dirty_str = dirty_str.replace("margin: 1px 1px 12px;", "margin: 0;")
        dirty_str = dirty_str.replace("&lt;", "<")
        dirty_str = dirty_str.replace("&gt;", ">")
        clean_str = dirty_str.replace("&quote;", "\"")
        return clean_str

    def extract_data(self, url):
        # print('Extracting data')
        raw_json = self.get_raw_json(url)
        if raw_json is 'Error':
            print('Error Ocurred')
            pass
        media = json.loads(raw_json)
        for i in media["items"]:
            code = i["code"]
            # print(code)
            low_res_url = i["images"]["low_resolution"]["url"]
            embed_code = self.get_embed_code(code)
            img = InstaImage(code, low_res_url, embed_code)
            self.images.append(img)
        # print(media["more_available"])
        if media["more_available"]:
            # print('more available')
            max_id = media["items"][-1]["id"]
            print(max_id)
            url = self.url + "?max_id=" + max_id
            self.extract_data(url)


if __name__ == '__main__':
    images = InstaScraper('nbladakh').images
    for img in images:
        print(img.code)


