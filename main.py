import os, webbrowser, time
from test import *

killChromeCMD = "taskkill /f /im opera.exe"
def browserManage(link):
	i = 0
	while i < 2:
		webbrowser.open_new(link)
		x = open("durationfile.txt", "r")
		for y in x:
			timeToSeconds(y)
			time.sleep(int(y))
			os.system(f'cmd /c {killChromeCMD}')
		i += 1

files = {
	"file1" : "durationfile.exe",
	"file2" : ""
}

urls=["https://youtube.com/shorts/KD1xMzlMqko?feature=share","https://youtube.com/shorts/pL82bDBE2gY"]
def urlSetter(listofURLs):
	i=0
	while i < len(listofURLs):
		currentURL = listofURLs[i]
		cmd2=f"yt-dlp.exe --skip-download --get-duration {currentURL} > durationfile.txt"
		os.system(f"cmd /c {cmd2}")
		browserManage(listofURLs[i])
		i += 1
	return currentURL

urlSetter(urls)
input("if you press enter  ")
"""def timeToSeconds(originalTime):
	i = 0
	with open("durationfile.txt") as myTime:
		for line in myTime.readline():
			for character in line:
				while i < len(line):
					if line[i] == "\\" and line[i+1] == "n":
						break
					if line[i] != ":":  # means no colons, means just seconds
						i += 1
						if i == len(line) -1:
							seconds = line.strip()
							originalTime = int(seconds)
							return originalTime
					else:
						minutes, seconds = line.strip().split(":")
						minutes = int(minutes)
						minutes *= 60
						orginalTime = minutes + seconds
						return orginalTime"""