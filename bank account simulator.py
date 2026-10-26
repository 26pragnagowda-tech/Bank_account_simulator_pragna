balance = 0.0
transactions = []


def check_balance():
    print(f"\nCurrent Balance: ₹{balance:.2f}")


def deposit():
    global balance
    try:
        amount = float(input("Enter deposit amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
        else:
            balance += amount
            transactions.append(f"Deposited: ₹{amount:.2f}")
            print("Deposit successful!")
            print(f"Updated Balance: ₹{balance:.2f}")

    except ValueError:
        print("Invalid input! Please enter a number.")


def withdraw():
    global balance
    try:
        amount = float(input("Enter withdrawal amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
        elif amount > balance:
            print("Insufficient balance! Withdrawal rejected.")
        else:
            balance -= amount
            transactions.append(f"Withdrawn: ₹{amount:.2f}")
            print("Withdrawal successful!")
            print(f"Updated Balance: ₹{balance:.2f}")

    except ValueError:
        print("Invalid input! Please enter a number.")


def show_transactions():
    print("\n--- Transaction History ---")

    if not transactions:
        print("No transactions yet.")
    else:
        for index, transaction in enumerate(transactions, start=1):
            print(f"{index}. {transaction}")

    print(f"Current Balance: ₹{balance:.2f}")


def main():
    while True:
        print("\n===== BANK ACCOUNT SIMULATOR =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            show_transactions()
        elif choice == "5":
            print("Thank you for using our Bank Simulator!")
            break
        else:
            print("Invalid choice! Please select between 1 and 5.")


if __name__ == "__main__":
    main()
