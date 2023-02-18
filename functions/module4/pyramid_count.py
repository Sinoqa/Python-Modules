number = int(input("number here > "))
height = 0
sum = 0
for n in range(0,number+1):
    n +=1
    sum = n + sum
    if sum <= number:
        height +=1
print("The height of the pyramid:",height)
