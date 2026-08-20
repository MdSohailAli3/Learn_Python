class InvalidChaiFlavour(Exception): pass

def billing(flavor,quantity):
    menu = {"masala":20, "ginger" : 30}
    try:
        if flavor not in menu:
            raise InvalidChaiFlavour("we dont serve this flavour.")
        if not isinstance(quantity, int):
            raise TypeError("quantity must be in integer number")
        total = menu[flavor] * quantity
        print(f"Total amount is rupees: {total}")
        
    except Exception as e:
        print("Error: ",e)

    finally:
        print("Thank you for visissting")


billing("mint",5)
billing(2,3)
billing("masala","one")
billing("masala",4)



    