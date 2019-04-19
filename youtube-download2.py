import pytube
import os
import requests

inputUrl = input("youtube URL 입력 : ")
yt = pytube.YouTube(inputUrl)

#streams list
videos = yt.streams.all()
for i in range(len(videos)) :
    print(i,'-->', videos[i])

mp4File = yt.streams.get_by_itag(140) #mp4 tag

path = "C:/workspace/youtube"
#mp4File.download(path)

r = requests.get(inputUrl, stream=True)
with open(path, 'wb') as f:
    total_length = int(r.headers.get('content-length'))
    for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
        mp4File.download(path)
        if chunk:
            f.write(chunk)
            f.flush()
