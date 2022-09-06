from API_KEY import API_KEY
import requests
import urllib.request
import json


def get_hash_name(data):
    data = data.split()
    hash_name = ''
    for i in range(len(data)):
        hash_name += data[i]
        hash_name += '%20'

    hash_name = hash_name[:-3]
    hash_name = hash_name.replace('|', '%7C')
    hash_name = hash_name.replace('(', '%28')
    hash_name = hash_name.replace(')', '%29')
    return hash_name


def main():
    print(get_hash_name('AWP | Worm God (Factory New)'))


if __name__ == '__main__':
    main()
