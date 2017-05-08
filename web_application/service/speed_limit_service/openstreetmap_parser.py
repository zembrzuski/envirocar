from bs4 import BeautifulSoup


def extract_tags_information(tag):
    return [tag.get("k"), tag.get("v")]


def  extact_information_from_way(way):
    information = dict()

    information['id'] = way.get("id")
    information['uid'] = way.get("uid")

    tags = way.find_all("tag")

    for tag in tags:
        tag_info = extract_tags_information(tag)
        information[tag_info[0]] = tag_info[1]

    return information


def do_the_parsing(payload):
    soup = BeautifulSoup(payload)
    ways = soup.find_all('way')

    ways_information = list(map(lambda way: extact_information_from_way(way), ways))

    print("oi")

    return ways_information
