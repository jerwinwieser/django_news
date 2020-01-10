from bs4 import BeautifulSoup as bs
from datetime import timedelta, timezone, datetime
import requests

html = requests.get("https://www.nu.nl/").content
bsobj = bs(html, "html.parser")


headers = bsobj.find_all("div", {"class": "zone clearfix"})
print(bsobj)