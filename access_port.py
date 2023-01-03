




import serial.tools.list_ports


ports = serial.tools.list_ports.comports()

serial_inst = ports.serial()

serial_inst.baudrate = 115200
serial_inst.port = 'COM3'
serial_inst.open()

while 1:
    if serial_inst.in_waiting:
        packet =serial_inst.readline()
        print(packet.decode('utf'))