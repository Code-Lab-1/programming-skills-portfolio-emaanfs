

#Names1
names=["erica","john","aaron","oliver","hazel",]
print(names[0])
print(names[3])
print(names[2])
print(names[1])
print(names[4])


#greetings2
for i in names:
    print("welcome", i)


#your own list3
transportation=["car","bike","bicycle","train","bus"]
for i in transportation:
    print("i would like to own",i)


#guest list4
guest_list=["erica","john","pj","mathew"]
for i in guest_list:
    print("dear",i,"id like to invite you for a dinner at rove at down town dubai")


#change guest list5
guest_list.insert(0,"chris")
print(guest_list)
guest_list.remove("erica")
print(guest_list)
for i in guest_list:
    print("dear",i,"id like to invite you for a dinner at rove at down town dubai")



#shrinking guest list6   
names =["chris", "john", "erica"]
print("sorry, i can only invite two persons for the dinner")
print(names.pop(), "im sorry. let's meet next time")
for i in names:
    print(i , "you're invited for dinner at rove")
for i in names:
    del names[0]
print(names)    
print("number of guests coming for the dinner at rove", names)



#seeing the world
location = ["venice", "japan", "france", "egypt", "finland"]
print(location)
#sorted function
print(sorted(location))
print(location)
#sorted reverse function
print(sorted(location, reverse = True))
print(location)
#reverse function
location.reverse()
print(location)
#reverse function 
location.reverse()
print(location)
#reverse function
location.reverse()
print(location)
#sort function
location.sort()
print(location)
#sort function in reverse
location.sort(reverse=True)
print(location)



