import os
from userinpu import Userinput
# from brow import brow
from analyzor import Analyzor
import random

try:
    # feature 1
    #get userinput instance
    userinputs = Userinput()
    # get budget input
    budget = userinputs.get_budget()
    # get shoplist input
    # {'apple':['sad','dw'],'sad':['sad','fre']}
    user_dict = userinputs.get_shoplist()

    # feature 2
    print('pretending searching online.......... ')
    price_item_list =[]
    # get random price and product list, fake data provided due to no pop-up windows allowed
    # price_list: [{'11':'sfsdfs','22':'dsfsdf'},{'33':'fsdfs','33':'fsdf}]
    for i, keywords in user_dict.items():
        item = {}
        for j in keywords:
            ke = random.randint(1,100) # produce random fake price
            item[ke] = i+j
        price_item_list.append(item)

    # feature 3
    # match budget and total possible cost for products on shoplist
    analyze = Analyzor(budget, price_item_list)
    c = analyze.price_budget_match()
    # show results in terminal, save in csv file if user choose to save
    choice = input('do you want to save results in csv file? enter y to save; enter to print results')
    if choice =='y':
        current_path = os.path.dirname(os.path.abspath(__file__))
        analyze.output2csv()
    else:
        for i in c:
            for price, items in i.items():
                print('total price', price, 'items and their price', items)
# user exit error handling
except (KeyboardInterrupt, ValueError, TypeError,AttributeError) :
    print('exit')
# program execution finalize
finally:
    print('thank you, bb')