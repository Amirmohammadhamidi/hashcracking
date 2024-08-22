import hashlib
import threading
import sys

password_len = 7
password_cracked = False
charset = list(
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$*_-.")


def check_password_validity(hash: str, password: str, type: str):
    if (type == "md5"):
        return (hashlib.md5(password.encode()).hexdigest() == hash)
    elif (type == "sha1"):
        return (hashlib.sha1(password.encode()).hexdigest() == hash)
    elif (type == "sha224"):
        return (hashlib.sha224(password.encode()).hexdigest() == hash)
    elif (type == "sha256"):
        return (hashlib.sha256(password.encode()).hexdigest() == hash)
    elif (type == "sha384"):
        return (hashlib.sha384(password.encode()).hexdigest() == hash)


def crack_six_loop(hash: str, type: str, word: str):
    global password_cracked
    if (password_len == 5):
        for counter in range(70):
            if (password_cracked):
                break
            if (check_password_validity(hash, word + charset[counter], type)):
                password_cracked = True
                print("password: ", word + charset[counter])
                break


def crack_fifth_loop(hash: str, type: str, word: str):
    # ~3 mins
    global password_cracked
    # if (password_len == 5):
    #     for counter in range(70):
    #         if (password_cracked):
    #             break
    #         if (check_password_validity(hash, word + charset[counter], type)):
    #             password_cracked = True
    #             print("password: ", word + charset[counter])
    #             break
    # else:
    for counter in range(70):
        crack_six_loop(hash, type, word + charset[counter])
        if (password_cracked):
            break


def crack_fourth_loop(hash: str, type: str, word: str):
    # max timout is: 20 sec
    global password_cracked
    # if (password_len == 4):
    #     for counter in range(70):
    #         if (password_cracked):
    #             break
    #         if (check_password_validity(hash, word + charset[counter], type)):
    #             password_cracked = True
    #             print("password: ", word + charset[counter])
    #             break
    # else:
    for counter in range(70):
        crack_fifth_loop(hash, type, word + charset[counter])
        if (password_cracked):
            break


def crack_third_loop(hash: str, type: str, word: str):
    global password_cracked
    # if (password_len == 3):
    #     for counter in range(70):
    #         if (password_cracked):
    #             break
    #         if (check_password_validity(hash, word + charset[counter], type)):
    #             password_cracked = True
    #             print("password: ", word + charset[counter])
    #             break
    # else:
    for counter in range(70):
        crack_fourth_loop(hash, type, word + charset[counter])
        if (password_cracked):
            break


def crack_second_loop(hash: str, type: str, word: str):
    global password_cracked
    # if (password_len == 2):
    #     for counter in range(70):
    #         if (password_cracked):
    #             break
    #         if (check_password_validity(hash, word + charset[counter], type)):
    #             password_cracked = True
    #             print("password: ", word + charset[counter])
    #             break
    # else:
    for counter in range(70):
        thread = threading.Thread(
            target=crack_third_loop, args=(hash, type, word + charset[counter]))
        thread.start()
        if (password_cracked):
            break


def crack_first_loop(hash: str, type: str):
    global password_cracked
    # if (password_len == 1):
    #     for counter in range(70):
    #         if (check_password_validity(hash, charset[counter], type)):
    #             password_cracked = True
    #             print("password: ", charset[counter])
    #             break
    # else:
    for counter in range(70):
        thread = threading.Thread(
            target=crack_second_loop, args=(hash, type, charset[counter]))
        thread.start()
        if (password_cracked):
            break


def crack_password(target_hash: str, type="md5"):
    crack_first_loop(target_hash, type)


def calculate_password_len():
    global password_len
    while (True):
        password_len_str = input("password characters number(default == 5) :")
        try:
            password_len = int(password_len_str)
            if (password_len < 1 or password_len > 8):
                print("hash cracker can crack passwords with len between 1 and 8")
                password_len = 7
            else:
                break
        except ValueError:
            password_len = 7
            print("input must be int")


print("options : ")
print("[1]:md5_hashCracker")
print("[2]sha1 hashCracker")
print("[3]sha224 hashCracker")
print("[4]sha256 hashCracker")
print("[5]sha384 hashCracker")
print("[6]:default_hashCracker")
print("[7]:exit")
selected_option = input("enter target mode : ")
while (True):
    try:
        selected_option_index = int(selected_option)
        if (selected_option_index == 7):
            print("bye!")
            break
        calculate_password_len()
        target_hash = input("enter target hash : ")
        print("wait for cracking...")
        if (selected_option_index == 1):
            crack_password(target_hash)
        elif (selected_option_index == 2):
            crack_password(target_hash, "sha1")
        elif (selected_option_index == 3):
            crack_password(target_hash, "sha224")
        elif (selected_option_index == 4):
            crack_password(target_hash, "sha256")
        elif (selected_option_index == 5):
            crack_password(target_hash, "sha384")
        else:
            print("invalid index")

    except ValueError:
        print("invalid input format")
