#Imports 
from pytube import YouTube
import itertools
import threading
import time
import sys


link = input("Enter the link: ")
yt = YouTube(link)


#Print Info
print("Title: ", yt.title) #Title
print("Number of views: ", yt.views) #Views
print("Length of the video: ", yt.length, "sec.") #Time
print("Descripotions: ", yt.description) # Video Description
print("Ration: ", yt.rating) # Infos

ys = yt.streams.get_highest_resolution()
# ys = yt.streams.get_audio_only()


done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!\n ')

t = threading.Thread(target=animate)
t.start()


ys.download()


time.sleep(1)
done = True




