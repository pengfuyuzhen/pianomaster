import pygame.mixer
from time import sleep
import RPi.GPIO as GPIO
from sys import exit
import serial
from playsound import playsound

port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)

while True:
    port.write("\r\nSay something:")
    rcv = port.readline()
    port.write("\r\nYou sent:" + repr(rcv))

pygame.mixer.init(48000, -16, 1, 1024)

# do = pygame.mixer.Sound("sounds/do.wav")
# re = pygame.mixer.Sound("sounds/re.wav")
# mi = pygame.mixer.Sound("sounds/mi.wav")
# fa = pygame.mixer.Sound("sounds/fa.wav")
# sol = pygame.mixer.Sound("sounds/sol.wav")
# la = pygame.mixer.Sound("sounds/la.wav")
# si = pygame.mixer.Sound("sounds/si.wav")
# a4 = pygame.mixer.Sound("sounds/a-4.mp3")
# c4 = pygame.mixer.Sound("sounds/c-4.mp3")
# d4 = pygame.mixer.Sound("sounds/d-4.mp3")
# f4 = pygame.mixer.Sound("sounds/f-4.mp3")
# g4 = pygame.mixer.Sound("sounds/g-4.mp3")

# soundChannelA = pygame.mixer.Channel(1)
# soundChannelB = pygame.mixer.Channel(2)
# soundChannelC = pygame.mixer.Channel(3)

print "Songs Ready."

while True:
   try:
      if (rcv == "DO"):
         pygame.mixer.music.load("sounds/do.wav")
         pygame.mixer.music.play()
      if (rcv == "RE"):
         pygame.mixer.music.load("sounds/re.wav")
         pygame.mixer.music.play()
      if (rcv == "MI"):
         pygame.mixer.music.load("sounds/mi.wav")
         pygame.mixer.music.play()
      if (rcv == "FA"):
         pygame.mixer.music.load("sounds/fa.wav")
         pygame.mixer.music.play()
      if (rcv == "SO"):
         pygame.mixer.music.load("sounds/sol.wav")
         pygame.mixer.music.play()
      if (rcv == "LA"):
         pygame.mixer.music.load("sounds/la.wav")
         pygame.mixer.music.play()
      if (rcv == "TI"):
         pygame.mixer.music.load("sounds/si.wav")
         pygame.mixer.music.play()
      if (rcv == "B1"):
         pygame.mixer.music.load("sounds/c-4.mp3")
         pygame.mixer.music.play()
      if (rcv == "B2"):
         pygame.mixer.music.load("sounds/d-4.mp3")
         pygame.mixer.music.play()
      if (rcv == "B3"):
         pygame.mixer.music.load("sounds/f-4.mp3")
         pygame.mixer.music.play()
      if (rcv == "B4"):
         pygame.mixer.music.load("sounds/g-4.mp3")
         pygame.mixer.music.play()
      if (rcv == "B5"):
         pygame.mixer.music.load("sounds/a-4.mp3")
         pygame.mixer.music.play()
      sleep(.01)
   except KeyboardInterrupt:
      exit()