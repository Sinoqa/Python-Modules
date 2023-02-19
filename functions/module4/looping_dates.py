#Get the date from user
date = input("birthdate here > ")
the_sum = 0
#loop through the numbers
while the_sum not in range(1,10):
    for number in date:
        num = int(number)
        the_sum += num

    if the_sum > 10:
        sum1 = the_sum
        iterable_number = str(the_sum)
        for number in iterable_number:
            num = int(number)
            the_sum += num
        the_sum -= sum1
    print(the_sum)
