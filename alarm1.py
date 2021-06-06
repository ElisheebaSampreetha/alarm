# -*- coding: utf-8 -*-
"""
Created on Mon May 31 22:10:50 2021

@author: india
"""

import datetime
import winsound

alarmHour=int(input(" enter the hour you want to wake up:"))
alarmMint=int(input(" enter the minute you want to wake up:"))
amPm=str(input("am or Pm:"))
if(amPm == "pm"):
    alarmHour = alarmHour + 12
while( 1 == 1):
    if(alarmHour == datetime.datetime.now().hour and alarmMint == datetime.datetime.now().minute):
        print("wake up")
        winsound.PlaySound("sound.wav",winsound.SND_NOSTOP)
        break
