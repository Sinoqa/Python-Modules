hatList = [1, 2, 3, 4, 5]
#step 1
user_intiger= int(input("> "))
middle = int((len(hatList)+1) / 2 )
m = hatList.index(middle)
hatList.insert(m ,user_intiger)
hatList.remove(middle)
#step 2
hatList.pop()


#step 3
print(len(hatList))

#pabida step
print(hatList)

---end(test)
a


---start
hatList = [1, 2, 3, 4, 5]
user_intiger= int(input("> "))
hatList.insert(2 ,user_intiger)
hatList.remove(3)


hatList.pop()


print(len(hatList))
