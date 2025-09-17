# Write a function to validate input from user as int between 0 to 9

def take_input():
    try :
        num = int(input("Enter a number between 0 to 9: "))
        if num not in range(10):
            raise ValueError("Number not in range")
        return num
    except Exception as e:
        print(e)
        return take_input()  # recursion

print(take_input())