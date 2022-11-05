from tkinter import*
import tkinter.font as Font
import RPi.GPIO as GPIO
from gpiozero import LED
import time

## Defined list of nuumbers from "0 t0 9" and letters from "A to Z" in morse code 
CODE = {'0' : '-----',
       '1' : '.----',
       '2' : '..---',
       '3' : '...--',
       '4' : '....-',
       '5' : '.....',
       '6' : '-....',
       '7' : '--...',
       '8' : '---..',
       '9' : '----.',
       'A' : '.-',
       'B' : '-...',
       'C' : '-.-.',
       'D' : '-..',
       'E' : '.',
       'F' : '..-.',
       'G' : '--.',
       'H' : '....',
       'I' : '..',
       'J' : '.---',
       'K' : '-.-',
       'L' : '.-..',
       'M' : '--',
       'N' : '-.',
       'O' : '---',
       'P' : '.--.',
       'Q' : '--.-',
       'R' : '.-.',
       'S' : '...',
       'T' : '-',
       'U' : '..-',
       'V' : '...-',
       'W' : '.--',
       'X' : '-..-',
       'Y' : '-.--',
       'Z' : '--..', }

## Using "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)
LED = 23
GPIO.setup(LED, GPIO.OUT)

## GUI Definitions
win = Tk()
win.title("Morse code convertor")
myFont = FONT.Font(family = 'Helvetica', size = 14, weight = 'bold')

##Crreating a dot function
def dot():
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(0.5)

##Creating a dash function
def dash():
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(3)

##Creating a convert morse function
def CONVERT_MORSE():
    input = INPUT.get()
    for letter in input:
        for symbol in CODE[letter.upper()]:
            if symbol == '-':
                dash()
            elif symbol == '.':
                dot()
            else:
                time.sleep(2)
        time.sleep(2)

##Creating a close function
def close():
    GPIO.cleanup()
    win.destroy()

##Creating widgets
INPUT = Entry(win, font = myFont, width = 24, bg='white')
INPUT.grid(row=0, column=0)

LEDBUTTON = Button(win, text = 'CONVERT', FONT = MyFont, command = CONVERT_MORSE, bg='grey', height=1, width=24)
LEDBUTTON.grid(row=1, column=0)

exitBUTTON = Button(win, text = 'EXIT', FONT = MyFont, command = CLOSE, bg='grey', height=1, width=24)
exitBUTTON.grid(row=2, column=0)

win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()


             


