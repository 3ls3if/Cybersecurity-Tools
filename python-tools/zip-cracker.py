from zipfile import ZipFile, BadZipFile

# Use a method to attempt to extract the zip file with a given password
def attempt_extract(zf_handle, password):
    try:
        # Attempt to extract the zip file using the password
        zf_handle.extractall(pwd=bytes(password.strip(), 'utf-8')) 
        print("[+] Password found: ", password.strip())
        return True
    except (RuntimeError, BadZipFile):  # RuntimeError is raised for a wrong password
        return False
    except ValueError:
        print("Error processing the password")
        return False
#

def main():
    print("[+] Beginning brute-force ")
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'r', errors='ignore') as f:
            # Iterate through password entries in rockyou.txt
            for passwd in f:
                if attempt_extract(zf, passwd):
                    print("[+] Extraction successful with password:", passwd.strip())
                    return
            print("[+] Password not found in list")
            # Attempt to extract the zip file using each password

if __name__ == "__main__":
    main()
