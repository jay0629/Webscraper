#!/usr/bin/python3.5

# first use sudo pip to install scrapy

import scrapy
import os
import sys
import subprocess
import platform
import re

class Scrape(scrapy.Spider):
    name = 'filmsdailySpider'
    start_urls = ['https://filmdaily.co/trailers']

    def parse(self, response):
        for title in response.css('.mkd-pt-two-content-top-holder-cell>h3'):
            yield {'Movie Trailers [*] ': title.css('a ::text').extract_first()}

        for next_page in response.css('mkd-post-info-date entry-date entry-date updated > a'):
            yield response.follow(next_page, self.parse)


def runspider():
    plat = platform.system()
    if plat in ["linux","Linux"]:
        fileName = "scrape_output"
        file = open(fileName, "w")
        file.write("Starting Scrape of ****Filmdaily***" + "\n" + "\n")
        file.close()

        os.system("scrapy runspider scraper.py 2>> scrape_output")

        file = open(fileName, "a")
        file.write("\n" + "Stopping Scrape of ****Filmdaily***")
        file.close()

        """file = open(fileName, "a")
        file.write("\n-----------------")
        for line in fileName:
            if re.findall(r'^{''Movie', re.M):
            #if re.findall(r'\{\'Movie', fileName, flags=re.MULTILINE):
                file.write(line[:-1])
            else:
                print("none")
        file.close()"""

    elif plat in ["darwin","Darwin"]:
        # MAC OS X
        print(plat)
        print("To do ")
        pass
    elif plat in ["win32","Win32"]:
        # Windows
        print(plat)
        print("To do ")
        pass
    elif plat in ["win64","Win64"]:
        # Windows 64-bit
        print(plat)
        print("To do ")
        pass

if __name__ == "__main__":
    runspider()
# scrapy runspider scraper.py
