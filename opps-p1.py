class F15:
    def __init__(kesava,start_time,end_time):
        kesava.start_time=start_time
        kesava.end_time=end_time
        print("the object is created for the class F15")
    def Lights(kesava,color):
        kesava.color=color
        print(kesava.color," color Light is on")
    def Fan(kesava,speed):
        kesava.speed=speed
        print("the fan speed is:",kesava.speed)
    def Ac(kesava,roomtemp,outsidetemp):
        kesava.roomtemp=roomtemp
        kesava.outsidetemp=outsidetemp
        print("the room temperature is:",roomtemp)
        print("the out side temperature is:",outsidetemp)
    def display(kesava):
        print("the difference is:",kesava.outsidetemp-kesava.roomtemp)
        print("the fan speed is:",kesava.speed)
        print("the class starts from "+kesava.start_time+" and ends at "+kesava.end_time)
kesava=F15("9:00","4:00")
kesava.Lights("green")
kesava.Fan(5)
kesava.Ac(18,32)
kesava.display()
