#N students take K apples and distribute them among each other evenly.
# The remaining (the undivisible )part remains in the basket.how many apples will each single student get ?
# how manny apples will remain in rhe basket? the program reads the number N and K it should print two answers for the questiones above.
k=int(input("the number of apples"))
n=int(input("the number of students"))
apples= k//n
remaining_apples=k%n
print("single student will get", apples)
print("remaining apples in basket", remaining_apples)

