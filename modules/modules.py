#!/usr/bin/env python3
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
import string


def redirects1(modes, input1):
    input2 = input("   ⤷ ")
    if input2 == "":
        lol = 1
    if input2 != "":
        modes += input1
        try:
            ars = bool(input2)
            return input1, modes
        except ValueError:
            print("Timeout Must Be A Number")
            if "-d" in input2:
                input1.replace("-d", "")


def logo(uname):
    os.system("cls" if os.name == "nt" else "clear")
    print(
        Fore.RED
        + """   
                                    
                         ╓φ▒Γ ,╖╗⌐
                        Φ╬╬Γ @╬╬Γ ╔▓
                       ^╣╬▓µ╣╬▓  ▄▓▓▓
                     ╔▓  ╙╬╬╬╩  ╜▀▀▀╙╙
                    ▄▓▓▓▄  ╣╬▓µ╓╓╖╗╗φφ@φ
                  "╙╙╙╙╙"  ╟╬╬╣╝╣╬╬▀╨╣╬▓                 
                  ¥φφφφφφφφ╬╬╩   ╫╬▓, ╟╬⌐                 
                   └╙╨╨╨╨╫╬╬╩ ╔▓  ╚╬╬L `                 
                    %φφφφ╬╬╩ ╔▓▓▓╕ ╙╬Γ                    __,---. 
                     `╙╨╨╨╜  ▀▀▀▀▀¬                      /__|o\  ) 
                 ░█▀▀▄░█░░█▀▀░█▀▀▄░█▀▀░█▀▄                `-\ / /
                 ▒█▄▄█░█░░█▀░░█▄▄▀░█▀▀░█░█                  ,) (,
                 ▒█░▒█░▀▀░▀░░░▀░▀▀░▀▀▀░▀▀░                 //   \\
                   A Advanced OSINT Tool                  {(     )}
===========================================================""===""=========
                                                            |||||
                 By Jeffrey Montanari                        |||
                 Twiter: @alfredredbird1                      |

             Thanks To Our Sponsor: Smoke-wolf
"""
    )
    print("             The Target Username: " + uname + Fore.RESET)


def siteDownloader(modes, input1):
    input2 = input("SITE: ⤷ ")
    if input2 == "":
        lol = 1
    if input2 != "":
        modes += input1

        try:
            # thanks to https://thepythoncode.com/article/extract-web-page-script-and-css-files-in-python for the code refrence
            response = urllib.request.urlopen(input2)
            webContent = response.read().decode("UTF-8")

            f = open("./downloadedSites/downloaded-site.html", "w")
            f.write(webContent)
            f.close
            print("Downloaded Page And Saved To: downloaded-site.html")
            url = input2
            session = requests.Session()
            session.headers[
                "User-Agent"
            ] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
            # get the HTML content
            html = session.get(url).content
            # parse HTML using beautiful soup
            soup = bs(html, "html.parser")
            # get the JavaScript files
            script_files = []
            for script in soup.find_all("script"):
                if script.attrs.get("src"):
                    # if the tag has the attribute 'src'
                    script_url = urljoin(url, script.attrs.get("src"))
                    script_files.append(script_url)
            # get the CSS files
            css_files = []
            for css in soup.find_all("link"):
                if css.attrs.get("href"):
                    # if the link tag has the 'href' attribute
                    css_url = urljoin(url, css.attrs.get("href"))
                    css_files.append(css_url)
            print("Total script files in the page:", len(script_files))
            print("Total CSS files in the page:", len(css_files))
            # write file links into files
            with open("./downloadedSites/javascript_files.txt", "w") as f:
                for js_file in script_files:
                    print(js_file, file=f)

            with open("./downloadedSites/css_files.txt", "w") as f:
                for css_file in css_files:
                    print(css_file, file=f)

            return modes
        except requests.exceptions.RequestException:
            print("Error Downloading Web Content!")
        except ConnectionError:
            print("Error Downloading Web Content!")
        except ValueError:
            print("Unknow URL!")
        except requests.exceptions.ConnectionError:
            print("Error Downloading Web Content!")
        except requests.exceptions.HTTPError:
            print("Error Downloading Web Content!")
        except requests.exceptions.InvalidURL:
            print("Error Downloading Web Content!")
        except ConnectionError:
            print("Error")


