# day = 15

# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")     # runs
#     case 5:
#         print("Friday")
#     case _:
#         print("Weekend")

# month = 5
# day = 1

# match day:
#     case 1 | 2 | 3 if month == 5:
#         print("Early May")
#     case d if d > 10 and month == 5:
#         print("Late May")     # runs
#     case _:
#         print("Other")

RED = "red"
color = "blue"

match color:
    case RED:                 # NOT a comparison! Captures "blue" into RED
        print("matched")