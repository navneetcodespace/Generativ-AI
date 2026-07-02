try:
    filename = input("Enter file name: ")

    with open(filename, "r") as file:
        for i in range(3):
            print(file.readline(), end="")

except FileNotFoundError:
    print("File not found.")

except PermissionError:
    print("Permission denied.")

finally:
    print("\nFile operation attempted.")