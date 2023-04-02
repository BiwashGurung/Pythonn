data = [
    ["john", 88, 86, 76, 66, 76],
    ["sam", 77, 67, 87, 67, 56],
    ["anna", 67, 65, 67, 76, 65],
    ["ben", 87, 78, 67, 77, 57],
    ["jeff", 90, 80, 79, 88, 70]
]


arr = []


for student in data:
    
    name = student[0]
    marks = student[1:]
    
   
    total = sum(marks)
    num = len(marks)
    average = total / num
    
    
    arr.append(average)
    
   
    print(f"{name}: {average}")
    

total = sum(arr) / len(arr)


print(f"Overall average marks: {total}")