def list_proxys():
    input2 = input("TYPE:  ⤷ ")
    # check if the directory exists
    if input2 == "":
        lol = 1
    if input2 == "http":
        if os.path.exists("./proxys/http.txt"):
            file1 = open("./proxys/http.txt", "r")
            Lines = file1.readlines()

            count = 0
            L = [Lines]

            for line in Lines:
                count += 1
                print("Proxy {}: {}".format(count, line.strip()))
        else:
            print(Fore.RED + "Cant Find The Proxy File!")
            print(Fore.RESET)

    elif input2 == "socks4":
        if os.path.exists("./proxys/socks4.txt"):
            file1 = open("./proxys/socks4.txt", "r")
            Lines = file1.readlines()

            count = 0
            L = [Lines]

            for line in Lines:
                count += 1
                print("Proxy {}: {}".format(count, line.strip()))
        else:
            print(Fore.RED + "Cant Find The Proxy File!")
            print(Fore.RESET)

    elif input2 == "socks5":
        if os.path.exists("./proxys/socks5.txt"):
            file1 = open("./proxys/socks5.txt", "r")
            Lines = file1.readlines()

            count = 0
            L = [Lines]

            for line in Lines:
                count += 1
                print("Proxy {}: {}".format(count, line.strip()))

        else:
            print(Fore.RED + "Cant Find The Proxy File!")
            print(Fore.RESET)


def read_save(slectpath):
    if slectpath == "":
        dir_path = Path.home() / "Downloads"

        file_name = "usernames.alfred"
        file_path = os.path.join(dir_path, file_name)
    if slectpath != "":
        file_path = os.path.join(slectpath)
    # check if the directory exists
    if os.path.exists(file_path):
        # reads the file
        file = open(file_path, "r+")
        file1 = open(file_path, "r")
        Lines = file1.readlines()

        count = 0
        L = [Lines]

        for line in Lines:
            count += 1
            print("Captured {}: {}".format(count, line.strip()))

        file.close()

    else:
        print(Fore.RED + "Cant Find The Save File!")
        print(Fore.RESET)


def ping():
    headers = headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)"
    }
    print(Fore.RED + "Defults To HTTPS")

    print(Fore.RESET + " ")

    reqSite = input("⤷ ")

    try:
        print(Fore.RESET + "Status Code:")
        test = requests.get(reqSite)
        print(test.status_code)

    except:
        print(Fore.RED + "Error!")
        print(Fore.RESET + " ")




def qexit():
    exitInput = input("Exit? [Y/N]")
    if exitInput == "Y" or exitInput == "y":
        exit(0)
    if exitInput == "N" or exitInput == "n":
        print("Continueing....")


def proxyCheck(modes, input1):
    typeInput = input("TYPE: ⤷ ")
    if typeInput != "":
        input2 = input("    IP: ⤷  ")
        if input2 == "":
            print("    You Need An IP Silly.")
            lol = 1
        if input2 != "":
            modes += input1

            input3 = input("     PORT: ⤷  ")
            if input3 != "":
                try:
                    # finish adding connectton options
                    prxs = input2 + ":" + input3
                    proxies = {"{typeInput}": prxs}
                #  print("Proxy: " + input2 + ":" + input3)
                except requests.exceptions.ProxyError:
                    print(Fore.RED + "Proxy Error!" + Fore.RESET)

                print("")
                print("     Save Proxy To File?")
                saveProxy = input("         [Y/n]?  ⤷ ")
                if saveProxy == "Y" or saveProxy == "y":
                    with open("proxyList.txt", "a") as fp:
                        fp.write(" \n" + input2 + ":" + input3)
                        fp.close()

                elif saveProxy == "N" or saveProxy == "n":
                    print(
                        "Continuing"
                        + Fore.RED
                        + "."
                        + Fore.GREEN
                        + "."
                        + Fore.YELLOW
                        + "."
                        + Fore.RESET
                    )

            if input3 == "":
                print("     Wheres The Port? Lol")
                lol = 1
                return lol

    if typeInput == "":
        print("Needs Proxy Type!")
        if "-c" in input1:
            input1.replace("-c", "")


