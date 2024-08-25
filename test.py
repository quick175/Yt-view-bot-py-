def timeToSeconds(originalTime):
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
						originalTime = minutes + seconds
						return originalTime