#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : follow_external_only.py
# @Author: Armote
# @Date  : 2018/10/29 0029
# @Desc  :随机收集外链接地址：仅供学习参考,里面有个方法木有!getNextExternalLink() is None !

from urllib import request
from bs4 import BeautifulSoup
import datetime
import random
import re

pages =set()
random.seed(datetime.datetime.now())

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())


# 获取页面所有内链的列表
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    # 找出所有以"/"开头的链接
    for link in bsObj.findAll("a", href=re.compile("^(/|.*" + includeUrl + ")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks


# 获取页面所有外链的列表
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # 找出所有以"http"或"www"开头且不包含当前URL的链接
    for link in bsObj.findAll("a",
                              href=re.compile("^(http|www)((?!" + excludeUrl + ").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts


def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html)
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(startingPage)
        #return getNextExternalLink(internalLinks[random.randint(0,len(internalLinks) - 1)])
        #这里demo没有方法
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]


def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink("http://oreilly.com")
    print("随机外链是： " + externalLink)
    followExternalOnly(externalLink)


# 收集网站上发现的所有外链列表
allExtLinks = set()
allIntLinks = set()


def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    bsObj = BeautifulSoup(html)
    internalLinks = getInternalLinks(bsObj, splitAddress(siteUrl)[0])
    externalLinks = getExternalLinks(bsObj, splitAddress(siteUrl)[0])
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            print("即将获取链接的URL是： " + link)
            allIntLinks.add(link)
            getAllExternalLinks(link)

getAllExternalLinks("http://oreilly.com")

followExternalOnly("http://oreilly.com")