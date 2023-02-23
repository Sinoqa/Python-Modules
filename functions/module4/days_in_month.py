def isYearLeap(year):
    if year < 1582:
        return False
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

days_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
def daysInMonth(year, month):
    year_check = isYearLeap(year)
    if year_check == True:
        days_month[2] = 29
    else:
        days_month[2] = 28
    return days_month[month]

    


testYears = [1900, 2000, 2016, 1987]
testMonths = [2,2,1,11]
testResults = [28,29,31,30]
for i in range (len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    print(yr, mo, "=>", end="")
    result = daysInMonth(yr,mo)
    if result == testResults[i]:
        print("ok")
    else:
        print("failed")
