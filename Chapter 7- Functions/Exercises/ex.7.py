
#message 1
def display_message():
    """display a message about what im learning"""
    msg= "i'm learning how to display a message in functions"
    print(msg) 
display_message()   

#favorite book 2
def favorite_book(title):
    """display a message about user's favorite book"""
    print(f"my favorite book is {title}.")
favorite_book("death on nile")    

#t-hirts 3
def make_shirt(size,text):
    """summarize the shirt that is going to be made."""
    print(f'\nwe do have a {size} shirt')
    print(f'the message on the tshirt is {text}')
make_shirt("small" , "bathspa university") 
make_shirt("medium" , "university of bath") 

#large shirts 4
def make_shirts(size = "large", text = "i love python"):
    """"summarize the shirt that is going to be made."""
    print(f"\nwe do have a {size} shirt.")
    print(f"the meassge on the shirt is {text}")
make_shirts()
make_shirts(size = "medium")
make_shirts("small" , "student of bathspa university")

#cities 5
def describe_city(city, country = 'finland'):
    """describe the city"""
    msg= f"{city} is in {country}."
    print(msg)
describe_city("helsinki")  
describe_city("vantaa") 
describe_city("sanvonlinna")  

