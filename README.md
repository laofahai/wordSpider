# Word spider for programmers

This simple project is built to help the programmers on English learning by crawling the words on given website such as some framework's documentation, then you can import the words to your own wordbook, I wish this can help on enrich your English vocabulary.

## Requirements
* [Proxy pool](https://github.com/jhao104/proxy_pool), so please follow the link and configure it first.
* [nltk](https://www.nltk.org/)  for handle words.
* [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/) for HTML parse.

## Installation

Configure the `Proxy Pool` first, and then:

```shell
git clone https://github.com/laofahai/wordSpider.git
cd wordSpider
pip install -r requirements.txt
```

That's all.

## Stop words
you can define your own stop words in the `stopWords.txt`.

## Usage
I have already create some spiders such as for Spring guide, Vue guide documentations, and the vacabulary already exists in the `words` folder.

if you want to crawl more, just define the spider in the `spiders` folder like this:

```python
from base.spider import BasicSpider

class VueGuide(BasicSpider):

    # This is the list page of documentations, spider will start crowling from here.
    fromUrl = "https://vuejs.org/guide/introduction.html"
    
    # The detail pages links in the list page
    def getLinksFromListPage(self, bs):
        return bs.select('#VPSidebarNav a')

    # Get the main content you want from detail page.
    def getContent(self, bs):
        return bs.select(".VPContentDoc .content")[0].text
```

and define the spiders in the `wordSpider.py`