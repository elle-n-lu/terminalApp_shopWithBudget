from os import path
import tkinter.filedialog
import tkinter as tk

class userinput:
    def __init__(self) -> None:
        pass
    # return budget by user input
    def get_budget(self):
        # user input budget
        while True:
            try:
                budget = float(input('print your budget:'))
                return budget
            #error handling
            except ValueError:
                print('please input a number')
        
    # open a window to select file to get path
    def get_path(self):
        # promp choose txt file
        print(
            'the website options are Woolworths and Myer\n'
            'the products unit includes "kg, g, L, ml, each, pack"\n'
            'the typing format of shopping budget, product and amount should look like below in your txt file:\n'
            '\n'
            'apple,1kg\n'
            'skim milk,2L\n'
            'egg,1box\n'
            '\n'
            'choose shooping list txt file'
        )
        # path_ = tkinter.filedialog.askopenfilename()  
       
        # #judge if path exists and if its txt file, or promp to selct again!
        # while len(path_) == 0:
        #         print('no file selected !')
        #         path_ = tkinter.filedialog.askopenfilename()
        # # txt format check
        # while '.txt' not in path_.split('/')[-1]:
        #         print('please choose txtfile !')
        #         path_ = tkinter.filedialog.askopenfilename()
        path_ = input('input the path where the txt file is, e.g. /Users/front/Documents/shoplist.txt    ')
        return path_
    
    # open file and save text in a shoppinglist dict
    # shoplists dict example:{'apple':['1kg', 'gala'], 'skim milk':['2L',' m2'],'lollies':['10pack',' grape']}
    def get_shoplist(self):
        shoplist={}
        #error handling when no file selected
        try:
            with open(self.get_path(), "r") as file1:
                for line in file1:
                    lines = line.strip()
                    product= lines.split(',')[0]
                    amount = lines.split(',')[1:]
                    shoplist[product] = amount
            return shoplist
        #error handling
        except FileNotFoundError:
            print('no file selected !')
    
# cd = use 




