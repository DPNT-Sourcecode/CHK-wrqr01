from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """
    Input: receives a string representing the items 
    Output: need to return the price of the items, if illegal input need to output -1
    Note: haven't been told the exact form of the input i.e are there spaces etc?
    also havn't been told if an empty string is an illegal input or not?
    also has't been mentioned if the multi items will always come in together as nX or not.
    """
    total=0
    # keep track of the number discountable of items with a dictionary 
    discount_tracker=defaultdict(int)
    discount_tracker["A"]=3
    discount_tracker["B"]=2
    # handle digits in input by storing them for the next time
    store_the_number=1
    for item in skus:
        if item=="A":
            total+=50 * store_the_number
            discount_tracker["A"]-=1*store_the_number
            store_the_number=1
            if discount_tracker["A"]==0: 
                total-=20
                discount_tracker["A"]=3
        elif item=="B":
            total+=30 * store_the_number
            discount_tracker["B"]-=1 * store_the_number
            store_the_number=1
            if discount_tracker["B"]==0: 
                total-=15
                discount_tracker["B"]=3
        elif item=="C":
            total+=20 * store_the_number
            store_the_number=1
        elif item=="D":
            total+=15
        elif item.isdigit():
            store_the_number=item
        elif item==" ":
            continue
        else:
            return -1
    return total


