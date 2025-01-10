def get_user():
    A = set(input("Enter elements of set A: ").split())
    B = set(input("Enter elements of set B: ").split())
    return A, B

def menu():
    print("\nChoose an operation:")
    print("1. Union")
    print("2. Intersection")
    print("3. Difference")
    print("4. Subset Check")
    print("0. Exit")
    return input("Input your choice: ")

def main():
    A, B = get_user()
    already_invalid = False

    while True:
        operation = menu()

        if operation == '0':
            break

        if operation == '1':
            result = A | B
            print(f"Union: {result}")
        elif operation == '2':
            result = A & B
            print(f"Intersection: {result}")
        elif operation == '3':
            result1 = A - B
            result2 = B - A
            print(f"Difference (A - B): {result1}")
            print(f"Difference (B - A): {result2}")
        elif operation == '4':
            result1 = A <= B
            result2 = B <= A
            print(f"Subset Check (A ⊆ B): {result1}")
            print(f"Subset Check (B ⊆ A): {result2}")
        else:
            if not already_invalid:
                print("Invalid operation")
                already_invalid = True
            else:
                print("Not a valid number again")

if __name__ == "__main__":
    main()
