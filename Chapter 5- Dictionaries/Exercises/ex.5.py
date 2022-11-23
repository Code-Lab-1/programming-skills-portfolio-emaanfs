

#person name1
data={"first_name":"erica","last_name":"john","age":"24","city":"melbourne"}
print(data["first_name"])
print(data["last_name"])
print(data["age"])
print(data["city"])


#glossary2
glossary={"else":"Else statements are used to do something else when the condition in the if statement isn't true","algorithm":"set of instructions to solve a problem","loop":"loops check condition and run code block","script":"set of steps to write a statement","variable":"stores value"}
for i in glossary:
    print(i , ":\n" + glossary[i])

#glossary 3 
python_dictonary={"else":"Else statements are used to do something else when the condition in the if statement isn't true",
"algorithm":"set of instructions to solve a problem",
"loop":"loops check condition and run code block",
"script":"set of steps to write a statement",
"variable":"stores value"}
python_dictonary.update({"Arrays":"Arrays are containers that hold",
"Argument":"An argument is a way to provide more information to a function.",
"Functions":"A function is a block of code that can be referenced by name to run the code it contains.",
"While loops":"While loops are set up just like if statements.",
"Conditional statements":"Conditional statements evaluate to true or false."})
for i in python_dictonary:
    print(i, ":" + python_dictonary[i]) 

#glossary 4
river={"nile":"egypt","lena":"russia","Purus":"brazil"}    
for i in river:
    print(i, "run through" , river[i])
for i in river.keys():
    print(i)
for i in river.values():
    print(i)        

#glossary 5
pets=[]
pet = {"animal type":"Amphibians",
"name":"kanye",
"owner":"pj",
"color":"brown"} 
pets.append(pet)
pet = {"animal type":"Reptiles",
"name":"mark",
"owner":"johnny",
"color":"white"} 
pets.append(pet)
pet={"animal type":"Mammals",
"name":"chris",
"owner":"erica",
"color":"black"} 
pets.append(pet)
for pet in pets:
    print("info of the pets ,", pet["name"],":")
    for key, value in pet.items():
        print(f"\t{key}:{value}")