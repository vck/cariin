from bs4 import BeautifulSoup as bs4
from requests import get
from hashlib import md5
import json

MAIN_URL = "https://pekanbaru.tribunnews.com"
content = get(MAIN_URL)
soup = bs4(content.text)
res = soup.find_all("div", {"class":"fr mt5 pos_rel"})
db = []

def get_content(url):
    r=s.find("div", {"class": "side-article txt-article"})
    if not r:
        return ""
    return r.text.strip("\n")

with open("db.txt", "a+") as f:
    for row in res:
        s = row.find_all("a")[0]
        url_id = md5(s["title"].encode()).hexdigest()
        url = s["href"]
        title = s["title"]
        full_url = MAIN_URL + "/" + url
        f.write(json.dumps({"url_id": url_id, "title": title, "url": url, "content": get_content(full_url)})+"\n")

