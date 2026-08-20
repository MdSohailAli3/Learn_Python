#file handling
# file = open("order.txt","w")
# try:
#     file.write("Ginger - 4 cups")
# finally:
#     file.close()


with open("orders.txt","w") as file:
    file.write("Masala - 5 cups")
