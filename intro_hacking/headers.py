#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests
import argparse

parser = argparse.ArgumentParser(description="Detector de headers")
parser.add_argument('-t', '--target', help = "Objetivo")
parser = parser.parse_args()


def main():
    if parser.target:
        try:
            url = requests.get(url=parser.target)
            headers = dict(url.headers)
            for h in headers:
                print(h + ' : ' + headers[h])
        except:
            print("404 Not Found")
    else:
        print("No hay objetivo")

if __name__ == '__main__':
    main()