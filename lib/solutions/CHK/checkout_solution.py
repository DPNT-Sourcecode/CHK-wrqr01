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
    discount_tracker=defaultdict(int)
    discount_tracker["A"]=3
    discount_tracker["B"]=2
    for item in skus:
        if item=="A":
            total+=50
            discount_tracker["A"]-=1
            if discount_tracker["A"]==0: 
                total-=20
                discount_tracker["A"]=3
        if item=="B":
            total+=30
            discount_tracker["B"]-=1
            if discount_tracker["B"]==0: 
                total-=15
                discount_tracker["B"]=3




