import socket
import sys
import time
def print_welcome():
    print ("\r\nWelcome to the SMTP user enumeration superscan\r\n")
print ("===============================================")
def enumerate_smtp(ip_address):
    # Path to the users dictionary file
    users_file_path= "/usr/share/metasploit-framework/data/wordlists/unix_users.txt"
    # Open the text file in Read mode and start enumerating
    with open(users_file_path,'r') as users_file:
        for user in users_file:
        # Clean-up the user value
            user = user.strip()
            # Do not process an empty user value
            if user == "":
                continue
            try:
                # Create a Socket object
                sok=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                # Connect to the SMTP Server
                sok.connect((ip_address,25))
                # Receive the banner from the server first
                sok.recv(1024)
                # Verify if the user exists on the server using the VRFY command
                sok.send('VRFY ' + user + '\r\n')
                # Sleep for 1 second so we don't flood the server
                time.sleep(1)
                #   Get the response from the server
                results=sok.recv(1024)
                if (not "550" in results):
                    print ("%s : Found" % user)
            except Exception:
                print ("An error occured!")
            finally:
                # Close the connection socket
                sok.close()
        # Let the user know that we finished
        print ("\r\nThe program has finished enumerating users.\r\n")
def main():
    print_welcome()
    enumerate_smtp(sys.argv[1])
if __name__ == '__main__':
    main()
