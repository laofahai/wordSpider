# coding: utf-8

from sre_compile import isstring
from bs4 import BeautifulSoup

import time
import requests
import re
import importlib
import sys
import traceback


class BasicSpider():

    retryCount = 5

    sleepTime = 1

    def run(self, url = None):
        if url is None:
            url = self.fromUrl

        rawHtml = self.fetchHtml(url)

        if rawHtml is None:
            print("failed to fetch: " + url)
            sys.exit()

        bs = BeautifulSoup(rawHtml, "lxml")
        links = self.getLinksFromListPage(bs)

        domain = re.search(r"((http|https)://.*?)\/", url).group(1)
        baseurl = re.search(r"((http|https)://.*?)\/", url).group()
        result = []

        for link in links:
            
            if isstring(link):
                href = link
            else:
                href = link.get("href")

            if href is None:
                continue

            if  href.startswith("/"):
                href = domain + href
            elif not href.startswith("http"):
                href = baseurl + href

            try:
                html = self.fetchHtml(href)
                if html is None or not html.startswith('<'):
                    continue
                bs = BeautifulSoup(html, "lxml")
            except:
                continue
            
            text = self.getContent(bs)
            result.append(self.cleanText(text))

            time.sleep(self.sleepTime)
            
        return " ".join(result)

    def getLinksFromListPage(self, bs):
        return bs.select('body a')
    
    def getContent(self, bs):
        return bs.select('body')[0].text

    def cleanText(self, text):
        text = text.replace('\n', ' ').replace('.', ' ')
        # camel case to space
        text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
        return text

    def getListLinks(self, rawHtml):
        return BeautifulSoup(rawHtml, 'html.parser').select('body a')


    def get_proxy(self):
        return requests.get("http://127.0.0.1:5010/get/").json()

    def delete_proxy(self, proxy):
        requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

    # your spider code

    def fetchHtml(self, url):
        # ....
        retry_count = 5
        proxy = self.get_proxy().get("proxy")
        print("Using proxy: %s, fetching: %s" % (proxy, url))
        while retry_count > 0:
            try:
                print("proxy tring times left: %d" % retry_count)
                response = requests.get(url, proxies={"http": "http://{}".format(proxy)})
                return response.text
            except Exception as e:
                retry_count -= 1
        # 删除代理池中代理
        self.delete_proxy(proxy)
        return None

def getSpider(module, spider):
    module = importlib.import_module( "." + module, "spiders")
    return getattr(module, spider)()