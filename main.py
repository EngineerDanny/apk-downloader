"""
APK DOWNLOADER
Author  :   Daniel Agyapong
Website :   https://engineerdanny.me
Date    :   February, 2022
"""

import sys
import requests
from bs4 import BeautifulSoup
from colored import fg, bg, attr
import re

base_url = 'https://apksfull.com'
version_url = 'https://apksfull.com/version/'
search_url = 'https://apksfull.com/search/'
dl_url = 'https://apksfull.com/dl/'
g_play_url = 'https://play.google.com/store/apps/details?id='

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Connection': 'keep-alive',
}


def show_internet_error():
    print(fg('red') + '\n[!] ERROR: ' + attr('reset') +
          'Check your internet connection and try again.\n')
    exit()


def show_arg_error():
    print(fg('red') + '\n[!] ERROR: ' + attr('reset') +
          'Invalid Format\nShould be of the format `python main.py {{PACKAGE_ID}}`')
    exit()


def show_invalid_id_err():
    print('%s%s PackageId is invalid %s' %
          (fg('white'), bg('red'), attr('reset')))
    exit()


def main():
    # Get the argument from the command line
    if len(sys.argv) != 2:
        show_arg_error()

    print('%s%s Hello, Welcome to APK Downloader 🙌 !!! %s' %
          (fg('white'), bg('green'), attr('reset')))

    # take the package_id from the user
    package_id = sys.argv[1]

    # verify g_play_url with packageId string
    g_play_res = requests.get(g_play_url + package_id,
                              headers=headers, allow_redirects=True)
    if(g_play_res.status_code != 200):
        show_invalid_id_err()

    # search the web page using the package id
    search_res = requests.get(search_url + package_id,
                              headers=headers, allow_redirects=True)

    # check the statuscode and verify it
    if search_res.status_code != 200:
        show_internet_error()

    # there will be a list of apps that show on the website
    soup = BeautifulSoup(search_res.content, 'html.parser')

    # # find the first class with the class name "search-dl"
    # children = soup.findChildren('a', class_='col col-6 list')

    # # get href of the first child
    # first_child = children[0]
    # app_href = first_child.get('href')

    # # get the name of the child
    # app_name = first_child.find('strong').text

    # # hyphenate and format the app name into lowercase
    # app_name_formatted = app_name.replace(" ", "-").lower()
    # app_url = version_url + app_href

    # # get string after the last '/'
    # app_id = app_href.rsplit('/', 1)[1]

    # app_response = requests.get(version_url + app_id,
    #                             headers=headers, allow_redirects=True)

    # if app_response.status_code != 200:
    #     show_internet_error()

    tbody_children = soup.findAll('a')

    sub_dl_links = []

    # tbody_children
    # loop through the children and get the href
    for item in tbody_children:
        # get href of the child
        link = item.get('href')
        # if link contains "downwload"
        if link.find("/download/") != -1:
            # append the link to the list
            sub_dl_links.append(base_url+link)

    # establish a connection to the first link
    sub_dl_res = requests.get(sub_dl_links[0],
                              headers=headers, allow_redirects=True)
    if sub_dl_res.status_code != 200:
        show_internet_error()

    # locate the script, get the contents
    script_text = BeautifulSoup(
        sub_dl_res.content, 'html.parser').findAll("script")

    # find the last but one script tag
    last_script = script_text[-2].contents[0]

    # query the token from the script
    token = re.findall("token','([^\']+)", last_script)[0]

    # make a request to the download link
    dl_res = requests.post(dl_url, data={'token': token}, headers=headers)
    if dl_res.status_code != 200:
        show_internet_error()
    dl_res_json = dl_res.json()
    # get the download_link from the json response
    download_link = dl_res_json['download_link']

    # download the apk
    print("Downloading APK")
    exit()
    r = requests.get(download_link, allow_redirects=True)
    with open(app_name_formatted+'.apk', 'wb') as f:
        f.write(r.content)
    print("APK Downloaded")

    exit()


main()
