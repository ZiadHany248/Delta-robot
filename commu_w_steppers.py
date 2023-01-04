import serial
import inv_no_input
import numpy as np

# setting up
steps_per_deg = 50
totalStepsM1 = 0
totalStepsM2 = 0
totalStepsM3 = 0
oldTotalStepsM1 = 0
oldTotalStepsM2 = 0
oldTotalStepsM3 = 0


ser = serial.Serial()
ser.port = "COM4"
ser.baudrate = 115200
ser.open()
while 1:
    stri = input("Enter three coords")
    str_list = stri.split(',')

    x_coord = str_list[0]
    y_coord = str_list[1]
    z_coord = str_list[2]
 
    theta11, theta12, theta13, theta21, theta22, theta23 = inv_no_input.inv(x_coord, y_coord, z_coord)
    arr = np.array([[theta11, theta12, theta13, theta21, theta22, theta23]])
    arr *= steps_per_deg

    currentTotalStepsM1 = arr[0][0] 
    currentTotalStepsM2 = arr[0][1]
    currentTotalStepsM3 = arr[0][2]
    #####
    #Further Serializaion to add direction input for each motor
    #####

    serialized_string = str(arr[0][0]) + ';' + str(arr[0][1]) + ';' + str(arr[0][2]) + '\r'


    serialized_string_coords = str(x_coord) + ';' + str(y_coord) + ';' + str(z_coord) + '\r'

    serialized_string_coords = serialized_string_coords.encode()
    ser.write(serialized_string_coords)

    oldTotalStepsM1 = currentTotalStepsM1
    oldTotalStepsM2 = currentTotalStepsM2
    oldTotalStepsM3 = currentTotalStepsM3