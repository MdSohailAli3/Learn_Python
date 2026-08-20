menu = {"masala" : 30, "ginger" : 40}

try:
    menu["elaichi"]
except KeyError:
    print("The key that you are trying to access does not exist!")
    