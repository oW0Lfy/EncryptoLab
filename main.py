from cryptography.fernet import Fernet
import hashlib
import os
import time
import base64

vld = "cbb70618ee5db13ea95a5e649276392103746ff10bce4f8c83ad33dee4e9d3daeb9bf6df82dec5146ae88af2a7d05c03ee5273630819f1719a64c2b56b2680bb"
#vld="1f40fc92da241694750979ee6cf582f2d5d7d28e18335de05abc54d0560e0f5302860c652bf08d560252aa5e74210546f369fbbbce8c12cfc7957b2652fe9a75"
def chckfile(fname0):
    fak= True
    try:
        with open(fname0, 'rb') as file:
            file = file.read()
    except:
        fak = False
    while fak == False:
        fname0 = input(str('Wrong Path. Try again:\n>'))
        try:
            with open(fname0, 'rb') as file:
                file = file.read()
        except:
            print("Nope,\n")
        else:
            fak = True
    return fname0
def chckkey(key0):
    keyauth0= True
    if key0[-4:] != ".key":
        keyauth0 = False
    try:
        with open (key0, "rb") as filekey:
            keyr = filekey.read()
    except:
        print("Nope.")
        keyauth0 = False
    while keyauth0 == False:
        key0 = input(str("Give Correct Key.\n>"))
        if key0[-4:] == ".key":
            keyauth0 = True
        else:
            keyauth0 = False
        try:
            with open (key0, "rb") as filekey:
                keyr = filekey.read()
        except:
            print("Nope.")
            keyauth0 = False
        else:
            keyauth0 = True
    with open (key0, "rb") as filekey:
        keyr = filekey.read()
    fernet0 = Fernet(keyr)
    return fernet0


def vald():
    inpVr = input(str("\n>"))
    psrd = hashlib.sha512()
    psrd.update(inpVr.encode("utf-8"))
    vrfy = psrd.hexdigest()
    return vrfy

def encry(fname):
    fname=chckfile(fname)
    nam=input(str('Give your Key`s Name:\n>'))
    fn = input(str("Give your File's Name:\n>"))
    key = Fernet.generate_key()
    with open("Key/"+nam+".key", 'wb')as filekey:
        filekey.write(key)
    with open ("Key/"+nam+".key","r") as namekey:
        reads=namekey.read()
    fernet = Fernet(key)
    print ("Your Encryption Key is:",reads)
    
    test = chckfile(fname)
    with open(test,"rb")as filen:
        original=filen.read()
    encrypted = fernet.encrypt(original)
    with open("Encrypted/"+fn+".encry", 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def decry(fname, key2):
    wrongkey = False
    fernet = key2
    # opening the encrypted file
    test=chckfile(fname)
    with open(test , "rb") as enc_file:
        encrypted = enc_file.read()
    #Checking Encryption key
    try:
        decrypted = fernet.decrypt(encrypted)
    except:
        print('Wrong Key Given.')
        wrongkey = True
    while wrongkey == True:
        key2 = input(str("Give Correct Key.\n>"))
        fernet = chckkey(key2)
        try:
            decrypted = fernet.decrypt(encrypted)
        except:
            print('NO VALID KEY MASTER.\n')
        else:
            wrongkey = False
    nam=input(str("Give your Decrypted File a name:\n>"))
    ext=input(str("Give your Decrypted File an Extension:\n(txt,jpg,png, etc)\n>"))
    # opening the file in write mode and
    # writing the decrypted data
    with open("DecryptResult/"+nam+"."+ext, 'wb') as dec_file:
        dec_file.write(decrypted)

dead=4
print("Welcome User.\n Who are you?")
auth=vald()
while auth != vld:
    dead=dead-1
    print("You have",dead,"tries left before REMOVAL and LOCKDOWN.")
    if dead == 0:
        print ("EXITING AND DELETING FILES . . .")
        time.sleep(2.5)
        exit()
    time.sleep(2.5)
    auth=vald()

os.system('cls')
print("I hope it is you Wolfy..\n\n")
print ("LOADING . . .")
time.sleep(3)
os.system("cls")
opts=["1","2","0"]
print('Welcome back Wolfy.')
print('\nSelect an Option:\n(1)Encrypt File\n(2)Decrypt File\n\n(0)EXIT')
quits=False
question = input("\n>")
while question not in opts:
    question = input("Come on Master, Don't be FOOKIN stoopid.\n>")
if question == "0":
    quits = True
while quits == False:
    if question == opts[0]:
        time.sleep(2.5)
        os.system("cls")
        print("ECRYPTION SELECTED. . .\n\n")
        file=input(str('Give File Path:\n>'))
        encry(file)

    if question == opts[1]:
        time.sleep(2.5)
        os.system("cls")
        print("DECRYPTION SELECTED. . .\n\n")
        fquest=input(str('Give File Path:\n>'))
        file = chckfile(fquest)
        qkey=input(str("Give Key Path:"))
        key=chckkey(qkey)
        decry(file, key)
    if question == opts[2]:
        exit()
    print('\nSelect an Option:\n(1)Encrypt File\n(2)Decrypt File\n\n(0)EXIT')
    question = input("\n>")
exit()
#---------------------------------------------------
# using the key

