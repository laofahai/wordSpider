#!/bin/python3
# coding: utf-8

# an English learning tool for programmers

from base.lauguage import Language, mergeAllFile
from base.spider import getSpider

spiders = {
    "vue": [
        "VueGuide"
    ],
    "springGuide": [
        "SpringBoot", "Spring"
    ],
    
}


if __name__ == "__main__":

    for moduleName in spiders:
        spiderList = spiders[moduleName]
        for spiderName in spiderList:
            text = getSpider(moduleName, spiderName).run()

            lang = Language(text)
            lang.wordFrequancyToFile(moduleName, spiderName)


    mergeAllFile()