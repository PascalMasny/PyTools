#Imports 
from pytube import YouTube
import itertools
import threading
import time
import sys
import os
import inquirer
from termcolor import colored
from pyfiglet import Figlet



link = input("Enter the link: ")
yt = YouTube(link)



#Print Info
print("Title: ", yt.title) #Title
print("Number of views: ", yt.views) #Views
print("Length of the video: ", yt.length, "sec.") #Time
print("Descripotions: ", yt.description) # Video Description
print("Ration: ", yt.rating) # Infos


#Loding Animation
done = False

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!   ')

# Audio Doenload
def audio_download():
    #just audio
    video = yt.streams.filter(only_audio=True).first()
    
    downloaded_file = video.download()
    #Loding start
    t = threading.Thread(target=animate)
    t.start()
    #download
    base, ext = os.path.splitext(downloaded_file)
    #new mp3 ending 
    new_file = base + '.mp3'
    #rename
    os.rename(downloaded_file, new_file)
    #Loding end
    time.sleep(1)
    global done
    done = True

# Video Download
def video_download():
    #video + audio 
    ys = yt.streams.get_highest_resolution()

    t = threading.Thread(target=animate)
    t.start()


    ys.download()


    time.sleep(1)
    global done
    done = True



#menue
# 
#     
questions = [
    inquirer.List(
        "main",
        message="What do you want to download your video as?",
        choices=["mp4 - Video", "mp3 - Music", "Exit"],
    ),
]
answers = inquirer.prompt(questions)










if answers == {'main': 'mp4 - Video'}:
    video_download()

elif answers == {'main': 'mp3 - Music'}:
    audio_download()

elif answers == {'main': 'Exit'}:
    exit()




#restart
restart = [
    inquirer.List(
        "restart",
        message="Do you want to restart?",
        choices=["Restart - Back to the menu", "Exit"],
    ),
]

answers2 = inquirer.prompt(restart)