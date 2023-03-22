# Decoder function added by Maria Herreros (Period 7-8 Section with TA Teresa Vu)
def encode(encode_password):
    res = ""
    for num in password:
        plus_3 = int(num) + 3
        more_than_10 = plus_3 % 10
        res += str(more_than_10)
    res = int(res)
    return res


def decoder(password):
    password = str(password)
    new_password = ""
    for element in password:
        element = int(element)
        if 0 <= element <= 2:  # If the element is between 0 and 2 (would become negative after subtracting 3)
            element -= 3  # Subtract 3 from element (e.g. 0 becomes -3)
            element = 10 - abs(element)  # Subtract the abs value of element from 10 for new digit (e.g. -3 -> 7)
        else:
            element -= 3
        element = str(element)
        new_password += element
    return new_password


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
            encoded = encode(password)
            decoded = decoder(encoded)
            print(f"The encoded password is {encoded}, and the original password is {decoded}.\n")
        else:
            continue
