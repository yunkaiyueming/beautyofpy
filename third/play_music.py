# coding=utf8

import mp3play

path = 'zao.mp3'


clip = mp3play.load(path)
clip.play()
try:
	while True:  # dead at here for playing mp3 file, you can press "CTRL+C" to exit
		pass
except KeyboardInterrupt:
	clip.stop()