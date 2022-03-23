from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string


def apply_discounting(skus):
    number_of_fs=skus.count("F")
    number_of_free_bs = skus.count("E")//2
    number_of_bs = skus.count("B")
    
    if number_of_bs==0:
        return (number_of_fs//3) * 10
    else:
        return (((number_of_bs - number_of_free_bs) // 2) * 15) + (number_of_free_bs * 30) + (number_of_fs//3) * 10
    
    


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
    #discount_tracker["B"]=2
    for item in skus:
        if item=="A":
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
        elif item=="C":
            total+=20 
        elif item=="D":
            total+=15
        elif item=="E":
            total+=40
        elif item=="F":
            total+=10
        elif item==" ":
            continue
        else:
            return -1
    
    total-=apply_discounting(skus)
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
