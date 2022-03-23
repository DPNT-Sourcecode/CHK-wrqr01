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
    discount_tracker["A"]=5
    discount_tracker["B"]=2
    discount_tracker["E"]=2
    # handle digits in input by storing them for the next time
    store_the_number=0
    for item in skus:
        if store_the_number==3 and item=="A":
            total+=130
            store_the_number=0
        elif store_the_number==2 and item=="B":
            total+=45
            store_the_number=0
        elif store_the_number!=0:
            return -1
        elif item=="A":
            total+=50
            discount_tracker["A"]-=1
            store_the_number=0
            if discount_tracker["A"]==0: 
                total-=30
                discount_tracker["A"]=5
            elif discount_tracker["A"]==2:
                total-=20
        elif item=="B":
            total+=30
            discount_tracker["B"]-=1
            store_the_number=0
            if discount_tracker["B"]==0: 
                total-=15
                discount_tracker["B"]=2
        elif item=="C":
            total+=20 
            store_the_number=0
        elif item=="D":
            total+=15
            store_the_number=0
        elif item=="E":
            total+=40
            discount_tracker["E"]-=1
            store_the_number=0
            if discount_tracker["E"]==0: 
                if "B" in skus:   
                    total-=30
                    discount_tracker["E"]=2
        elif item.isdigit():
            store_the_number=int(item)
        elif item==" ":
            continue
        else:
            return -1
    return total

# def checkout(skus):
#     """
#     Input: receives a string representing the items 
#     Output: need to return the price of the items, if illegal input need to output -1
#     Note: haven't been told the exact form of the input i.e are there spaces etc?
#     also havn't been told if an empty string is an illegal input or not?
#     also has't been mentioned if the multi items will always come in together as nX or not.
#     """
#     total=0
#     # keep track of the number discountable of items with a dictionary 
#     discount_tracker=defaultdict(int)
#     discount_tracker["A"]=3
#     discount_tracker["B"]=2
#     # handle digits in input by storing them for the next time
#     store_the_number=-1
#     for item in skus:
#         if item=="A":
#             total+=50 * store_the_number if store_the_number!=-1 else (store_the_number//3)*-30
#             discount_tracker["A"]-=1*store_the_number if store_the_number!=-1 else -1
#             store_the_number=-1
#             if discount_tracker["A"]==0: 
#                 total-=20
#                 discount_tracker["A"]=3
#         elif item=="B":
#             total+=30 * store_the_number if store_the_number!=-1 else store_the_number*-30
#             discount_tracker["B"]-=1 * store_the_number if store_the_number!=-1 else -1
#             store_the_number=-1
#             if discount_tracker["B"]==0: 
#                 total-=15
#                 discount_tracker["B"]=2
#         elif item=="C":
#             total+=20 * store_the_number if store_the_number!=-1 else store_the_number*-20
#             store_the_number=-1
#         elif item=="D":
#             total+=15 * store_the_number if store_the_number!=-1 else store_the_number*-15
#             store_the_number=-1
#         elif item.isdigit():
#             # handle numbers that have more than one digit
#             store_the_number=int(item) if store_the_number==-1 else int(str(store_the_number) + item)
#         elif item==" ":
#             continue
#         else:
#             return -1
#     return total




