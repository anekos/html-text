#!/bin/python

from html.parser import HTMLParser
import os

import requests

Blacklist = {'script', 'style'}


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.texts = []
        self.level = 0

    def handle_starttag(self, tag, attrs):
        if tag.lower() in Blacklist:
            self.level += 1

    def handle_endtag(self, tag):
        if tag.lower() in Blacklist:
            self.level -= 1

    def handle_data(self, data):
        if self.level == 0:
            if not data.strip() == '':
                self.texts.append(data)

def main(html_file):
    content = None
    if os.path.isfile(html_file):
        with open(html_file) as f:
            content = f.read()

    extractor = TextExtractor()
    extractor.feed(content)

    for text in extractor.texts:
        print(text)

if __name__ == '__main__':
    import fire
    fire.Fire(main)
