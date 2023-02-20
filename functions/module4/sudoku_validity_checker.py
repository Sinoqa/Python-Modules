table = [
    ["2","9","5","7","4","3",'8','6','1'],
    ["4","3","1","8","6","5",'9','2','7'],
    ["8","7","6","1","9","2",'5','4','3'],
    ["3","8","7","4","5","9",'2','1','6'],
    ["6","1","2","3","8","7",'4','9','5'],
    ["5","4","9","2","1","6",'7','3','8'],
    ["7","6","3","5","2","4",'1','8','9'],
    ["9","2","8","6","7","1",'3','5','4'],
    ["1","5","4","9","3","8",'6','7','2']
]
is_valid = True

for row in table:
    if len(set(row)) < len(row):
        is_valid = False

columns = [] 
for col in zip(*table):
    joined_col = "".join(col)
    columns.append(joined_col) 
for col in columns:
    if len(set(col)) < len(col):
        is_valid = False

if is_valid == True:
    print("yes")
else:
    print("no")
