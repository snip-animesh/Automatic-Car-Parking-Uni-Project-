import main
# import dataGenerator
from pyfirmata import Arduino, util, STRING_DATA, pyfirmata
import  keyboard
import time

port = 'COM3'

board = Arduino(port)

servo_pin = 6
board.digital[servo_pin].mode = pyfirmata.SERVO

rgbR = board.get_pin('d:11:o')
rgbG = board.get_pin('d:12:o')
rgbB = board.get_pin('d:13:o')

buzzer = board.get_pin('d:4:o')


def lcd(firstLine, secondLine):
    board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(firstLine))
    board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(secondLine))
    print("Display updated")
    time.sleep(.5)


def servo(angle):
    board.digital[servo_pin].write(angle)


def rgb(RGB):
    rgbR.write(RGB[0])
    rgbG.write(RGB[1])
    rgbB.write(RGB[2])


def buzzers(val):
    buzzer.write(val)


servo(110)
time.sleep(1)

while True:
    parks = main.run()
    entry = parks[0]
    outro = parks[1]
    parkings = parks[2:]
    buzzers(0)
    # Counting available solts
    available_slots = ""
    for i in range(0, len(parkings)):
        if parkings[i] == 0:
            available_slots = available_slots + " " + str(i + 1)
    print(available_slots)
    # lcd("Available Slots", available_slots)

    # If any car at entry , then displaying at lcd and opening gate or ramaining it closed.

    if entry == 1 and parkings.count(0) > 0 and outro == 0:  # car in entry and slots available
        servo(0)
        lcd("Available Slots", available_slots)

        rgb([0, 1, 0])


    elif entry == 0 and parkings.count(0) > 0 and outro == 0:  # No car in entry and slots available
        servo(110)
        lcd("Available Slots", available_slots)

        rgb([0, 1, 0])

    elif parkings.count(0) == 0 and outro == 0:  # No slots available
        servo(110)
        lcd("    NO SLOTS", "    AVAILABLE")

        rgb([1, 0, 0])
    if parkings.count(0) == 0 and entry == 1:  # No slots available and car in entry
        buzzers(1)
        print("buzzers")

    if outro == 1:
        servo(0)
        rgb([0, 0, 1])
        time.sleep(.1)

    print("Iteration Done")

    if keyboard.is_pressed ("space"):
        break

servo(110)
rgb([0,0,0])
buzzers(0)
lcd("","")
