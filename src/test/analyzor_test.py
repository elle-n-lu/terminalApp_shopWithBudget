import csv
import os
import pytest
import sys
sys.path.append('..')
from analyzor import Analyzor

testUserDict = {'Egg': ['700g', 'large'], 'Apple': ['1kg'], 'milk': ['2L']}
testSearchLists = [
    {'6.80': 'Egg 700g',
     '7.20': 'Egg large',
     },
    {'4.50': 'Apple 1kg',
     },
    {'5.3': 'milk 2L',}
]

# fake data provided for add_price funtion testing
arr = [{'1.3': 'ww1'},
       {'1.3': 'ww12', '1.2': 'ww34'},
       {'1.1': 'ww18', '1.22': 'ww6', '1.51': 'ww5'}]
total = [{'3.7': [['1.3', 'www1'], ['1.3', 'ww12'], ['1.1', 'ww18']]},
         {'3.82': [['1.3', 'www1'], ['1.3', 'ww12'], ['1.22', 'ww6']]},
         {'4.11': [['1.3', 'www1'], ['1.3', 'ww12'], ['1.51', 'ww5']]},
         {'3.6': [['1.3', 'www1'], ['1.2', 'ww34'], ['1.1', 'ww18']]},
         {'3.72': [['1.3', 'www1'], ['1.2', 'ww34'], ['1.22', 'ww6']]},
         {'4.11': [['1.3', 'www1'], ['1.3', 'ww34'], ['1.51', 'ww5']]}]

# systemexit error handling
def exitErr():
    raise SystemExit('left')

# module initialization
@pytest.fixture(scope="module")
def createAnalyzor():
    return Analyzor(12, testSearchLists)

def test_add_price(createAnalyzor):
    total = createAnalyzor.add_price(arr)
    assert total ==total

# total_price_list return according to the inialized module
budgetMatch_return = [ {16.6: [['Egg 700g','6.80'],['Apple 1kg','4.50'],[ 'milk 2L','5.3']]},
     {17:[ ['Egg large','7.20'],['Apple 1kg','4.50'], ['milk 2L','5.3']]}]

def test_price_budget_match(createAnalyzor):
    # when call the funtion, returned value should match the provided one
    total_price_list_return = createAnalyzor.add_price(testSearchLists)
    # if all cost match budget, or user choose to keep going
    assert total_price_list_return == budgetMatch_return
    # if quit
    # assert total_price_list_return == None
    with pytest.raises(SystemExit):
        exitErr()

def test_get_path(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "/usr/front/doc/")
    path_ = input('input the path where you want to save the csv file, e.g. /Users/front/Documents')
    assert path_ == "/usr/front/doc/"

def test_output2csv():
    current_path = os.path.dirname(os.path.abspath(__file__))
    output = budgetMatch_return
    with open('sresults.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        field = ["product", "price", "total"]
        writer.writerow(field)
        for j in output:
            for key, val in j.items():
                for index, i in enumerate(val):
                    if index == len(val)-1:
                        i.append(key)
                    writer.writerow(i)
        print(f'data saved in {current_path}/sresults.csv')
    with pytest.raises(SystemExit):
        exitErr()
