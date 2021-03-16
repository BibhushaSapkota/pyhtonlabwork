#write a python program to convert seconds to day,hour,minutes and seconds
seconds=int(input("enter the seconds"))
days=(((seconds//60)//60)//24)
hour=((seconds//60)//60)
minutes=(seconds)//60

print("its",days,"days",hour,"hour",minutes,"minutes")