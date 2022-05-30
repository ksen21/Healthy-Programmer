
from pygame import mixer
from datetime import datetime
from time import time

def musicOnLoop(song,stopper):
    mixer.init()
    mixer.music.load(song)
    mixer.music.play()

    while True:
        a = input()

        if a == stopper:
            mixer.music.stop()
        break

def Value(message):
    with open("myValues.txt",'a') as f:
        f.write(f'{message} {datetime.now()}\n ')



if __name__ == '__main__':

    water=time()
    eyes=time()
    excercise=time()

    secOfWater=30
    secOfEyes=20
    secOfExcercise=30

    while True:
        if time()-water>secOfWater:
           print("Water Drinking time ! Enter 's' to stop alarm")
           musicOnLoop('WG.mp3','s')
           water=time()
           Value('Drank at')

        if time()-eyes>secOfEyes:
           print("Eyes Excercise time ! Enter 'done' to stop alarm")
           musicOnLoop('eyes.mp3','done')
           eyes=time()
           Value('Eyes Excercise at')

        if time() -excercise > secOfExcercise:
            print("Physical Activity time ! Enter 'done' to stop alarm")
            musicOnLoop('physical.mp3', 'done')
            excercise = time()
            Value('Physical Activity at')













