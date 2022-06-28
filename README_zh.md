# 一个单词爬虫

这个小工具用来从一些指定的网站上（如一些框架的文档）爬取内容，并通过 `nltk` 解析后统计词频，用来帮助程序员学习英语。输出的结果你可以导入到你的单词本里面，这样就可以有针对性的提高常用词汇量或者练习你的发音。

## 需求
* [Proxy pool](https://github.com/jhao104/proxy_pool) 爬虫代理池，首先你要先配置好这个
* [nltk](https://www.nltk.org/)  用于文本处理
* [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/) 用于解析 HTML

## 安装

首先按照上面的链接配置代理池，然后：

```shell
git clone https://github.com/laofahai/wordSpider.git
cd wordSpider
pip install -r requirements.txt
```

## 停止词
你可以在 `stopWords.txt` 中配置停止词，我已经在里面配置了一些高频的停止词。

## 使用
我已经创建了几个爬虫，如爬取 Vue Guide 和 Spring Guide 的，爬取结果已经存在 `words` 目录中，如果你想要获取更多，只需要创建你自己的爬虫：

```python
from base.spider import BasicSpider

class VueGuide(BasicSpider):

    # 文档列表的链接
    fromUrl = "https://vuejs.org/guide/introduction.html"
    
    # 文档列表页面的内容区域, bs 是 BeautifulSoup 的实例
    def getLinksFromListPage(self, bs):
        return bs.select('#VPSidebarNav a')

    # 每一页文档页面中的内容区域
    def getContent(self, bs):
        return bs.select(".VPContentDoc .content")[0].text
```

然后将你的爬虫配置到 `wordSpider.py`

## 产物

`words` 目录中包含了程序运行的产物，每个爬虫都会有一个单独的文件按词频排序存放爬取的单词，单词已经经过停止词过滤、词性还原等操作，这样你就可以把他们导入到你的背单词软件里面了，比如`不背单词`，对于一些专有名词()、缩写或不正确的单词，软件还会再过滤一遍。