import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "http://blogfiles.naver.net/20120808_257/aaugh33_1344410923803jfnxF_PNG/%BB%FD%B0%A2%B8%B9%C0%BA%B0%ED%BE%E7%C0%CC2.png"
htmlURL = "http://google.com"

savePath1 = "C:/workspace/Section2/test1.png"
savePath2 = "C:/workspace/Section2/cat.html"

dw.urlretrieve(imgUrl,savePath1)
dw.urlretrieve(htmlURL,savePath2)

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlURL).read()

saveFile1 = open(savePath1,'wb')
saveFile1.write(f)
saveFile1.close()

with open(savePath2,'wb') as saveFile2:
    saveFile2.write(f2)

print("다운로드 완료!")
