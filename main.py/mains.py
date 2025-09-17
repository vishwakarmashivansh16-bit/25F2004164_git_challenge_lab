# main.py
# Arithmetic Operations in a single Pythn
#main.py;

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def main():
    print("Welcome to Arithmetic Operations Project")
    print("Choose an operation:")
    print("1. Sum")
    print("2. Difference")
    print("3. Product")

    choice = int(input("Enter your choice (1-3): "))
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == 1:
        print("Result =", add(a, b))
    elif choice == 2:
        print("Result =", subtract(a, b))
    elif choice == 3:
        print("Result =", multiply(a, b))
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
