import redis
import requests


def do_request(url):
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    cached_url = r.get(url)

    if cached_url:
        return cached_url

    resp = requests.get(url)
    payload = resp.content.decode('utf-8')

    r.set(url, payload)

    return payload
