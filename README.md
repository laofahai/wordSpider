# Word spider for programmers

This simple project is built to help the programmers on English learning by crawling the words on given website such as some framework's documentation, then you can import the words to your own wordbook to improve your vocabulary or practice the pronunciation, I wish this can help on enrich your English vocabulary.

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
You can define your own stop words in the `stopWords.txt`, actually I have already defined some of that.

## Usage
I have already create some spiders such as for Spring guide, Vue guide documentations, and the vocabulary already exists in the `words` folder.

if you want to crawl more, just define the spider in the `spiders` folder like this:

```python
from base.spider import BasicSpider

class VueGuide(BasicSpider):

    # This is the list page of documentations, spider will start crawling from here.
    fromUrl = "https://vuejs.org/guide/introduction.html"
    
    # The detail pages links in the list page
    def getLinksFromListPage(self, bs):
        return bs.select('#VPSidebarNav a')

    # Get the main content you want from detail page.
    def getContent(self, bs):
        return bs.select(".VPContentDoc .content")[0].text
```

and define the spiders in the `wordSpider.py`

## Artifacts
The `words` directory will save the words frequency for every spider, and the `words/__all.txt` is all of them. so you can import that to your learning APP like `不背单词`.


Hope everything goes well with you.