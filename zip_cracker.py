import sys
import time
import zipfile
from tqdm import tqdm

# Get zip file
zip_file = None
if len(sys.argv) > 1:
    zip_file = sys.argv[1]
else:
    print("ERROR: PLEASE ENTER A ZIP FILE")
    exit(0)

# Get password list
# Only sets password list if argument is given in command
passwordlist = ''
if len(sys.argv) > 2:
    passwordlist = sys.argv[2]

# Check if zip file exists
try:
    zip_file = zipfile.ZipFile(zip_file)
except FileNotFoundError:
    print("ERROR: ZIP FILE DOES NOT EXIST")


def bruteForce(possible, password_max_length, title):
    print(title)

    password_possibilities = pow(len(possible), password_max_length)
    start_time = time.time()

    for i in range(password_max_length - 1):
        password_possibilities += pow(len(possible), (i + 1))

    password_tested = 0

    for i in range(password_max_length):
        indices = [0 for x in range(i + 1)]

        while indices[0] < len(possible):
            # create password
            pwd = ""
            for j in range(len(indices)):
                pwd += possible[indices[j]]

            indices[len(indices) - 1] += 1

            if len(indices) > 1:
                if indices[len(indices) - 1] == len(possible):
                    for j in range(len(indices) - 1, 0, -1):
                        if indices[j] == len(possible):
                            indices[j] = 0
                            if j != 0:
                                indices[j - 1] += 1
                        else:
                            break

            password_tested += 1
            percentage = round(password_tested / password_possibilities * 10000) / 100
            time_spent = round((time.time() - start_time) * 100) / 100
            sys.stdout.write(f"\rpasswords tested: {password_tested} / {password_possibilities} - {percentage}% -"
                             f" [{time_spent} s]")
            sys.stdout.flush()

            try:
                zip_file.extractall(pwd=str.encode(pwd))
            except (RuntimeError, zipfile.BadZipFile):
                continue
            else:
                print(f"\npassword: {pwd}")
                exit(0)


# Crack password of zip with password list file
if passwordlist != '':
    num_lines = 0
    try:
        num_lines = len(list(open(passwordlist, "rb")))
    except FileNotFoundError:
        print("ERROR: PASSWORD LIST FILE NOT FOUND")
        exit(0)

    final_password = ""

    # loops through every password in given file
    with open(passwordlist, "rb") as passwords:
        for password in tqdm(passwords, total=num_lines, unit="passwords"):
            # tries if given password is correct
            try:
                zip_file.extractall(pwd=password.strip())
            except (RuntimeError, zipfile.BadZipFile):
                continue
            else:
                final_password = password
                break
    print(f"password: {final_password.decode().strip()}")
    exit(0)
else:
    # Possible symbols in password
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    # other = '![]{}()%&*$#^<>~@|'
    password_max_length = 7

    bruteForce(numbers, password_max_length, "Checking for passwords with only numbers")
    bruteForce(lowercase_letters, password_max_length, "\nChecking for passwords with only lowercase letters")
    bruteForce(uppercase_letters, password_max_length, "\nChecking for passwords with only uppercase letters")
    bruteForce(lowercase_letters + uppercase_letters, password_max_length, "\nChecking for passwords with uppercase "
                                                                           "letters and lowercase letters")
    bruteForce(lowercase_letters + numbers + uppercase_letters, password_max_length, "\nChecking for passwords with "
                                                                                     "uppercase letters, numbers and"
                                                                                     " lowercase letters")
