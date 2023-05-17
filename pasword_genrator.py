from cryptography.fernet import Fernet
#used to encrpyt the data that we store in a file....

#creating a fnc to use the key which is creted below
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

'''def write_key():
    key = Fernet.generate_key()
    with open ("key.key", "wb") as key_file:#used to create the key
        key_file.write(key)
write_key()'''

key = load_key() 
fer = Fernet(key)

#key + password + text to encrypt = random text
#random text + key + password  = text

def view():
    with open("Pasaword.txt",'r')as f:
        for line in f.readlines():  #used to read all the line of the file at a time...
            print(line.rstrip())
            #rstrip fnc will strip our data and return from the file..
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user , "| Password:",fer.decrypt(passw.encode()).decode())

            
def add():
    name = input("Acoount name: ")
    pwd = input("password: ")

    #it will open the new file or if the file already exists it will add the new content to the file...
    
    with open("Pasaword.txt",'a')as f:  #here it will automatically close the file we need not to do it manually...
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
        #pwd is converted to its encryted form but first we encode it to covert it into bytes..
        
while True:
    #loop will run till the statement is true...
    mode = input("Would you like to create new password or view the existing one(press view/add),press q to quit)")
    if (mode == "q"):
        #It will break the loop and and return us no value...
        break 
    # Acc. to the above input 
    #if the user selects the view mode then , user can only read the data...
    elif(mode == "view"):
        #lets call the fnc view..
        view()
    #if the user selects the add mode then , user can create a new account...
    elif(mode == "add"):
        #lets call the fnc add..
        add()
    else:
        #otherwise it will show invalid and continue the statement...
        print("Invalid mode")
        continue

    