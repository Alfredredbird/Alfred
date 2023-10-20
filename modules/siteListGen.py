# this is the function to generate the site list. we moved it from the ./modules.py file to help shorten its length.

import os
from os import walk
import urllib
import time
from colorama import *
from pathlib import Path
from bs4 import BeautifulSoup as bs
import requests
import json
from rich.console import Console
from torrequest import TorRequest
from os import listdir
from os.path import isfile, join
from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs
from bs4 import BeautifulSoup
import wget
import random
def siteListGen(console, testall, get_random_string, domain_extensions, uname):

    input2 = input("CHAR: ⤷ ")
    trys = input("  TRYS: ⤷ ")
    siteType = input("     TYPE: ⤷ ")
    siteGenOPtions = input("       OPTIONS: ⤷ ")
    if siteGenOPtions == "":
        lol = 1
    if siteGenOPtions != "":
        if "-a" in siteGenOPtions:
            testall = True
        if "-d" in siteGenOPtions:
            domain_extensions = True

    if input2 == "":
        lol = 1
    if input2 != "":
        with console.status("Testing.....") as status:
            siteLst = []
            b = 0
            if testall == False:
                if siteType != "":
                    while b != int(trys):
                        b += 1
                        siteLst.append(
                            "https://"
                            + str(get_random_string(int(input2)))
                            + str(siteType)
                        )
                if siteType == "":
                    while b != int(trys):
                        b += 1
                        gen = get_random_string(int(input2))
                        siteLst.append("https://" + str(gen) + ".com")
            # generates a combo of sites
            if testall == True:
                if siteType != "":
                    for _ in range(int(trys)):
                        siteLst.append(
                            "https://"
                            + str(get_random_string(int(input2)))
                            + str(siteType)
                        )
                if siteType == "":
                    domains = [
                        ".com",
                        ".net",
                        ".org",
                        ".xyz",
                        ".edu",
                        ".co",
                        ".us",
                        ".uk",
                    ]
                    for _ in range(int(trys)):

                        gen = get_random_string(int(input2))
                        siteLst += [f"https://{gen}{dom}" for dom in domains]

                        pass
            if domain_extensions == True:
                if siteType != "":
                    for _ in range(int(trys)):
                        siteLst.append(
                            "https://"
                            + str(get_random_string(int(input2)))
                            + str(siteType)
                        )
                if siteType == "":
                    domains = [
                        ".com/u/",
                        ".net/u/",
                        ".org/u/",
                        ".xyz/u/",
                        ".edu/u/",
                        ".co/u/",
                        ".us/u/",
                        ".uk/u/",
                        ".com/user/",
                        ".net/user/",
                        ".org/user/",
                        ".xyz/user/",
                        ".edu/user/",
                        ".co/user/",
                        ".us/user/",
                        ".uk/user/",
                        ".com/profile/",
                        ".net/profile/",
                        ".org/profile/",
                        ".xyz/profile/",
                        ".edu/profile/",
                        ".co/profile/",
                        ".us/profile/",
                        ".uk/profile/",
                    ]
                    for _ in range(int(trys)):

                        gen = get_random_string(int(input2))

                        siteLst += [f"https://{gen}{dom}{uname}" for dom in domains]
                        pass

            siteError = 0
            # print(siteLst)
            i = 0
            f = open("working.txt", "w")
            while i != len(siteLst):
                try:
                    r = requests.get(siteLst[i], timeout=1)
                    print(
                        "["
                        + Fore.GREEN
                        + "+"
                        + Fore.RESET
                        + "] "
                        + str(siteLst[i])
                        + " "
                        + str(i)
                        + "/"
                        + str(trys)
                    )
                    if r.status_code >= 200 and r.status_code <= 500:
                        f.write(
                            '{"site": "'
                            + str(siteLst[i])
                            + "/"
                            + '", "nsfw": "Unknown"}'
                            + "\n"
                        )
                except (
                    requests.exceptions.ConnectionError,
                    requests.exceptions.Timeout,
                    IndexError,
                    requests.exceptions.HTTPError,
                    requests.exceptions.BaseHTTPError,
                    requests.exceptions.SSLError,
                    requests.exceptions.TooManyRedirects,
                    requests.exceptions.TooManyRedirects,
                    requests.exceptions.RetryError,
                    TypeError,
                    requests.exceptions.ChunkedEncodingError,
                ):
                    siteError += 1
                    print(
                        "["
                        + Fore.RED
                        + "-"
                        + Fore.RESET
                        + "] "
                        + "?"
                        + " "
                        + str(i)
                        + "/"
                        + str(trys)
                    )
                except KeyboardInterrupt():
                    print("Stopping..... Saved To alfred/working.txt")
                # tbh its 11 at night rn and idk what i+=1 does
                i += 1
            print(str(siteError) + " Not Working Sites...")
