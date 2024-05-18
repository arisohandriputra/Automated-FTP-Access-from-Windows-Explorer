from ftplib import FTP
import os
import keyring
import winshell

def create_ftp_shortcut(ftp_address, username, password, shortcut_name):
    try:
        ftp = FTP(ftp_address)
        ftp.login(username, password)
        print("Successful login to FTP")

        shortcut_target = f'ftp://{username}:{password}@{ftp_address}'
        
        desktop = winshell.desktop() 
        shortcut_path = os.path.join(desktop, f'{shortcut_name}.lnk')
        with winshell.shortcut(shortcut_path) as shortcut:
            shortcut.path = shortcut_target
            shortcut.description = 'FTP Shortcut'
        
        print(f"Shortcut successfully created in: {shortcut_path}")
        ftp.quit()
    except Exception as e:
        print("Failed to create a shortcut:", e)

if __name__ == "__main__":
    ftp_address = "your_ftp_server"
    username = "your_ftp_username" 
    password = keyring.get_password("FTP", username)

    if not password:
        print("Password not found on keyring. Please enter the password:")
        password = input("Password: ")
        keyring.set_password("FTP", username, password)

    shortcut_name = "FTP Shortcut"
    create_ftp_shortcut(ftp_address, username, password, shortcut_name)
    
# Access FTP with Windows Explorer and automatically create Shortcuts on the Desktop