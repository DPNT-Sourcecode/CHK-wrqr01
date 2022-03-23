# noinspection PyUnusedLocal
# skus = unicode string
from collections import Counter
import string

class checkout():
    def __init__(self):
        self.item_counts=None

    def update_items(self, item_counts, item1, item2, required_amount):
        """remove any items the customer is getting for free from the item_count dictionary"""
        num_free_item1s = item_counts[item2]//required_amount
        return item_counts[item1] - num_free_item1s if num_free_item1s < item_counts[item1] else 0

    def group_discount_offer(self):
        num=0
        offer_amount=0
        for item in ["S","T","X","Y","Z"]:
            num+=self.item_counts[item]
        num=num//3
        offer_amount += num*45
        
        # loop over from cheapest to most costly for customer to benefit most from offer
        # remove the items from the list so they won't be charged again
        for item in ["X","S","T","Y","Z"]:
            if self.item_counts[item] < num:
                num-=self.item_counts[item]
                self.item_counts[item]=0
            else:
                self.item_count[item]-=num
                num=0
                break

        return offer_amount

    def get_total_cost(self, item_counts):
        price_list={A:50, B:30, C:20, D:15, E:40, F:10, G:20, H:10, I:35, J:60, K:70, L:90, M:15, N:40, O:10, P:50, Q:30, R:50, S:20, T:20, U:40, V:50, W:20, X:17, Y:20, Z:21}
        list1=["B", "M", "Q"]
        list2=["E", "N", "R"]
        required_amounts=[2, 3, 3]
        for item1, item2, required_amount in zip(list1, list2, required_amounts):
            item_counts[item1]=update_items(item_counts, item1, item2, required_amount)

        total_cost=0
        print(f"the number of Es: {item_counts}")

        for item in item_counts.keys():
            if item=="A":
                num_5s=item_counts[item]//5
                num_3s=(item_counts[item]%5)//3
                num_1s=item_counts[item] - (num_5s*5 + num_3s*3)
                total_cost+= num_5s * 200 + num_3s * 130 + num_1s * price_list[item]

            elif item=="B":
                num_2s=item_counts[item]//2
                num_1s=item_counts[item]%2
                total_cost+= num_2s * 45 + num_1s * price_list[item]
            
            elif item=="F":
                total_cost+=item_counts[item]*price_list[item] - (item_counts[item]//3)*price_list[item]

            elif item=="H":
                num_10s=item_counts[item]//10
                num_5s=(item_counts[item]%10)//5
                num_1s=item_counts[item] - (num_10s*10 + num_5s*5)
                total_cost+= num_10s * 80 + num_5s * 45 + num_1s * price_list[item]

            elif item=="K":
                num_2s=item_counts[item]//2
                num_1s=item_counts[item]%2
                total_cost+= num_2s * 120 + num_1s * price_list[item]

            elif item=="P":
                num_5s=item_counts[item]//5
                num_1s=item_counts[item]%5
                total_cost+= num_5s * 200 + num_1s * price_list[item]
            
            elif item=="Q":
                num_3s=item_counts[item]//3
                num_1s=item_counts[item]%3
                total_cost+= num_3s * 80 + num_1s * price_list[item]
            
            elif item=="U":
                total_cost+=item_counts[item]*price_list[item] - (item_counts[item]//4)*price_list[item]
                
            elif item=="V":
                num_3s=item_counts[item]//3
                num_2s=(item_counts[item]%3)//2
                num_1s=item_counts[item] - (num_3s*3 + num_2s*2)
                total_cost+= num_3s * 130 + num_2s * 90 + num_1s * price_list[item]
            else:
                total_cost+=item_counts[item] * price_list[item]

        return total_cost


    def checkout(self, skus):
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

        self.item_counts=Counter(skus)
        total+=self.group_discount_offer()
        total+=self.get_total_cost(item_counts)

        return total





