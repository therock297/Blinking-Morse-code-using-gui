#Importing few libraries that are necassary for this task
from tkinter import* #Standard GUI library
import tkinter.font as Font #Imported font for styling the text from tkinter
import RPi.GPIO as GPIO #enables us to use the cleanup method
from gpiozero import LED #Similary this library enables use to work with LED'S
import time #For representing time in code

INPUT_SIZE = 12    #Input size limit

#Defined list of nuumbers from "0 to 9" and letters from "A to Z" in morse code 
#These are standard dot and dash set for the morse code
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
#In this case we use BCM- the GPIO number- rather than the pin number itself
GPIO.setmode(GPIO.BCM) #Basically it tells the library which pin nunbering system you are going to use.
LED = 23 #Setting the led to pin no 23 of raspberry pi
GPIO.setup(LED, GPIO.OUT) #the pin will state in logic level high or low( output voltage 3.3V or 0V).

## GUI Definitions
win = Tk() #Instantiating the window that will trigger, by calling the method tk
win.title("Morse code convertor")  #Giving the title for the window 
MyFont = Font.Font(family = 'Helvetica', size = 14, weight = 'bold') #Creating the font using the font library and then giving some parameters

##Crreating a dot function
def dot():
    GPIO.output(LED, GPIO.HIGH) #Led will remain on, but for what time?? So, the time is defined below
    time.sleep(0.5) #Will remain on for 0.5 seconds because the led is recieving voltage at 3.3V or 5V
    GPIO.output(LED, GPIO.LOW) #Led will remain off, but for what time?? So, the time is defined below
    time.sleep(0.5)  #will remain off for 0.5 seconds because the voltage provided is now 0V.

##Creating a dash function
def dash():
    GPIO.output(LED, GPIO.HIGH) #Similar explanation of this part as explained above but led will remain on and off for 3 seconds
    time.sleep(3)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(3)

##Creating a convert morse function that converts any sort of letter into dots and dashes
def CONVERT_MORSE():
    input = INPUT.get()  #Getting input 
    if input <= INPUT_SIZE and input > 0:
        for letter in input: 
            for symbol in CODE[letter.upper()]: #If letter is in upper case then, 
                if symbol == '-': #Setting the if condition in which, 
                    dash()  #we are calling the dash function as set above.
                elif symbol == '.': #Setting the elif condition in which, 
                    dot()   #we are calling the dot function as set above.
                else:
                    time.sleep(2)  #Will sleep for 2 seconds if any word doesn't contain any dot and dash
            time.sleep(2)
    else:
        print("*** ERROR *** \n -== The input size is greater than 12 or null ==-")

##Creating a close function 
def close():
    GPIO.cleanup() #this sets up the GPIO pins back to their intital settings 
    win.destroy()  # Will destory the window 

##Creating widgets
INPUT = Entry(win, font = MyFont, width = 24, bg='white') #Here I have created a entry spot in which a string will be entered by the user
INPUT.grid(row=0, column=0) #So the entry spot, will on the first spot of the window

#This button will load the morse code 
LEDBUTTON = Button(win, text = 'CONVERT', FONT = MyFont, command = CONVERT_MORSE, bg='grey', height=1, width=24) #Given the led button some parameters
LEDBUTTON.grid(row=1, column=0) #The LEDBUTTON is placed in the 1st row

#This is the exit button which will exit out of the window
exitBUTTON = Button(win, text = 'EXIT', FONT = MyFont, command = close, bg='grey', height=1, width=24) #Similarly given exit button some parameters
exitBUTTON.grid(row=2, column=0) #The EXITBUTTON is placed int he 2nd row

win.protocol("WM_DELETE_WINDOW", close)  #This command is used to close the window completely using the close function
win.mainloop()  #It will be loop forever in order to keep GUI running
