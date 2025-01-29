# my_app.py
def greet(name):
  """
  This function greets the user with a personalized message.

  Args:
    name: The name of the user to greet.

  Returns:
    A string containing the greeting message.
  """
  return f"Hello, {name}! Welcome to my simple Python app."

if __name__ == "__main__":
  name = input("Enter your name: ")
  print(greet(name))
