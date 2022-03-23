# noinspection PyUnusedLocal
# skus = unicode string
from collections import Counter
import string

def update_items(item_counts, item1, item2, required_amount):
    """remove any items the customer is getting for free from the items_count dictionary"""
    num_free_item1s = item_counts[item2]//required_amount
    return item_counts[item1] - num_free_item1s
    
def get_total_cost(item_counts):
    price_list={"A":50,"B":30,"C":20,"D":15,"E":40,"F":10,"G":20,"H":10,"I":35,"J":60,"K":80,"L":90,"M":15,"N":40,"O":10,"P":50,"Q":30,"R":50,"S":30,"T":20,"U":40,"V":50,"W":20,"X":90,"Y":10,"Z":50}
    list1=["B", "M", "Q"]
    list2=["E", "N", "R"]
    required_amounts=[2, 3, 3]
    for item1, item2, required_amount in zip(list1, list2, required_amounts):
        item_counts[item1]=update_items(item_counts, item1, item2, required_amount)

    total_cost=0
    for item in item_counts.keys():
        if item=="A":
            num_5s=item_counts[item]//5
            num_3s=(item_counts[item]%5)//3
            num_1s=item_counts[item] - (num_5s*5 + num_3s*3)
            total_cost+= num_5s * 200 + num_3s * 130 + num_1s * price_list[item]

        if item=="B":
            num_2s=item_counts[item]//2
            num_1s=item_counts[item]%2
            total_cost+= num_2s * 45 + num_1s * price_list[item]
        
        if item=="F":
            total_cost+=(item_counts[item]//3) * 10

        if item=="H":
            num_10s=item_counts[item]//10
            num_5s=(item_counts[item]%10)//5
            num_1s=item_counts[item] - (num_10s*10 + num_5s*5)
            total_cost+= num_10s * 80 + num_5s * 45 + num_1s * price_list[item]

        if item=="K":
            num_2s=item_counts[item]//2
            num_1s=item_counts[item]%2
            total_cost+= num_2s * 150 + num_1s * price_list[item]

        if item=="P":
            num_5s=item_counts[item]//5
            num_1s=item_counts[item]%5
            total_cost+= num_5s * 200 + num_1s * price_list[item]
        
        if item=="Q":
            num_3s=item_counts[item]//3
            num_1s=item_counts[item]%2
            total_cost+= num_3s * 80 + num_1s * price_list[item]
        
        if item=="U":
            total_cost+= (item_counts[item]//4) * price_list[item]
            
        if item=="V":
            num_3s=(item_counts[item]%5)//3
            num_2s=item_counts[item]//2
            num_1s=item_counts[item] - (num_3s*5 + num_2s*3)
            total_cost+= num_3s * 130 + num_2s * 90 + num_1s * price_list[item]
        

    return total_cost


def checkout(skus):
    """
    Input: receives a string representing the items 
    Output: need to return the price of the items, if illegal input need to output -1
    Note: haven't been told the exact form of the input i.e are there spaces etc?
    also havn't been told if an empty string is an illegal input or not?
    also has't been mentioned if the multi items will always come in together as nX or not.
    """
    total=0
    allowed=set(string.ascii_uppercase)
    for char in skus:
        if char not in allowed:
            return -1

    item_counts=Counter(skus)
    total=get_total_cost(item_counts)

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


