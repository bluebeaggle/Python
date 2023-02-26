def greet() :
    print("hello")
    print("hello")
    print("hello")
greet()

def greet_with_name(name) :
    print(f"hello {name} ")
    print(f"hello {name} ")
    print(f"hello {name} ")
greet_with_name("Daeheon")    

def greet_with(name, location) :
    print(f'hello my name is {name} and I live in {location}')
greet_with("Daeheon", "Seoul")
greet_with(location = "Seoul", name="Daeheon")

