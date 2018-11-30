import urllib.request
from html.parser import HTMLParser
import urllib, http
import re
import datetime

links = []
value = []


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if tag != 'a':
            return
        attr = dict(attrs)
        links.append(attr)

    def handle_data(self, data):
        value.append(data)

def unique_word(number_of_iteration = 1000, base_url = "https://www.prothomalo.com", first_route="/", file_name = str(datetime.datetime.now())):

    file_name += '.txt'
    final_value = set()
    not_visited_link = set()
    visited_link = set()
    not_visited_link.add(first_route)
    pattern_for_regex = re.compile(r'[^\u0980-\u09E5\u09F0-\u09FF\u0020]')
    interation = 0
    while len(not_visited_link) is not 0:

        if interation >= number_of_iteration:
            break
        else:
            interation += 1
        current_route = not_visited_link.pop()
        visited_link.add(current_route)

        try:
            source = urllib.request.urlopen(base_url+current_route)
            # print("https://www.prothomalo.com"+current_route)

        except Exception as e:
            continue

        data = MyHTMLParser()
        data.links = []
        data.value = []
        try:
            data.feed(str(source.read(), 'utf-8'))
        except Exception as e:
            continue

        # all value in web page

        for v in value:
            values = re.sub(pattern_for_regex, '', v)
            if len(values.split()):
                final_value.update(values.split())

        new_links = set()

        for l in links:
            try:
                new_links.add(l["href"])
            except Exception as e:
                continue
        not_visited_link.update(new_links-visited_link)
        print("Route: ", len(visited_link))
        new_links.clear()
        del data

    file = open(file_name, 'w+')
    for word in final_value:
        file.write(word+'\n')
    file.close()


