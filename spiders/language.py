from base.spider import BasicSpider

class PHPDoc(BasicSpider):

    fromUrl = "https://www.php.net/manual/en/"
    
    def getLinksFromListPage(self, bs):
        return bs.select('#layout-content a')

    def getContent(self, bs):
        return bs.select("#layout-content")[0].text

class GolangDoc(BasicSpider):

    fromUrl = "https://golang.google.cn/doc/"
    
    def getLinksFromListPage(self, bs):
        return bs.select('.Article a')

    def getContent(self, bs):
        if bs.select(".Article") is None or len(bs.select(".Article")) < 1:
            return ""
        return bs.select(".Article")[0].text

class PythonTutorial(BasicSpider):

    fromUrl = "https://docs.python.org/3/tutorial/index.html"
    
    def getLinksFromListPage(self, bs):
        return bs.select('#the-python-tutorial a')

    def getContent(self, bs):
        if bs.select(".body") is None or len(bs.select(".body")) < 1:
            return ""
        return bs.select(".body")[0].text