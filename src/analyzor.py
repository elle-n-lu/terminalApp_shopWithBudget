import os
import csv


class Analyzor:
    # analyzor object need three params when initialized/created
    def __init__(self, budget, price_list) -> None:
        self.budget = budget
        self.price_list = price_list

    # pure function
    # add each element of 1st list to each ele of 2nd list
    def add_price(self,arr1):
        total = []
        n = len(arr1)
        # if only one item for searching, then all prices for one item put in a list of dict
        if n == 1:
            return [{price: val} for price,val in arr1[0].items()]
        # if more than one item
        else:
            # if two items, then loop two lists, add each price, put relevant price and product name in list.
            for price1, x in arr1[0].items():
                for price2, y in arr1[1].items():
                    total.append({round(float(price1)+float(price2),2): [[x, price1], [y, price2]]})
            # the 'total' list will be applied to next addition loop if more than 2 items
            if n > 2:
                k = 2
                tt = []
                while k < n:
                    for i in total:
                        for price1, x in i.items():
                            for price2, y in arr1[k].items():
                                tt.append(
                                    {round(float(price1)+float(price2),2): x+[[y, price2]]})
                    total = tt
                    tt = []
                    k += 1
        return total
    
    # to find if the total cost of each possibility <= budget, then keep results in list
    # each possibility is a lsit of dict like this:
    # {12.9: [['SOGA', '1.4'], ['SOoden Handle', '2.7'], ['La Extra Large', '2.9'], ['Lemon And Lime wrap iron 6.5cm 4PK', '5.9']]}
    def price_budget_match(self):
        try:
            # search_items = self.search_item_match_records()
            search_items = self.price_list
            total_price_list = self.add_price(search_items)
            total_price_list_copy = total_price_list.copy()
            for i in range(len(total_price_list)-1,-1,-1):
                for key in total_price_list[i]:
                    if float(key)>self.budget:
                        total_price_list.remove(total_price_list[i])
            # budget not enough, let user choose to show the remaining results or quit
            if len(total_price_list) == 0:
                print('budget not enough to buy all products in the list! Try remove some or increase budget!')
                decision = input('check the search results, enter y;To Quit press enter  ')
                if decision != 'y':
                    raise SystemExit('left')
            
            # sort all results by the total cost
            total_price_list = sorted(total_price_list_copy, key= lambda item: list(item)[0])
            # # only return 10 possibility combinations for now
            if len(total_price_list) >10:
                return total_price_list[:10]
            else:
                return total_price_list
        except SystemExit as e:
            print(e)

    # ask user to choose a directory to save results in csv file
    def get_path(self):
        path_ = os.path.dirname(os.path.abspath(__file__))
        return path_

    # each line example:
    # {12.9: [['SOGA', '1.4'], ['SOoden Handle', '2.7'], ['La Extra Large', '2.9'], ['Lemon And Lime wrap iron 6.5cm 4PK', '5.9']]}
    def output2csv(self):
        try:
            output = self.price_budget_match()
            if output == None:
                raise SystemExit('quit program')
            # select folder path to save csv
            else:
                path_ =  self.get_path()
                file_path = os.path.join(path_+'/', 'results.csv')
                
                with open(file_path, 'w', newline='') as file:
                    writer = csv.writer(file)

                    field = ["product", "price", "total"]
                    writer.writerow(field)
                    for j in output:
                        for key, val in j.items():
                            for index, i in enumerate(val):
                                if index == len(val)-1:
                                    i.append(key)
                                writer.writerow(i)
                    print(f'data saved in {file_path}')
        except SystemExit as e:
            print(e)

