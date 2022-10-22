import cryptography
from cryptography.fernet import Fernet
import protect_folder as pf
import os
import shutil

def validation(f_path, add_newpass):
    if add_newpass:
        if not os.path.exists(f_path):
            print("-"*100)
            print("[-] Folder NOT exists!!!")
            print("[-] Please enter existing Folder!!!")
            print("-"*100)
            return -1
        else:
            return 0
    else:
        if not os.path.exists(f_path):
            os.makedirs(f_path)
            return 0
        else:
            print("-"*100)
            print("[-] FOLDER/FILE ALREADY EXISTS!!!")
            print("[-] Enter unique FOLDER/FILE name.")
            print("-"*100)
            return -1

def application_folder(f_path, add_newpass):
    count = 0
    while (count < 3):
        count += 1
        user_application = input("[+] Enter the application for which this password serves as credintials :: ")
        print("-"*100)

        application_path = os.path.join(f_path, user_application)

        if add_newpass:
            temp = validation(application_path, False)
            if temp == -1:
                pass
            else:
                print("[+] Application Directory ware made successfully...")
                print("-"*100 + "\n")
                return application_path
        else:
            if validation(application_path, add_newpass) == 0:
                print("[+] Application Directory ware made successfully...")
                print("-"*100 + "\n")
                return application_path
    return -1

def passEncrypt(password, folder_name, *extra):
    try:
        def generate_key():
            key = Fernet.generate_key()
            with open("my_key.key", "wb") as thekey:
                thekey.write(key)

        def encrypt_pass(password):
            with open("my_key.key", "rb") as thekey:
                key = thekey.read()
            byte_pass = bytes(password,"utf-8")
            encrypted_password = Fernet(key).encrypt(byte_pass)
            return encrypted_password       

        my_path = os.path.abspath(os.getcwd())
        folder_path = os.path.join(my_path, folder_name)

        if extra[0]:
            if validation(folder_path, extra[0]) == -1:
                return -1
            else:
                os.chdir(folder_path)

                if not pf.validatePassword():
                    return -3

                e_password = encrypt_pass(password)
        else:
            if validation(folder_path, extra[0]) == -1:
                return -1
            else:
                os.chdir(folder_path)

                if extra[2]:
                    file_pass = pf.make_password(folder_name, True)
                else:
                    file_pass = pf.make_password(folder_name, False)

                if not file_pass:
                    os.chdir(my_path)
                    shutil.rmtree(folder_path)
                    return -3

                generate_key()
                e_password = encrypt_pass(password)

        app_path = application_folder(folder_path, extra[0])

        if app_path != -1:
            os.chdir(app_path)
        else:
            return -2

        if extra[1]:
            description = input("[+] Enter Desccription about Password...\n[+] ")
            print("-"*100)
            
            with open("description.txt", "w") as dp:
                dp.write("[+] Description about password...\n\n")
                dp.write("[+] " + description)

        with open("encrypted_password.txt", "w") as myFile:
            myFile.write("[+] Your ENCRYPTED password is ::: ")
            myFile.write(str(e_password))
            myFile.write("\n")

        os.chdir(my_path)

    except FileNotFoundError:
        print("-"*100)
        print("\n[-] FOLDER/FILE NOT exists...")
        print("\n[-] Make your encrypted file and try again...\n")
        print("-"*100)
        return -2
    except KeyboardInterrupt:
        print()
        print("-"*100)
        print("[-] Some KEYBOARD interruption occure...!!!\n[-] Please try again!!!")
        print("-"*100)
    except:
        print("\n" + "-"*100)
        print("[-] Some error occur, Please try again...")
        print("-"*100 + "\n")

def passDecrypt(folder_name, *extra):
    try:
        my_path = os.path.abspath(os.getcwd())
        folder_path = os.path.join(my_path, folder_name)

        if not os.path.exists(folder_path):
            print("-"*100)
            print("[-] FOLDER NOT exists...")
            print("[-] You have to make a FOLDER of encrypted passwords to decrypt it!!!")
            print("-"*100)
            return False
        
        if not os.path.isdir(folder_name):
            print("-"*100)
            print("[-] Enter valid FOLDER name!!!")
            print("-"*100 + "\n")
            return False

        os.chdir(folder_path)

        if not pf.validatePassword():
            return False

        user_application = input("[+] Enter the application for which this password serves as credintials :: ")
        print("-"*100)
        description_path = os.path.join(folder_path, user_application)

        with open("my_key.key", "rb") as key:
            the_key = key.read()

        os.chdir(description_path)

        try:
            if extra[0]:
                with open("description.txt", "r") as dp:
                    readf = dp.read()
                    print(readf)
        except FileNotFoundError:
            print("\n" + "-"*40 + "<>"*10 + "-"*40)
            print("[-] USER did not add DESCRIPTION file for this application!")
            print("-"*40 + "<>"*10 + "-"*40 + "\n")

        with open("encrypted_password.txt", "rb") as ep:
            ep_text = ep.read()

        encrypted_password = ep_text[36:]

        decrypted_password_bytecode = Fernet(the_key).decrypt(encrypted_password)
        decrypted_password = decrypted_password_bytecode.decode()

        os.chdir(my_path)
        return decrypted_password

    except cryptography.fernet.InvalidToken:
        print("-"*100)
        print("[-] Invelid Token")
        print("[-] Please try again")
        print("-"*100)
        return False
    except FileNotFoundError:
        print("-"*100)
        print("\n[-] FOLDER/FILE NOT exists...")
        print("\n[-] Make your encrypted file and try again...\n")
        print("-"*100)
        return False
    except TypeError:
        print("-"*100)
        print("\n[-] Check your encrypted password and try again...\n")
        print("-"*100)
        return False
    except NotADirectoryError:
        print("\n" + "-"*100)
        print("[-] The directory name is invalid!!!")
        print("[-] Please enter valid FILE/FOLDER name!!!")
        print("-"*100 + "\n")
        return False