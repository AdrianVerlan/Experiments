import pygame
import datetime

alarm_h = int(input("Write alarm hour: "))
alarm_m = int(input("Write alarm minutes: "))

pygame.mixer.init()
pygame.mixer.music.load("testare_alarma.mp3")

while True:

    current_time = datetime.datetime.now()
    current_hour = current_time.hour
    current_minute = current_time.minute
    minutes_left = alarm_m - current_minute
    seconds_left = 60 - current_time.second
    if seconds_left == 60:
        seconds_left= 0
        minutes_left +=1
    if minutes_left <0:
        minutes_left += 60
    print(f"Time to alarm : {minutes_left:02d}:{seconds_left:02d}")

    if current_hour== alarm_h and current_minute == alarm_m:
        print()
        print("It's time to wake up!!!")
        pygame.mixer.music.play()
        pygame.time.delay(10000)
        pygame.mixer.music.stop()
        break