def timeoutC(modes, input1):
    input2 = input("   ⤷ ")
    if input2 == "":
        lol = 1
        return lol
    if input2 != "":
        modes += input1

        try:
            timeout = int(input2)
            return timeout
        except ValueError:
            print("Timeout Must Be A Number")
            if "-t" in input2:
                input1.replace("-t", "")


def darkAlfred(console, uname):
    # clears the terminal when Dark Alfred is ran
    os.system("cls" if os.name == "nt" else "clear")
    test = False
    lol = 0
    inputnum = 0
    start = False
    siteList = []
    modes = ""
    iptext = ""
    try:
        rp = requests.get("http://ipecho.net/plain")
        iptext = rp.text
    except ConnectionError:
        print("Connection Error! Cant Get Ip Address.")
    print(
        Fore.BLACK
        + """
                    ,╓╔╦╦╦╖╓
                ╔▒╠╠╩╙╙╙"╙╙╚╬╠▒╦,
              ,Φ╠╩"   ,╓▄▄╓,    ╙
            @╠╩   *████▀▀▀███▓,   ╬╬,
           ╬╠╙  ▄µ          ╙███   ╬╠µ
          ╠╠╩  ██▌  ╓▒╠╩╝╠╬╦  ╙██   ╠╠                                                                                                  
          ╠╠  j██  ⌠╠╩    ╚╠▒  ██▌  ╠╠⌐                 
          ╠╠   ██  └╠╬    ╠╠╩  ██▌  ╠╠⌐
          ╚╠φ  ╟██   ╚╬╠╠╠╩`  ▄██  ,╠╬
           ╠╠╦  ╙██▌,      ,,  ╙  ,╠╠
            ╚╬`   ╙▀█████████▀   #╠╩
               ,@╦     └└─    ╓@╠╩`
                "╚╠╠▒▒φφφφ@▒╠╠╩╙

░▒█▀▀▄░█▀▀▄░█▀▀▄░█░▄░░░█▀▀▄░█░░█▀▀░█▀▀▄░█▀▀░█▀▄
░▒█░▒█░█▄▄█░█▄▄▀░█▀▄░░▒█▄▄█░█░░█▀░░█▄▄▀░█▀▀░█░█
░▒█▄▄█░▀░░▀░▀░▀▀░▀░▀░░▒█░▒█░▀▀░▀░░░▀░▀▀░▀▀▀░▀▀░
 """
    )
    print("Searching The DarkWeb For Usernames With: " + uname + ".")
    print("Your Ip Is: " + iptext)
    print(
        Fore.RED
        + "===================================================================="
        + Fore.RESET
    )
    print(
        """
Caution! By Using This Might Expose 
You To Dangerous Websites Or Content.
Read More On The Doc's https://github.com/Alfredredbird/alfred/wiki
"""
    )
    print(
        Fore.RED
        + "===================================================================="
        + Fore.RESET
    )

    input1 = input("⤷  ")
    while test != True:
        if input1 != "":
            # if there is a problem with this code its prob this
            if "-tp" in input1:
                torPassword = input("Tor Password:  ⤷")
            if "-s" in input1:
                input2 = input("Are You Sure? [Y/N]? ⤷ ")
                if input2 == "":
                    lol = 1
                if input2 != "":
                    if input2 == "Y" or input2 == "y":

                        input3 = input("100% Sure? [Y/N]? ⤷ ")
                        if input2 != "":
                            if input2 == "Y" or input2 == "y":
                                #  modes += input1
                                #  inputnum += input2
                                print("Ok..")
                                start = True
                            if input2 == "N" or input2 == "n":
                                test = False
                                input1 = ""
                                print("Ok! Returing To Alfred.")
                                time.sleep(2)
                                return test

                    if input2 == "N" or input2 == "n":
                        test = False
                        input1 = ""
                        print("Ok! Returing To Alfred.")
                        time.sleep(2)
                        return test

        if "" in input1 and inputnum != "":
            test = True
        inputnum = ""
    if start == True:
        try:
            with open("sites.json", "r") as f:
                for jsonObj in f:
                    siteDic = json.loads(jsonObj)
                    siteList.append(siteDic)
        except FileNotFoundError:
            print(Fore.RED + "Cant Find Site File")

            exit(-1)
        except json.JSONDecodeError:
            print(Fore.RED + "Error With Site File" + Fore.RESET)
            exit(-9)

        dir_path = Path.home() / "Downloads"
        file_name = "usernames.alfred"
        file_path = os.path.join(dir_path, file_name)
        # check if the directory exists
        if os.path.exists(dir_path):
            # create the file
            print(" ")
            print("Creating / Overwriting Save File.")

        else:
            print("Directory doesn't exist.")
        with open(file_path, "w") as f:
            for site in siteList:

                with console.status("Working....") as status:
                    siteN = site["site"]
                    try:
                        tr = TorRequest(password=torPassword)
                        tr.reset_identity()
                        response = tr.get(siteN + uname)

                        if (
                            TorRequest.status_code >= 200
                            and TorRequest.status_code >= 300
                        ):
                            print(
                                "["
                                + Fore.GREEN
                                + "+"
                                + Fore.RESET
                                + "] "
                                + siteN
                                + uname
                            )
                            f.write("[" + "+" + "] " + siteN + uname + "\n")

                    except ConnectionError():
                        print("Connection Error!")


