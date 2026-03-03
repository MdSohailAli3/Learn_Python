import json
def load_data():
    try:
        with open('data.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("not found")
        return {}
    
def save_data_helper(data):
    with open('data.txt','w') as file:
        json.dump(data,file)

def login(data):
    print()
    name = input("Enter Username: ")
    password = input("Enter Password: ")
    if(data.get(name) == password):
        print("Login Succesful.")
        return True
    else:
        print("Invalid username or password.")
    return False    




def signUp(data):
    name = input("Enter Username: ")
    password = input("Enter Password: ")
    #checking if user already exist
    if name in data:
        print("Account already exists!!, Try Login.")
        return

    data[name] = password
    save_data_helper(data)
    print("Account created successfully")


def main():
    data = load_data()
    while True:
        print("\nWelcome User:")
        print("1. Login")
        print("2. Sign-UP")
        print("3. Exit")
        choice = input("Enter Chaoice: ")
        match choice:
            case '1':
                if(login(data)): #check first that user exist
                    break
            case '2':
                signUp(data)
            
            case '3':
                break
            case _:
                print("Enter correct option!!!")

if __name__ == "__main__":
    main()