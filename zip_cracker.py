import sys
import zipfile
from tqdm import tqdm

# https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt
passwordlist = ''
zip_file = sys.argv[1]

# Only sets password list if argument is given in command
if len(sys.argv) > 2:
    passwordlist = sys.argv[2]

zip_file = zipfile.ZipFile(zip_file)
# Crack password of zip with password list file
if passwordlist != '':
    num_lines = len(list(open(passwordlist, "rb")))

    # loops through every password in given file
    with open(passwordlist, "rb") as passwords:
        for password in tqdm(passwords, total=num_lines, unit="passwords"):
            # tries if given password is correct
            try:
                zip_file.extractall(pwd=password.strip())
            except (RuntimeError, zipfile.BadZipFile):
                continue
            else:
                print(f"\npassword: {password.decode().strip()}")
                exit(0)
else:
    # Possible symbols in password
    possible = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'#![]{}()%&*$#^<>~@|'
    password_max_length = 4
    password_possibilities = pow(len(possible), password_max_length)

    for i in range(password_max_length):
        indices = [0 for x in range(i + 1)]
        print(i + 1)
        while indices[0] < len(possible) - 1:
            # create password
            password = ""
            for j in range(len(indices)):
                password += possible[indices[j]]

            indices[len(indices) - 1] += 1

            if len(indices) > 1:
                if indices[len(indices) - 1] == len(possible) - 1:
                    for j in range(len(indices) - 1, 0, -1):
                        if indices[j] == len(possible) - 1:
                            indices[j] = 0
                            if j != 0:
                                indices[j - 1] += 1
                        else:
                            break

            try:
                zip_file.extractall(pwd=str.encode(password))
            except (RuntimeError, zipfile.BadZipFile):
                continue
            else:
                print(f"\npassword: {password}")
                exit(0)