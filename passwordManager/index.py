from cryptography.fernet import Fernet


menu='''
        type 'add' for adding new password
        type 'view' for viewing password
        type 'q' to quit
'''
# pwd = input("Master Password? ")
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", 'wb') as key_file:
        key_file.write(key)
'''
def load_key():
    file = open("key.key", 'rb')
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)


def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print(f"User : {user}, Password : {fer.decrypt(passw.encode()).decode()}")
    

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('password.txt','a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")







while True:
    mode = input(menu).lower()
    if mode == 'add':
        add()
    elif mode == 'view':
        view()
    elif mode == 'q':
        break
    else:
        print("Invalid Mode.")
        continue