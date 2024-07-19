from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET
import random


def get_curr_num():
    url = "https://xkcd.com/rss.xml"
    response = requests.get(url)
    response.raise_for_status()
    root = ET.fromstring(response.content)
    curr_num = 0
    for item in root.findall(".//channel/item"):
        link = item.find("link")
        curr_num = link.text.split("https://xkcd.com/")[-1].split("/")[0]
        break
    return int(curr_num)


def get_random_num():
    return random.randint(1, get_curr_num())


def get_random():
    num = get_random_num()
    link = "https://xkcd.com/" + str(num)
    return scrape(link)


def get_latest():
    num = get_curr_num()
    link = "https://xkcd.com/" + str(num)
    return scrape(link)


def scrape(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")

    comic_div = soup.find("div", id="comic")
    img_tag = comic_div.find("img") if comic_div else None

    title_div = soup.find(
        "div", id="ctitle"
    )  # Correctly finds the div with id 'ctitle'
    title_text = (
        title_div.get_text() if title_div else "No title found"
    )  # Extract text if found, else default message

    img_title = (
        img_tag.get("title") if img_tag else "No image title found"
    )  # Get the title attribute from the img tag

    if img_tag:
        return [
            "https:" + img_tag["src"],
            url,
            title_text,
            img_title,
        ]  # Include img_title as the fourth item
    else:
        return None
