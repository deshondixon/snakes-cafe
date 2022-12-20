from textwrap import dedent


def snakesCafe():
    print(dedent(
        """
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************
    """
    ))
    enter = input("press enter to see view menu ")
    print(dedent("""
    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls
    
    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden
    
    Desserts
    --------
    Ice Cream
    Cake
    Pie
    
    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears
    
     ***********************************
     ** What would you like to order? **
     ***********************************
    
    """))

    order_dict = {}

    ask_again = True
    while ask_again:
        print
        choice = input("> ")
        if choice in order_dict:
            order_dict[choice] += 1
        else:
            order_dict[choice] = 1
        for choice in order_dict:
            if choice != "quit":
                print(f"**{order_dict[choice]} orders of {choice} have been added to your meal**")
        if choice == "quit":
            exit()
            break


if __name__ == "__main__":
    snakesCafe()
