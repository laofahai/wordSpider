from base.spider import BasicSpider

class Spring(BasicSpider):
    
    fromUrl = "https://spring.io/guides/"
    
    def getLinksFromListPage(self, bs):
        return bs.select('.content a')

    def getContent(self, bs):
        return bs.select(".main-body--wrapper")[0].text

class SpringBoot(BasicSpider):
    
    fromUrl = "https://docs.spring.io/spring-boot/docs/current/reference/html/"
    
    def getLinksFromListPage(self, bs):
        return bs.select('.hdlist a')

    def getContent(self, bs):
        return bs.select("#doc")[0].text