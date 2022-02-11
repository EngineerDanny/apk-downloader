import requests
from bs4 import BeautifulSoup
from colored import fg, bg, attr
from requests_html import HTMLSession
import re
import json

base_url = 'https://apksfull.com'
version_url = 'https://apksfull.com/version/'
search_url = 'https://apksfull.com/search/'

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'https://apksfull.com/',
    'Connection': 'keep-alive',

}

print('%s%s Hello, Welcome to APK Downloader 🙌 !!! %s' %
      (fg('white'), bg('green'), attr('reset')))
# take the package_id from the user
# package_id = input(
#     "Enter the packageId of the android app\nShould something like com.example.app\n")

# verify packageId string

# establish a session
# session = HTMLSession()

# connect to needed webpage
# resp = session.get(search_url+"farmhouse")


response = requests.get(search_url + "com.farmhouse.app",
                        headers=headers, allow_redirects=True)
statusCode = response.status_code
content = response.content

# check the statuscode and verify if the packageId is valid
if statusCode == 200:
    print("PackageId is valid")
else:
    print("PackageId is invalid")
    exit()


# there will be a list of apps that show on the website
soup = BeautifulSoup(content, 'html.parser')

# find the first class with the class name "search-dl"
children = soup.findChildren('a', class_='col col-6 list')

first_child = children[0]
# get href of the first child
app_href = first_child.get('href')
print(app_href)

# get the name of the child
app_name = first_child.find('strong').text
print(app_name)

# hyphenate and format the app name into lowercase
app_name_formatted = app_name.replace(" ", "-").lower()
app_url = version_url + app_href

# get string after the last '/'
app_id = app_href.rsplit('/', 1)[1]


app_response = requests.get(version_url + app_id,
                            headers=headers, allow_redirects=True)

if app_response.status_code == 200:

    app_soup = BeautifulSoup(app_response.content, 'html.parser')

    tbody_children = app_soup.findAll('a')

    links = []

    # tbody_children
    # loop through the children and get the href
    for item in tbody_children:
        # get href of the child
        link = item.get('href')
        # if link contains "downwload"
        if link.find("/download/") != -1:
            # append the link to the list
            links.append(base_url+link)

    # establish a session
    session = HTMLSession()
    # connect to needed webpage
    download_response = session.get(links[0],
                                    headers=headers, allow_redirects=True)

    # tbody_href = tbody_first_child.get('class')
    download_link = BeautifulSoup(download_response.content, 'html.parser')

    # locate the script, get the contents
    script_text = download_link.findAll("script")

    token = "Z1NjU091TVdGdkVZZWNXeStDaGgvL1RXbVBKeUo1OVk2Ti9ySCtyY2JvVjA1SlF0Nzd5VlpHcGc4aGhrU05KKzBYc0VkUzZsZE5XSGNoaU5JUlpQYnVCRU5NY29qUGxKbDkvbkZJZHFDQ2pqdndtVDJVaFdqUGtocXBuQmtabWsxd1JhaVYxZlZiM0o0UEFVZVdGbkc2QURJMVdkWXEzbXdFeG9ObTJqM01zdWt2RnRlNUVIb1B6Uk9KNll6eHkzSU55UGc5eWRiZktHSFppVng0MFJpZz09"

    length = len(token)

    # find the last script tag
    last_script = script_text[-2].contents[0]

    tokens = []

    # check if the token is present for all the words in splitted
    for word in last_script.split():
        if(len(word) >= 288):
            tokens.append(word)

    # get javascript object inside the script
    # result = re.search(r'^[0-9a-fA-F]{32}$', s)
    model_data = re.findall("token','([^\']+)", last_script)[0]
    
    print(model_data) 
# get href of the first child
# app_href = first_child.get('href')

# "(?m)^(?=\s*([a-z]{4,}\s*)*$).*"g
exit()

# retrieve the first app from the list
# get the download link
# download the app

# print("This is the content of the request " + str(content.decode()) + "\n")
