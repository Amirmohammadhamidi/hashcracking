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

    # def crack_two_digit_hash(hash: str, type: str, combination: str):


# def crack_six_loop(hash: str, type: str, word: str):


def crack_fifth_loop(hash: str, type: str, word: str):
    # 3 min
    global password_cracked
    if (password_len == 5):
        for counter in range(70):
            if (password_cracked):
                break
            if (check_password_validity(hash, word + charset[counter], type)):
                password_cracked = True
                print("password: ", word + charset[counter])
                break
    # else:
    #     for counter in range(70):
    #         crack_six_loop(hash, type, word + charset[counter])


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
        # print("thread with index : ", counter, " created")
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
        # print("thread with index : ", counter, " created")
        if (password_cracked):
            break


def handle_md5():
    target_hash = input("enter target hash : ")
    print("wait for cracking...")
    crack_first_loop(target_hash, "md5")


def handle_thread_number():
    global password_len
    while (True):
        password_len_str = input("password characters number :")
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

    # we will make it more accurate


print("options : ")
print("[1]:md5_hashCracker")
print("[2]:default_hashCracker")
print("[3]:exit")
selected_option = input("enter target mode : ")
while (True):
    try:
        selected_option_index = int(selected_option)
        handle_thread_number()
        if (selected_option_index == 1):
            handle_md5()
        elif (selected_option_index == 3):
            print("bye!")
            break
    except ValueError:
        print("invalid input format")
