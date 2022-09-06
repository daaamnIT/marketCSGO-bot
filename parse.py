from API_KEY import API_KEY
import requests
import urllib.request
import json
from operator import itemgetter


def sort(data):
    for i in range(len(data)):
        flot = data[i]['extra']['float']
        data[i]['flot'] = flot
    mylist = sorted(data, key=itemgetter('price', 'flot'))

    return mylist



def get_url(data):
    url_pattern = 'https://market.csgo.com/en/item/[4302244430]-[480085569]-[AK-47%20%7C%20Redline%20(Field-Tested)]/'
    hash_name_arr = data['market_hash_name'].split()
    hash_name = ''
    for i in range(len(hash_name_arr)):
        hash_name += hash_name_arr[i]
        hash_name += '%20'
    url = 'https://market.csgo.com/en/item/'+str(data['class'])+'-'+str(data['instance'])+'-'+hash_name + '/'

    return url


def main(hash_name):
    hash_name = hash_name
    with urllib.request.urlopen("https://market.csgo.com/api/v2/search-item-by-hash-name-specific?key="+API_KEY+"&hash_name=" + hash_name) as url:
        data = json.loads(url.read().decode())

    res = data
    res = sort(data['data'])
    print(json.dumps(res, indent=4, sort_keys=True))
    return res


if __name__ == '__main__':
    main()
