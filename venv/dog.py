#given the integer N-the number of minutes that is passed since the midnight- how many hours and minutes are displayed
#on the 24th digital clock ?
n=int(input('enter the minutes passed since midnight'))
hours= (n//60)
minutes= (n%60)
print("the hours is ",hours)
print("the minutes is",minutes)
print(f'its {hours}:{minutes}now')

