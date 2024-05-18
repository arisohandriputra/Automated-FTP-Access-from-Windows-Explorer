# Automated FTP Access from Windows Explorer
This Python code allows you to automatically log into FTP using given credentials, and then open Windows Explorer to navigate to that FTP. It uses the ftplib module to interact with FTP, os to run commands on the operating system, and keyring to store passwords securely. In addition, the code uses winshell to create a shortcut on the desktop. By replacing the FTP address, username, and password values, you can use this script for a variety of different FTP accounts.
### Required modules:
To run it, you just need to make sure that you have Python installed and that the ftplib and keyring modules are installed. The os module is part of the standard Python installation, so you don't need to install it separately.
You can install the keyring module using pip by running the following command in a terminal or command prompt:
```
pip install keyring
```
Also make sure you have the winshell module, as it is required to create shortcuts on the desktop. You can install it by running the command:
```
pip install pywin32
```
### Features:
* This code allows you to log into the FTP using the given credentials and open Windows Explorer automatically to navigate to that FTP.
* It utilises Python's inbuilt module **'ftplib'** to interact with FTP and **'os'** to execute commands in the operating system.
* By changing the **'ftp_address'**, **'username'**, and **'password'** values, you can easily use them for different FTP accounts.

> [!NOTE]
> This code is a simple example that I implemented based on my imagination, credential security does not include perfect security.

> [!CAUTION]
> Please be careful and do not publish your FTP credentials such as your FTP **Username** and **Password**.
