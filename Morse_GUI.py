import tkinter as tk #GUI
import sys
import RPi.GPIO as GPIO #Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

LED = 21 #LED Output port

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Declare pin number standard
GPIO.setup(LED, GPIO.OUT) #Set pin mode

morseCodeRef = {'A': '.-',
              'B': '-...',
              'C': '-.-.',
              'D': '-..',
              'E': '.',
              'F': '..-.',
              'G': '--.',
              'H': '....',
              'I': '..',
              'J': '.---',
              'K': '-.-',
              'L': '.-..',
              'M': '--',
              'N': '-.',
              'O': '---',
              'P': '.--.',
              'Q': '--.-',
              'R': '.-.',
              'S': '...',
              'T': '-',
              'U': '..-',
              'V': '...-',
              'W': '.--',
              'X': '-..-',
              'Y': '-.--',
              'Z': '--..',
        }

#Method to convert user input to string and then to morse code and then make LED blink
def ConvertToMorse():
    morseCodeString = [] #character holder for word/string
    text = txt.get() #get input
    text = text.upper() #convert to upper case to match morseCodeRef
    for char in text:
        for i, j in morseCodeRef.items():
            if char == i:
                morseCodeString.append(j) #add char to string
    morseCodeString = ("".join(morseCodeString)) 
    morseCodeString = list(morseCodeString) #create a string list
    BlinkLEDMorse(morseCodeString) #make the LED blink the code

#Method to blink the led based on whether there is a dah or di
def BlinkLEDMorse(morseCodeString):
    for char in morseCodeString:
        if char == '-': #DAH
            GPIO.output(LED, GPIO.HIGH )
            sleep(0.6)
            GPIO.output(LED, GPIO.LOW )
            sleep(0.2)
        elif char == '.': #DI
            GPIO.output(LED, GPIO.HIGH )
            sleep(0.2)
            GPIO.output(LED, GPIO.LOW )
            sleep(0.2)

def callback(sv):
    userInput = sv.get()[0:12] #Ensures maximum characters is 12
    print("User Input: " , userInput)
    sv.set(userInput) #add character to stringVar


#GUI
window = tk.Tk()


#Instructions

greeting = tk.Label(text="Enter the word/s you want blinked:")

greeting.grid(column=2, row=0)


#User Input
sv = tk.StringVar()

sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))

txt = tk.Entry(window,width=20, textvariable=sv)

txt.grid(column=3, row=0)


#Submit Button

b = tk.Button(window, text="Submit", command=ConvertToMorse)

b.grid(column=3, row=2)


window.title("Morse Code")

window.geometry('400x100')

window.mainloop()
