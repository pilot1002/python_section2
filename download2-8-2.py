from bs4 import BeautifulSoup
import sys
import io
import urllib.request as req
import urllib.parse as rep
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

base = "https://www.inflearn.com/"
quote = rep.quote_plus("")

url = base + quote

res = req.urlopen(url)
savePath = "C:/workspace/imagedown/"

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errono.EEXIST:
        print("폴더 만들기 실패!")
        raise

soup = BeautifulSoup(res,"html.parser")

img_list = soup.select("ul.slides")[0]
img_text = soup.select_one("div.block.courseitem > a").string()

for i, e in enumerate(img_list,1):
    #with open(savePath+"text_"+str(i)+".txt","wt") as f:
    #    f.write(e.select_one("h4.block_title > a").string)
    fullFileName = os.path.join(savePath, savePath+img_text+'.png')
    req.urlretrieve(e.select_one("div.block.courseitem#297519 > a > img")['src'],fullFileName)

print("다운로드 완료")
