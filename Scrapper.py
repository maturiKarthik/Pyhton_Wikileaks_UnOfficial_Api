from bs4 import BeautifulSoup
import requests
import Const


class ScrapManager(object):

    def __init__(self, url):
        if str(url).startswith("http"):
            self.soup = self.soup_tags(self.__get_content(url))
        else:
            self.soup = self.soup_tags(str(url))

    def soup_tags(self, html_cnt):
        return BeautifulSoup(html_cnt, Const.PARSER)

    def __get_content(self, url):
        return requests.get(url).content

    def find_elements(self, html_tag, attr):
        if attr != "no":
            return self.soup.findAll(html_tag, attr)
        return self.soup.findAll(html_tag)
