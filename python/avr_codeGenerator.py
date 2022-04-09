# AVR C-Code Generator

import os


def PORTA(direction):
    f = open("PORTA.c", "w+")
    f.write(
        "#include <avr/io.h>\n\nvoid DIO_set_PORTA_dir(void)\n{\nDDRA = 0b{};\n}")
    f.close()
    f = open("PORTA.h", "w+")
    f.write("DIO_set_PORTA_dir(void);")
    f.close()


def PORTB(direction):
    f = open("PORTB.c", "w+")
    f.write(
        "#include <avr/io.h>\n\nvoid DIO_set_PORTB_dir(void)\n{\nDDRB = 0b{};\n}")
    f.close()
    f = open("PORTB.h", "w+")
    f.write("DIO_set_PORTB_dir(void);")
    f.close()


def PORTC(direction):
    f = open("PORTC.c", "w+")
    f.write(
        "#include <avr/io.h>\n\nvoid DIO_set_PORTC_dir(void)\n{\nDDRC = 0b{};\n}")
    f.close()
    f = open("PORTC.h", "w+")
    f.write("DIO_set_PORTC_dir(void);")
    f.close()


def PORTD(direction):
    f = open("PORTD.c", "w+")
    f.write(
        "#include <avr/io.h>\n\nvoid DIO_set_PORTD_dir(void)\n{\nDDRD = 0b{};\n}")
    f.close()
    f = open("PORTD.h", "w+")
    f.write("DIO_set_PORTD_dir(void);")
    f.close()


done = 0

while (1):
    print("Please Enter the letter for the port to set it's direction : ")
    port = input()
    port_dir = [0, 0, 0, 0, 0, 0, 0, 0]
    i = 0

    if 'A' or 'a' in port:
        for i in range(0, 8):
            # while (0 == done):
            print("Select pin ({}) direction: (in/out)\n".format(i))
            status = input()
            if 'in' in status:
                port_dir[i] = 0
                #done = 1
            elif 'out' in status:
                port_dir[i] = 1
                #done = 1
            else:
                print("Sorry, Wrong choice!!!")

            ++i

        PORTA(port_dir[:8])

    elif 'B' or 'b' in port:
        for i in range(0, 8):
            # while (0 == done):
            print("Select pin ({}) direction: (in/out)\n".format(i))
            status = input()
            if 'in' in status:
                port_dir[i] = 0
                #done = 1
            elif 'out' in status:
                port_dir[i] = 1
                #done = 1
            else:
                print("Sorry, Wrong choice!!!")

            ++i

        PORTB(port_dir[:8])

    elif 'C' or 'c' in port:
        for i in range(0, 8):
            # while (0 == done):
            print("Select pin ({}) direction: (in/out)\n".format(i))
            status = input()
            if 'in' in status:
                port_dir[i] = 0
                #done = 1
            elif 'out' in status:
                port_dir[i] = 1
                #done = 1
            else:
                print("Sorry, Wrong choice!!!")

            ++i

        PORTC(port_dir[:8])

    elif 'D' or 'd' in port:
        for i in range(0, 8):
            # while (0 == done):
            print("Select pin ({}) direction: (in/out)\n".format(i))
            status = input()
            if 'in' in status:
                port_dir[i] = 0
                #done = 1
            elif 'out' in status:
                port_dir[i] = 1
                #done = 1
            else:
                print("Sorry, Wrong choice!!!")

            ++i

        PORTD(port_dir[:8])

    print("Continue ? (y/n)")
    c = input()
    if 'n' in c:
        break
