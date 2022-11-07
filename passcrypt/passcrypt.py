# passcrypt is platform where you can protect your passsword and store it...

import password_handling
import delete_password_files as dpf
import argparse
import maskpass
import sys
import pyfiglet, termcolor
import platform, os

# ---------------------------------############################------------------------------------------------------------

dev_info = """
                                        VERSION = 1.2
                                        DEVELOPED BY = NEEL THAKOR (Github ==> neelthakor21)
"""

if(platform.system() == 'Windows'):
    os.system('cls')
if(platform.system() == 'Linux'):
    os.system('clear')

line = "#"*120
print(termcolor.colored(dev_info, 'red', attrs=['dark', 'bold']))
print(termcolor.colored(line, 'cyan', attrs=['dark', 'bold']))

try:
  print(termcolor.colored(line, 'cyan', attrs=['dark', 'bold']))
  banner_text = pyfiglet.figlet_format("PASSCRYPT", font='starwars', width=500)
  print(termcolor.colored(banner_text, 'green', attrs=['dark', 'bold']))
except:
  pass

# ---------------------------------############################------------------------------------------------------------

parser = argparse.ArgumentParser(description="Encrypt and Decrypt your passwords and many more...")
muex = parser.add_mutually_exclusive_group()
muex.add_argument("-E", "--encrypt", action='store_true', help="To encrypt your password.")
muex.add_argument("-D", "--decrypt", action='store_true', help="To decrypt your password.")
parser.add_argument("-V", "--description", action='store_true',help="print description provided by user while encrypting.(THIS ARGUMENT USE WITH DECRYPT ARGUMENT!)")
parser.add_argument("-N", "--newpass", action='store_true', help="Enter password for new application for given user.(THIS ARGUMENT USE WITH ENCRYPT ARGUMENT!)")
parser.add_argument("-A", "--add_description", action='store_true', help="To add description for password.(THIS ARGUMENT USE WITH ENCRYPT ARGUMENT!)")
parser.add_argument("-P", "--password", action='store_true', help="To add password for your main folder.!!IF NOT GIVEN BY USER THEN IT SELECTS DEFAULT PASSWORD!! (THIS ARGUMENT USE WITH ENCRYPT ARGUMENT!)")
parser.add_argument("-dF", "--deleteUserFolder", action='store_true', help="To DELETE USER passwords folder.")
parser.add_argument("-df", "--deleteAppPassword", action='store_true', help="To DELETE USER APPLICATION password folder.")
args = parser.parse_args()

def pass_len(password, re_entered_password):
    if len(password) == 0 or len(re_entered_password) == 0:
        print("\n" + "-"*100)
        print("[-] Length of application password should not be 0!")
        print("-"*100 + "\n")
        return False
    else:
        return True

def password_validation(password, re_entered_password):
    if password == re_entered_password:
        return True
    else:
        return False


if __name__ == "__main__":
    if args.encrypt or args.newpass:
        try:
            count1 = 0
            while(count1 < 3):
                count1 += 1
            
                print("-"*100)
                user_password = maskpass.askpass(prompt="[+] Enter Your password for application :: ", mask="*")
                print("-"*100)
                reentered_user_password = maskpass.askpass(prompt="[+] Re-Enter Your password for application :: ", mask="*")
                print("-"*100)

                if not pass_len(user_password, reentered_user_password):
                    sys.exit(0)
                
                if password_validation(user_password, reentered_user_password):
                    count2 = 0
                    while(count2 < 3):
                        count2 +=1

                        user_foldername = input("[+] Enter USER name for store your encrypted passwords :: ")
                        print("-"*100)
                            
                        add_new_password = args.newpass
                        add_description = args.add_description
                        user_file_password = args.password

                        encrypted_pass = password_handling.passEncrypt(user_password, user_foldername, add_new_password, add_description, user_file_password)

                        if encrypted_pass != -1:
                            break
                    
                    if type(encrypted_pass) == str:
                        print("[+] Encrypting your password...")
                        print("[+] Password Encrypted successfully...")
                        print("="*45 + "#"*10 + "="*45)
                        break
                    else:
                        break
                else:
                    print("-"*100)
                    print("[-] Passwords doesn't match!!!")
                    print("[-] Re-enter passwords")
                    print("-"*100)

        except KeyboardInterrupt:
            print()
            print("-"*100)
            print("[-] Some KEYBOARD interruption occure...!!!\n[-] Please try again!!!")
            print("-"*100)

    elif args.decrypt:
        try:
            print("-"*100)
            user_folder_name = input("[+] Enter Your USER FOLDER Name :: ")
            print("-"*100)

            user_description = args.description
            
            decrypted_password = password_handling.passDecrypt(user_folder_name, user_description)

            if decrypted_password == False:
                pass
            else:
                print("="*100)
                print(f"[+] Your Decrypted pasword is ::: {decrypted_password}")
                print("="*100 + "\n")
        except KeyboardInterrupt:
            print()
            print("-"*100)
            print("[-] Some KEYBOARD interruption occure...!!!\n[-] Please try again!!!")
            print("-"*100)

    elif args.deleteUserFolder or args.deleteAppPassword:
        if not dpf.deleteF(args.deleteUserFolder, args.deleteAppPassword):
            sys.exit(-1)
        
    else:
        print("\n\n")
        print(parser.print_help())
        print("="*100)
        print()
