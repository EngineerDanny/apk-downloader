import requests
from bs4 import BeautifulSoup
from colored import fg, bg, attr


search_url = 'https://apkpure.com/search?q='

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'https://apkpure.com/',
    'Connection': 'keep-alive',
    'Cookie': '_dt_sample=0.11676142055208727; apkpure__sample=0.6108889568447815; _gid=GA1.2.1308399544.1644410253; apkpure__lang=en; __gads=ID=95d37f1c2592ef80-22d5468daccf0060:T=1644410270:RT=1644410270:S=ALNI_MaqPuhXZavpdLT3FHHPYxhMdCYm0g; AMP_TOKEN=$NOT_FOUND; _ga=GA1.2.342726199.1644410250; _ga_NT1VQC8HKJ=GS1.1.1644410249.1.1.1644415267.27; FCNEC=[["AKsRol998pISqWVDnMf0J0OkJsTnHlbQP-wpCnt5bu5QoevJHAMWyQQOoqYeQUoDswlY4Y0_XMdz7AGT0Kch8pDjGGmLMx_Z5t70SoIp6il2AV_nmY-hFT7hlF9NyQZ0y8L3QLBTl8Ckug86BRL0QBiTrlqJxX1awQ=="],null,[]]'
}

print('%s%s Hello, Welcome to APK Downloader 🙌 !!! %s' %
      (fg('white'), bg('green'), attr('reset')))
# take the package_id from the user
# package_id = input(
#     "Enter the packageId of the android app\nShould something like com.example.app\n")
# verify packageId string
response = requests.get(search_url+"farmhouse",
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
children = soup.findChildren('dl', class_='search-dl')

first_child = children[0].findChildren('dd')
print(first_child)
exit()

# retrieve the first app from the list
# get the download link
# download the app

# print("This is the content of the request " + str(content.decode()) + "\n")
