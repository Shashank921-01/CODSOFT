def calculator():
    print("✨ Welcome to CodSoft Calculator ✨")
    print("-" * 40)
    
    while True:
        print("\nChoose an operation:")
        print("1 ➝ Addition")
        print("2 ➝ Subtraction")
        print("3 ➝ Multiplication")
        print("4 ➝ Division")
        print("5 ➝ Modulus")
        print("6 ➝ Power")
        print("0 ➝ Exit")

        choice = input("Enter your choice: ")

        if choice == "0":
            print("\n🙏 Thanks for using the calculator. Goodbye!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("❌ Invalid choice! Please select a valid option.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("❌ Invalid input! Please enter numbers only.")
            continue

        if choice == "1":
            result = num1 + num2
            op = "+"
        elif choice == "2":
            result = num1 - num2
            op = "-"
        elif choice == "3":
            result = num1 * num2
            op = "×"
        elif choice == "4":
            if num2 == 0:
                print("⚠️ Division by zero is not allowed!")
                continue
            result = num1 / num2
            op = "÷"
        elif choice == "5":
            result = num1 % num2
            op = "%"
        elif choice == "6":
            result = num1 ** num2
            op = "^"

        print(f"\n✅ Result: {num1} {op} {num2} = {result}")
        print("-" * 40)


# Run the calculator
if __name__ == "__main__":
    calculator()