def printFiles():
    # ha ha Only Files. Sounds like something else, I wonder what? (Only Fans)
    onlyfiles = [f for f in listdir("./") if isfile(join("./", f))]
    return onlyfiles


def catFile():
    file_path = input("Filname:  ⤷ ")
    try:
        with open(file_path, "r") as f:
            for jsonObj in f:
                siteDic = json.loads(jsonObj)
                print(siteDic)

    except FileNotFoundError:
        print(Fore.RED + "Cant Find Site File")
    except json.JSONDecodeError:
        print(Fore.RED + "Error With Site File" + Fore.RESET)


# this is the module that edits the configuration file. needs to be cleaned up tho
def configEditor(config):
    # reads the config
    config.read("./config/config.ini")
    # gets input
    editConfigAwnser = input("Edit The Config? [y/n]: ⤷ ")
    # decieds what to do
    if editConfigAwnser == "y" or editConfigAwnser == "Y":
        # options
        print("[1] Check for updates: " + str(config.get("main", "checkforupdates")))
        print("[2] Show tips: " + str(config.get("main", "showtips")))
        # gets input
        editConfig = input("What Do You Want To Change? ⤷ ")
        # figures out what to do
        if editConfig == "1":
            # update config logic
            if config.get("main", "checkforupdates") == "yes":
                print("Ok! [checkforupdates] Is Set For Yes. Changing To No")
                config.set("main", "checkforupdates", "no")
                with open("./config/config.ini", "w") as f:
                    config.write(f)
                    return True
            # update config logic
            if config.get("main", "checkforupdates") == "no":
                print("Ok! [checkforupdates] Is Set For No. Changing To Yes")
                config.set("main", "checkforupdates", "yes")
                with open("./config/config.ini", "w") as f:
                    config.write(f)
                    return False
        if editConfig == "2":
            # update config logic
            if config.get("main", "showtips") == "yes":
                print("Ok! [showtips] Is Set For Yes. Changing To No")
                config.set("main", "showtips", "no")
                with open("./config/config.ini", "w") as f:
                    config.write(f)
                    return True
            # update config logic
            if config.get("main", "showtips") == "no":
                print("Ok! [showtips] Is Set For No. Changing To Yes")
                config.set("main", "showtips", "yes")
                with open("./config/config.ini", "w") as f:
                    config.write(f)
                    return False
    if editConfigAwnser == "n" or editConfigAwnser == "N":
        print("Aww ok")


