def greet(name):
    if name.isalpha():  # Check if name contains only letters
        return f"Hello, {name}! Welcome to my simple Python app."
    else:
        return "Please enter a valid name (letters only)."

if __name__ == "__main__":
    while True:  # Loop until valid input is received
        name = input("Enter your name: ")
        greeting = greet(name)
        print(greeting)
        if greeting.startswith("Hello"):  # Exit loop if valid name
            break
