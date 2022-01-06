def main():
    """The program will implement writing and decoding a code for text files that contain Latin letters"""
    number_use= input("Please choose between e and d-  ")
    if number_use=="e":
        key=input("please write Encryption key- ")
        file=input("please write  name of file- ")
        print(e(key,file))
    if number_use=="d":
        key=input("please write Encryption key- ")
        file=input("please write name of file- ")
        print (d(key,file))
main()
