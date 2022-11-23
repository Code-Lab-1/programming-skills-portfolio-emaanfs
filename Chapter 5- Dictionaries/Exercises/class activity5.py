
#class activity 1
fruit=["apple","banana","orange","berries"]
for list in fruit:
    print("the following lines will print each letter", list)
    for letters in list:
        print(letters)

#class activity 2
student={"name":"emaan fatima","age":"20","course":"cc","gender":"F","nationality":"pakistani"}
print(student)
student["name"]="fatima"
print(student)

#class activity 3
student={"name":"emaan fatima","age":"20","course":"cc","gender":"F","nationality":"pakistani"}
print(student.keys())
student.pop("course")
print(student["age"])
del student["age"]
print(student)

#class activity 4
student={"name":"emaan fatima","age":"20","course":"cc","gender":"F","nationality":"pakistani"}
student.update({"email":"emanfs@gmail.com"})
student.update({"blood group":"B+"})
print(student)

#class activity 5
student={"name":"emaan fatima","age":"20","course":"cc","gender":"F","nationality":"pakistani"}
student["age"]="30"
print(student)
student.popitem()
print(student)
if "name" in student:
    print("name is present")
else:
    print("name is not in the dictionary") 

