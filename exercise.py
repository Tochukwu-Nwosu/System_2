import json

with open("exercise.json") as reader:              # Opens the exercise.json file as reader
    details = json.load(reader)                    # Stores the data in the json file to the variable 'details'

class system:
    def __init__(self):
        pass
    def registration (self):
        print("\nREGISTRATION\n")
        self.username = input("Enter username: ")
        self.password = input("Enter password: ")
        if (self.username in details.keys()):                                     
            print("Username alredy exist!")
        else:
            details[self.username] = self.password
            with open("exercise.json", "w") as reader:
                json.dump(details, reader)
            print("Registration Completed!")
        
    def login (self):
        print("\nLOGIN\n")
        self.username = input("Enter username: ")
        self.password = input("Enter password: ")

        if (self.username in details.keys() and self.password == details[self.username]):
            print("Welcome!")
        else:
            print("Please Register!")



obj = system()
obj1 = system()
obj.registration()
obj1.registration()
obj.login()
obj.login()
obj.login()
# obj2 = system()
# obj3 = system()
# obj4 = system()
print(details)