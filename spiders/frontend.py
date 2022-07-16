from base.spider import BasicSpider

class VueGuide(BasicSpider):

    fromUrl = "https://vuejs.org/guide/introduction.html"
    
    def getLinksFromListPage(self, bs):
        return bs.select('#VPSidebarNav a')

    def getContent(self, bs):
        return bs.select(".VPContentDoc .content")[0].text

class FlutterDoc(BasicSpider):

    fromUrl = "https://docs.flutter.dev/"
    
    def getLinksFromListPage(self, bs):
        return bs.select('.site-sidebar a')

    def getContent(self, bs):
        if bs.select(".site-content") is None or len(bs.select(".site-content")) < 1:
            return ""
        return bs.select(".site-content")[0].text