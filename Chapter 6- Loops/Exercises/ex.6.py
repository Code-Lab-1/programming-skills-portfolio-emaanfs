

#pizza toppings
prompt="what toppings would you like on your pizza"

while True:
    toppings=input(prompt)
    if toppings !="quit":
        print(" i'll add {toppings} to your pizza.")
    else:
        break

#movies tickets
age=0
ticket=0
while True:
  age = input()
  if age =='quit':
    break
  age = int(input("Enter the age"))

  if age < 3:
    print("free ticket")
  elif age < 12:
    print("ticket is $10")
  else:
    print("ticker is $15")  

#infinity 3
while True:
    print(1+1)
    break

#sandwich 4
sandwich_order=["chicken sandwich", "cheese sandwich", "veggie sandwich", "egg sandwich"]
finished_sandwiches=[] 
while sandwich_order:
  order=sandwich_order.pop()
  print(order + "is ready to go")
  finished_sandwiches.append(order) 
for sandwich in finished_sandwiches:
  print(order + "sandwich is ready")

#no pastrami 5
sandwich_order=["pastrami","chicken sandwich", "cheese sandwich", "veggie sandwich", "egg sandwich"]
finished_sandwich=[]
while "pastrami" in sandwich_order:
  sandwich_order.remove("pastrami")
print("\n")
while sandwich_order:
  order=sandwich_order.pop()
  print(f"your {order} has been made.")
  finished_sandwich.append(order)
print("\n") 
for sandwich in finished_sandwich:
    print(f"{sandwich} is ready.")
