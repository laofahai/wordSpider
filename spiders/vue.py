from base.spider import BasicSpider

class VueGuide(BasicSpider):

    fromUrl = "https://vuejs.org/guide/introduction.html"
    
    def getLinksFromListPage(self, bs):
        return bs.select('#VPSidebarNav a')

    def getContent(self, bs):
        return bs.select(".VPContentDoc .content")[0].text