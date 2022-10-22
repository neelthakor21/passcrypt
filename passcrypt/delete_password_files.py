import os
import protect_folder as pf
import shutil

def deleteF(duFolder, duAppFile):
    cwd = os.getcwd()

    if duFolder:
        try:
            print("\n" + "-"*100)
            userFolder = input("[+] Enter USER FOLDER name to be deleted :: ")
            print("-"*100)

            userFolderPath = os.path.join(cwd, userFolder)
            os.chdir(userFolderPath)

            if not pf.validatePassword():
                return False

            os.chdir(cwd)

            shutil.rmtree(userFolderPath)

            print("="*100)
            print(f"[+] USER FOLDER {userFolder} deleted successfully...")
            print("="*100 + "\n")

        except KeyboardInterrupt:
            print()
            print("-"*100)
            print("[-] Some KEYBOARD interruption occure...!!!\n[-] Please try again!!!")
            print("-"*100)

        except PermissionError as error:
            print("\n" + "-"*100)
            print(f"[-] {error}")
            print("-"*100 + "\n")

        except FileNotFoundError as error:
            print("\n" + "-"*100)
            print(f"[-] {error}")
            print("-"*100 + "\n")
    
    elif duAppFile:
        try:
            print("\n" + "-"*100)
            userFolder = input("[+] Enter USER FOLDER name to be deleted :: ")
            print("-"*100 + "\n")

            userFolderPath = os.path.join(cwd, userFolder)
            os.chdir(userFolderPath)

            if not pf.validatePassword():
                return False

            print("\n" + "-"*100)
            userApp = input("[+] Enter USER Application to be deleted from USER FOLDER :: ")
            print("-"*100 + "\n")

            userAppPath = os.path.join(userFolderPath, userApp)

            shutil.rmtree(userAppPath)

            print("="*100)
            print(f"[+] USER APPLICATION {userApp} deleted successfully from USER FOLDER {userFolder}...")
            print("="*100 + "\n")
            
        except KeyboardInterrupt:
            print()
            print("-"*100)
            print("[-] Some KEYBOARD interruption occure...!!!\n[-] Please try again!!!")
            print("-"*100)

        except PermissionError as error:
            print("\n" + "-"*100)
            print(f"[-] {error}")
            print("-"*100 + "\n")

        except FileNotFoundError as error:
            print("\n" + "-"*100)
            print(f"[-] {error}")
            print("-"*100 + "\n")