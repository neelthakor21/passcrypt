import maskpass
import hashlib

def password_hashing(password):
    try:
        salt = "gta5"
        password_with_salt = password + salt

        hashed_password = hashlib.md5(password_with_salt.encode())
        # print(f"hashed password :: {hashed_password.hexdigest()}")
        return hashed_password.hexdigest()
    except:
        return -1

def strongPassword(password):
    special_char = ['@', '#', '!', '$', '%', '^', '&', '*', '?']
    val = True

    if len(password) < 6 or len(password) >= 12:
        print("\n" + "[-] Length of password should greater than 6 and less than or equal 12.")
        val = False
    
    if not any(char.isdigit() for char in password):
        print("\n" + "[-] Password should have at least one numeral.")
        val = False

    if not any(char.isupper() for char in password):
        print("\n" + "[-] Password should have at least one upper case letter.")
        val = False

    if not any(char.islower() for char in password):
        print("\n" + "[-] Password should have at least one lower case letter.")
        val = False

    if not any(char in special_char for char in password):
        print("\n" + "[-] Password should have at least one special characters like '@', '#', '!', '$', '%', '^', '&', '*', '?'.\n")
        val = False

    if val:
        return val
    else:
        return False


def make_password(folder_name, password_value):
    if password_value:
        count = 0
        while(count < 3):
            count += 1
            password = maskpass.askpass(prompt="[+] Enter the Password for USER FOLDER :: ", mask="*")
            print()
            re_entered_password = maskpass.askpass(prompt="[+] Re-Enter the password for USER FOLDER :: ", mask="*")
            print("-"*100)

            if password == re_entered_password:
                if strongPassword(password):
                    hashed_password = password_hashing(password) 

                    if hashed_password != -1:
                        with open("user_password.txt", "w") as up:
                            up.write(hashed_password)
                    
                    return True
                else:
                    print("-"*35 + "#"*30 + "-"*35 + "\n")
                    return False

            else:
                print("\n" + "-"*100)
                print("[-] Passwords does't match...try again!!!")
                print("-"*100 + "\n")

            if count == 3:
                print("[-] Three time fail to match the passwords! Try again later...")
                print("="*100 + "\n")
                return False
    else:
        print("\n" + "-"*35 + "#"*30 + "-"*35)
        print("|[-]--->  Password did't given by user, so default password is :: user_folder_name@passcrypt  <--|")
        print("-"*35 + "#"*30 + "-"*35 + "\n")

        default_password = folder_name + "@passcrypt"
        hashed_password = password_hashing(default_password)

        if hashed_password != -1:
            with open("user_password.txt", "w") as up:
                up.write(hashed_password)
            
            return True
        else:
            return False

def hash_match(hp1, hp2):    
    if hp1 == hp2:
        return True
    else:
        print("\n" + "-"*100)
        print("[-] Password doesn't match! try again...")
        print("-"*100 + "\n")
        return False

def validatePassword():
    count = 0
    while count < 3:
        count += 1
        val_pass = maskpass.askpass(prompt="[+] Enter password to access User folder :: ", mask="*")
        print("-"*100)

        hash_pass = password_hashing(val_pass)

        if hash_pass == -1:
            print("\n" + "-"*100)
            print("[-] some problem occure!!!")
            print("-"*100 + "\n")
        else:
            try:
                with open("user_password.txt", "r") as up:
                    hashed_pass = up.read()
            except FileNotFoundError:
                return False
            
            if count == 3:
                print("[-] Three time fail to match the passwords! Try again later...")
                print("="*100 + "\n")
                return False

            if hash_match(hash_pass, hashed_pass):
                return True
        
    return False