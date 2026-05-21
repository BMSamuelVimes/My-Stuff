import math

######--MONEY OR JUST A NUMBER--######
amount = float(input("What number are you doubling? "))
dblNum = int(input("How many times is it doubling? "))

yes_yes = ['yes', 'y']
yes_no = ['no', 'n']

while True:
    isMon = input("Is this money (yes/no)? ")
    if isMon.lower() in yes_yes:
        print("Continuing...")
        print(f"{'NumX':<8} {'Doubled':<15}")
        print("-----------------")
        for count in range(1, dblNum + 1):
            print(f"{count:<8} ${amount:,.2f}")
            amount *= 2
        break
    if isMon.lower() in yes_no:
        print(f"{'NumX':<8} {'Doubled':<15}")
        print("-----------------")
        for number in range(1, dblNum + 1):
            if number == 1:
                print(number, "\t", amount)
            elif number in range(2, dblNum + 1):
                Doubled = 2 * amount
                print(number, "\t", Doubled)
                amount = Doubled
        break
    else:
        print("Must be YES or NO.")



# ##########--JUST MONEY--#########
# amount = float(input("What number are you doubling? "))
# dblNum = int(input("How many times is it doubling? "))
# isMon = input("Is this money (yes/no)? ").lower()

 
# print(f"{'NumX':<8} {'Doubled':<15}")
# print("-----------------")


# for count in range(1, dblNum + 1):
#     print(f"{count:<8} ${amount:,.2f}")
#     amount *= 2


# for number in range(1, dblNum + 1):
#     if number == 1:
#          print(number, "\t", amount)
#     elif number in range(2, dblNum + 1):
#         Doubled = 2 * amount
#         print(number, "\t", Doubled)
#         amount = Doubled
    


# locale.setlocale(locale.LC_ALL, 'C')

# amount = float(input("What number are you doubling? "))
# dblNum = int(input("How many times is it doubling? "))
# isMon = input("Is this money (yes/no)? ").lower()
 
# print("NumX\tDoubled")
# print("-----------------")

# if isMon == "yes":
#     for number in range(1, dblNum + 1):
#        if number == 1:
#           print(number, "\t", amount)
#        elif number in range(2, dblNum + 1):
#           Doubled = 2 * amount
#           print(number, "\t", "$", Doubled)
#           amount = Doubled
# elif isMon == 'no":
#     for number in range(1, dblNum + 1):
#        if number == 1:
#           print(number, "\t", amount)
#        elif number in range(2, dblNum + 1):
#           Doubled = 2 * amount
#           print(number, "\t", Doubled)
#           amount = Doubled


# Money = .01
# Days = int(input("Please enter number of days worked. "))

# print("Days\tAmount Made")
# print("----------------------")

# for number in range(1, Days +1):
#     if number == 1:
#         print(number, "\t", .01)
#     elif number in range(2, Days +1):
#         Amount_Made = 2 * Money
#         print(number, "\t", Amount_Made)
#         Money = Amount_Made)