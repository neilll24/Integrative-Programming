def divide(a, b):
    if b == 0:
        return None
    return a / b

def exponentiate(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        return None
    return a % b

def summation(a, b):
    if a > b:
        return None
    return sum(range(a, b + 1))

def main():
    while True:
        print("\n[D] Divide")
        print("[E] Exponentiate")
        print("[R] Remainder")
        print("[F] Summation")
        print("[Q] Quit")
        
        choice = input("Enter choice: ").upper()
        
        if choice == 'Q':
            break
        
        if choice in ['D', 'E', 'R', 'F']:
            try:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Enter numbers only.")
                continue
            
            if choice == 'D':
                result = divide(a, b)
            elif choice == 'E':
                result = exponentiate(a, b)
            elif choice == 'R':
                result = remainder(a, b)
            elif choice == 'F':
                result = summation(a, b)
            
            if result is None:
                print("Invalid Input")
            else:
                print("Result:", result)
        else:
            print("Invalid choice")

main()