def scriptDownloader(sitePaths, extinsion):
    count = 0
    file1 = open(sitePaths, "r")
    Lines = file1.readlines()
    L = [Lines]
    for line in Lines:
        count += 1
        # downloads the file from the site
        print("Downloading File: " + line)
        url = line
        r = requests.get(url, allow_redirects=True)
        try:
            open("./downloadedSites/file" + str(count) + extinsion, "wb").write(
                r.content
            )
        except FileNotFoundError:
            print("Cant Find: " + item + "Skiping!")
        except OSError:
            print("Permission Error")


def dirDump(mydir):
    filelist = [f for f in os.listdir(mydir)]
    for f in filelist:
        os.remove(os.path.join(mydir, f))


def errorCodes(ec):
    ec = 1
    return ec


# Function to download images
def download_images(image_urls, output_directory):
    for url in image_urls:
        try:
            image_filename = os.path.join(output_directory, os.path.basename(url))
            wget.download(url, image_filename)
            print(f"Downloaded: {image_filename}")
        except Exception as e:
            print(f"Error downloading image: {e}")


# Function to download videos
def download_videos(video_urls, output_directory):
    for url in video_urls:
        try:
            video_filename = os.path.join(output_directory, os.path.basename(url))
            wget.download(url, video_filename)
            print(f"Downloaded: {video_filename}")
        except Exception as e:
            print(f"Error downloading video: {e}")


# Main function
def imgandVidDownlaod(input2):
    url = input2
    output_directory = (
        "./downloadedSites/"  # Change this to your desired output directory
    )

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        # Find and download images
        img_tags = soup.find_all("img")
        img_urls = [img["src"] for img in img_tags if "src" in img.attrs]
        download_images(img_urls, output_directory)

        # Find and download videos (you might need to adjust this for specific websites)
        video_tags = soup.find_all("video")
        video_urls = [video["src"] for video in video_tags if "src" in video.attrs]
        download_videos(video_urls, output_directory)
    else:
        print(f"Failed to fetch the URL. Status code: {response.status_code}")


def configUpdateStuff(config):
    config.read("./config/config.ini")
    # this is the function to update the code
    x = random.randint(1, 4)
    if x == 3 and config.get("main", "checkforupdates") == "yes":
        print("You Can Disable Updating In The Config File")
    if x == 2:
        print("Join Our Discord: https://discord.gg/xrdjxyuSQt ")

    if config.get("main", "checkforupdates") == "yes":
        cfu = input("Check For Updates? [y/n]: ⤷ ")
        if "Y" in cfu or "y" in cfu:
            exec(open("./update.py").read())
        elif "N" in cfu or "n" in cfu:
            print("Ok! Ill Ask Later....")
        else:
            print("Not Sure What You Ment. Ill Ask Later")
    getNum = random.randint(1, 10)
    # asks the user if they want to enable updates
    if config.get("main", "checkforupdates") == "no":
        if getNum == 7:
            changeconfig = input("Updates Are Disabed. Wanna Renable Them? [y/n]: ⤷ ")
            # pharses it
            if "Y" in changeconfig or "y" in changeconfig:
                config.set("main", "checkforupdates", "yes")
                print("Updates Are Enabled!")
                with open("./config/config.ini", "w") as f:
                    config.write(f)
            elif "N" in changeconfig or "n" in changeconfig:
                print("Ok! Ill Ask Later....")
            else:
                print("Not Sure What You Ment. Ill Ask Later")
    if getNum == 3 and config.get("main", "showtips") == "yes":
        # this gets the random tip to display on the screen
        randomTip = random.choice(open("./config/tips.txt").readlines())
        print(randomTip)

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = "".join(random.choice(letters) for i in range(length))
    return result_str