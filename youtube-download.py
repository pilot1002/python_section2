import pytube
import os
import subprocess

inputUrl = input("youtube URL 입력 : ")
#yt = pytube.YouTube("https://youtu.be/MhQKe-aERsU") #다운 받을 동영상 URL 지정
yt = pytube.YouTube(inputUrl)
videos = yt.streams.all()

#print('videos',videos)

for i in range(len(videos)) :
    print(i,' , ', videos[i])

cNum = int(input("다운 받을 화질 선택(0~21 입력) : "))
#cNum = 0
down_dir = "C:/workspace/youtube"
videos[cNum].download(down_dir)

newFileName = input("변환 할 mp3 파일명 입력(ex. FILENAME.mp3) : ")
oriFileName = videos[cNum].default_filename

#command 있는 명령어를 실행
subprocess.call(['ffmpeg','-i',
    os.path.join(down_dir,oriFileName),
    os.path.join(down_dir,newFileName)
])
#mp4 파일 삭제
#os.remove(oriFileName)

#수행완료
print("동영상 다운로드 및 mp3 변환 완료!")
