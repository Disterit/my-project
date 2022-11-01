import json
from bs4 import BeautifulSoup
import lxml
import requests

count = 0
for i in range(1,3):
    url = f"https://phil-nsk.ru/festivali/festivali/rossiya-muzyka-sibir/?PAGEN_1={i}"


    list_fest_urls = []

    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }


    req = requests.get(url=url, headers=headers)
    src = req.text

    soup = BeautifulSoup(src, "lxml")

    url_fest = soup.find_all("a", class_="name")

    for url_fests in url_fest:
        fest_page = url_fests.get("href")
        full_fest_page = "https://phil-nsk.ru" + fest_page
        list_fest_urls.append(full_fest_page)


    list_afisha_urls = []


    for list_url_festivals in list_fest_urls:
        q = requests.get(list_url_festivals, headers=headers)
        soup_1 = q.text
        soup = BeautifulSoup(soup_1, "lxml")

        block_festival = soup.find_all(class_="g-left item")

        list_for_urls_fest = []

        for item in block_festival:
            fest_block_urls = item.find(class_="name-in").get("href")
            fest_http = "https://phil-nsk.ru" + fest_block_urls
            list_for_urls_fest.append(fest_http)


        for urls_fest in list_for_urls_fest:
            req = requests.get(urls_fest, headers=headers)
            soup = BeautifulSoup(req.text, "lxml")

            fest_list_result = []

            name_festival = soup.find("h1").text
            date_festival = soup.find("div", class_="date g-left").text
            price_festival = soup.find("span", class_="price")
            if price_festival == None:
                continue
            else:
                price_festival = price_festival.text.strip()


            fest_list_result.append(
                {
                    "name_festival": name_festival,
                    "date_festival": date_festival,
                    "price_festival": price_festival,
                }
            )


            with open("fest_list_result.json",  "a", encoding="utf-8") as file:
                json.dump(fest_list_result, file, indent=4, ensure_ascii=False)
            count += 1
            print(f"Fest parsing:{count}")
