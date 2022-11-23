
#class activity 1
fruit=["apple","banana","orange","berries"]
for list in fruit:
    print("the following lines will print each letter", list)
    for letters in list:
        print(letters)

#class activity 
student={"name":"emaan fatima","age":"20","course":"cc","gender":"F","nationality":"pakistani"}
print(student)
student["name"]="fatima"
print(student)
print(student["age"])
print(student.keys())
del student["age"]
print(student)
student.pop("course")
print(student)
student.update({"email":"emanfs@gmail.com"})
student.update({"blood group":"B+"})
print(student)
if "name" in student:
    print("name is present")
else:
    print("name is not in the dictionary")    

if not "name" in student:
    print("student name")
else:
    print("name not there")    
student["age"]="30"
print(student)
student.popitem()
print(student)
        