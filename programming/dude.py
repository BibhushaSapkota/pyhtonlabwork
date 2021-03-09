# you live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each of the 10 stops on the way.
# how long will the bus journey take ? Alternatively, you could run to univerity . You jog the first mile at 7mph;
# then run the next two at 15mph; before jogging the last at 7mph again. Will this be quicker or slower than the bus ?
living_miles_apart= 4
drives_velocity=25
time_taken_by_bus =(living_miles_apart/drives_velocity)*60
time_spent_in_bus_stop=10*2
total_time_taken_by_bus=time_taken_by_bus+time_spent_in_bus_stop
time_taken_by_jogging=(1/7)*60+(2/15)*60+(1/7)*60
print("the total time taken by bus is",total_time_taken_by_bus)
print ("the total time taken by jogging is",time_taken_by_jogging)
if total_time_taken_by_bus < time_taken_by_jogging:
    print("taking bus is quicker")
else:
    print("jogging is quicker")

