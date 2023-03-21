def encode(encode_password):
    res = ""
    for num in password:
        plus_3 = int(num) + 3
        more_than_10 = plus_3 % 10
        res += str(more_than_10)
    res = int(res)
    return res


if __name__ == "__main__":


    while True:



        print("Menu\n"
              "--------------")
        print("1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")
        option = int(input("Please enter an option: "))

        if option == 3:
            break
        elif option == 1:
            password = input("Please enter your password to encode: ")
            encode(password)
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            decoded = encode(password)
            print(f"The encoded password is {decoded}, and the original password is {password}.\n")
        else:
            continue