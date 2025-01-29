import random

def greet(name):
    greetings = ["Hello", "Hi", "Greetings", "Welcome", "Howdy"]
    random_greeting = random.choice(greetings)
    return f"{random_greeting}, {name}! Welcome to my simple Python app."

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet(name))
