import sys
import zipfile
from tqdm import tqdm

passwordlist = ''
zip_file = None
if len(sys.argv) > 1:
    zip_file = sys.argv[1]
else:
    print("ERROR: PLEASE ENTER A ZIP FILE")
    exit(0)

# Only sets password list if argument is given in command
if len(sys.argv) > 2:
    passwordlist = sys.argv[2]


try:
    zip_file = zipfile.ZipFile(zip_file)
except FileNotFoundError:
    print("ERROR: ZIP FILE DOES NOT EXIST")


def bruteForce(possible, password_max_length):
    password_possibilities = pow(len(possible), password_max_length)
    password_tested = 0

    for i in range(password_max_length):
        indices = [0 for x in range(i + 1)]

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

            password_tested += 1
            percentage = round(password_tested / password_possibilities * 100) / 100
            sys.stdout.write(f"\rpasswords tested: {password_tested} / {password_possibilities} - {percentage}%")
            sys.stdout.flush()

            try:
                zip_file.extractall(pwd=str.encode(password))
            except (RuntimeError, zipfile.BadZipFile):
                continue
            else:
                print(f"\npassword: {password}")
                exit(0)


# Crack password of zip with password list file
if passwordlist != '':
    try:
        num_lines = len(list(open(passwordlist, "rb")))
    except FileNotFoundError:
        print("ERROR: PASSWORD LIST FILE NOT FOUND")
        exit(0)

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
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'  # ![]{}()%&*$#^<>~@|'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    password_max_length = 10

    bruteForce(numbers, password_max_length)
