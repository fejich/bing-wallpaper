import urllib.request as req
import json
import re


url = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1614319565639&pid=hp&FORM=BEHPTB&uhd=1&uhdwidth=3840&uhdheight=2160'

# try:
res = req.urlopen(url)
res = res.read().decode('utf-8')

api = json.loads(res)

api = api['images']
downloadURL = "https://bing.com" + api[0]['url']
dateTime = api[0]['enddate']
copyright = api[0]['copyright'] # 获取版权信息
rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
new_copyright = re.sub(rstr, "_", copyright)  # 替换为下划线

req.urlretrieve(downloadURL, "./Wallpaper/{0}{1}{2}.jpg".format(dateTime, '@', new_copyright))
req.urlretrieve(url, "./Wallpaper/{}.json".format(dateTime))

# except:
#     print("Error.")
