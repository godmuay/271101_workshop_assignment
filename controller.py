import pyfirmata

# comport='COM7'

def acomport(x):
    comport = 'COM'+x
    return comport
# board=pyfirmata.Arduino(comport)


# board=pyfirmata.Arduino(comport)  
# led_1=board.get_pin('d:13:o') #Set pin to output
# led_2=board.get_pin('d:12:o')
# led_3=board.get_pin('d:11:o')
# led_4=board.get_pin('d:10:o')
# led_5=board.get_pin('d:9:o')

def led(total,led_1,led_2,led_3,led_4,led_5,fingers):#creat condition to controll digital out put 

    if fingers[0]==1:
        led_1.write(1)
    else:
        led_1.write(0)

    if fingers[1]==1:
        led_2.write(1)
    else:
        led_2.write(0)
      
    if fingers[2]==1:
        led_3.write(1)
    else:
        led_3.write(0)
       
    if fingers[3]==1:
        led_4.write(1)
    else:
        led_4.write(0)
        
    if fingers[4]==1:
        led_5.write(1)
    else:
        led_5.write(0)


