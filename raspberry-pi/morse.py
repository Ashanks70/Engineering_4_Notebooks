#type:ignore
import board
import time 
import digitalio
MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'}
led=digitalio.DigitalInOut(board.GP12)
led.direction=digitalio.Direction.OUTPUT
def translate(letter, led):
    order=letter.split(",")
    for i in order:
        if i==".":
            print("short")
            led.value=True
            time.sleep(.25)
        if i=="-":
            print(long)
            led.value=False
            time.sleep(.75)
        led.value=False
        time.sleep(.25)
    time.sleep(.5)

while True:
#        try:
    word=input("type word: ")

    for letter in word:
        if letter==" ":
            print(" ")
            time.sleep(1.75)
        if letter != " ":
            l=str.upper(letter)
            l=MORSE_CODE[l]
            print(l)
            str(l)
            translate(l,led)
        
#        except:
#            print("error, please try again")