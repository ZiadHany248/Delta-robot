



import serial

ardData = serial.Serial("COM3", 115200)


while 1:
    cmd = input("Whaddya want?")
    cmd += '\r'
    ardData.write(cmd.encode())