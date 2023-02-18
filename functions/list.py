#step 1 
beatles = []
print("step 1 ", beatles)
#step 2 
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("step 2 ", beatles)

#step 3 
for members in("Stu Sutcliffe","Pete Best"):
    beatles.append(members)
print("step 3 ", beatles)

#step 4
index1 = beatles.index("Stu Sutcliffe")
del beatles[index1]
index2 = beatles.index("Pete Best")
del beatles[index2]
print("step 4 ", beatles)

#step 5
beatles.insert(0, "Ringo Starr")
print("step 5 ", beatles)

#testing list length 
print("The Fab", len(beatles))
