from userinpu import userinput
# from brow import brow
from analyzor import analyzor
import random

try:
    # feature 1
    #get userinput instance
    userinputs = userinput()
    # get budget input
    budget = userinputs.get_budget()
    # get shoplist input
    # {'apple':['sad','dw'],'sad':['sad','fre']}
    user_dict = userinputs.get_shoplist()

    # feature 2
    # fake price_list
    search_lists = []
    print('pretending searching online.......... ')
    price_item_list =[]
    # get random price and product list, fake data provided due to no pop-up windows allowed
    # price_list: [{'11':'sfsdfs','22':'dsfsdf'},{'33':'fsdfs','33':'fsdf}]
    for i, keywords in user_dict.items():
        item = {}
        for j in keywords:
            ke = random.randint(1,100)
            item[ke] = i+j
        price_item_list.append(item)
    
    # feature 3
    # match budget and total possible cost for products on shoplist
    analyze = analyzor(budget, price_item_list)
    c = analyze.price_budget_match()
    # show results in terminal, no file writing in disks for security reason
    for i in c:
        for price, items in i.items():
            print('total price', price, 'items and their price', items)
# user exit error handling
except KeyboardInterrupt:
    print('exit')
except TypeError:
    print('exit')
except ValueError:
    print('exit')
# program execution finalize
finally:
    print('end of listing, leaving')