"""TRY BLOCK"""

try: 
    with open("app.py") as file:
        print("File Opened.")

    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("A valid value wasn't entered")
except ZeroDivisionError: #This whole block here is replaced with the above blcok
    print("Age cannot be 0.")
else:
    print("No exceptions were thrown")
finally:
    file.close()
print("Execution continues...")


"""RAISING"""
raise ValueError