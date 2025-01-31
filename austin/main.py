# open/load file
# show graph
# enter wanted columns
# 
# tkinter or pyqt
# jan 29 - 2.5hr
# a

user = -1

while user != 0:
    print("file search program")
    # print("enter number: ")

    try:
        user = int(input("Choose and option: "))
        if user == 1:
            print("option 1")
        elif user == 2:
            print("option 2")
        elif user == 3:
            print("option 3")
        elif user == 0:
            print("finished")
            break
        else:
            print("enter a valid option")
    except ValueError:
        print("Invalid input! Please enter a number.")