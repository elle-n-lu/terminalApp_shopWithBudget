from contextlib import contextmanager
import pytest
import sys
sys.path.append('..')
from analyzor import analyzor

testUserDict = {'Egg': ['700g', 'large'], 'Apple': ['1kg'], 'milk': ['2L']}
testSearchLists = [
    {'6.80': 'Manning Valley 18 Large Free Range Eggs 900g',
     '7.20': 'Sunny Queen 12 Extra Large Free Range Eggs 700g',
     '5.7': 'Manning Valley 12 Jumbo Free Range Eggs 800g',
     '7.4': 'Woolworths 12 X-large Free Range Eggs 800g'

     },
    {'4.50': 'Jazz Apple Snackers 1kg Punnet',
     '6.90': 'Macro Mini Organic Apple 1kg',
     '1.1': 'Kanzi Apple Each',
     '3.4': 'Jazz Apple Snackers 1kg Punnet'
     },
    {
        '5.3': 'Macro Organic Oat Milk Unsweetened 1l',
        '5.7': 'Woolworths Evaporated Milk 385ml', '5.95': 'Hunter Belle Full Cream Milk Unhomogenised 2l',
        '5.60': 'Riverina Fresh Lactose Free Full Cream Milk 2l', }
]
searchKeepListReturn = [
    {'6.80': 'Manning Valley 18 Large Free Range Eggs 900g',
     '7.20': 'Sunny Queen 12 Extra Large Free Range Eggs 700g',
     '7.4': 'Woolworths 12 X-large Free Range Eggs 800g'
     },
    {'4.50': 'Jazz Apple Snackers 1kg Punnet',
     '6.90': 'Macro Mini Organic Apple 1kg',
     '3.4': 'Jazz Apple Snackers 1kg Punnet'
     },
    {
        '5.95': 'Hunter Belle Full Cream Milk Unhomogenised 2l',
        '5.60': 'Riverina Fresh Lactose Free Full Cream Milk 2l', }]

searchKeepListReturn2 = [
    {'4.50': 'Jazz Apple Snackers 1kg Punnet',
     '6.90': 'Macro Mini Organic Apple 1kg',
     '3.4': 'Jazz Apple Snackers 1kg Punnet'
     },
    {
        '5.95': 'Hunter Belle Full Cream Milk Unhomogenised 2l',
        '5.60': 'Riverina Fresh Lactose Free Full Cream Milk 2l', }
]

arr = [{'1.3': 'ww1'},
       {'1.3': 'ww12', '1.2': 'ww34'},
       {'1.1': 'ww18', '1.22': 'ww6', '1.51': 'ww5'}]
total = [{'3.7': [['1.3', 'www1'], ['1.3', 'ww12'], ['1.1', 'ww18']]},
         {'3.82': [['1.3', 'www1'], ['1.3', 'ww12'], ['1.22', 'ww6']]},
         {'4.11': [['1.3', 'www1'], ['1.3', 'ww12'], ['1.51', 'ww5']]},
         {'3.6': [['1.3', 'www1'], ['1.2', 'ww34'], ['1.1', 'ww18']]},
         {'3.72': [['1.3', 'www1'], ['1.2', 'ww34'], ['1.22', 'ww6']]},
         {'4.11': [['1.3', 'www1'], ['1.3', 'ww34'], ['1.51', 'ww5']]}]

total_price_list_return = sorted(total, key=lambda item: list(item)[0])


def exitErr():
    raise SystemExit('left')

@pytest.fixture(scope="module")
def createAnalyzor():
    return analyzor(12, testUserDict, testSearchLists)

def test_search_item_match_records(createAnalyzor):
    search_keep_list = createAnalyzor.search_item_match_records()
    assert search_keep_list == search_keep_list
    # if egg item no match, and still return search results,
    # assert search_keep_list == searchKeepListReturn2
    # if quit
    # assert search_keep_list == None
    with pytest.raises(SystemExit):
            exitErr()

def test_add_price(createAnalyzor):
    total = createAnalyzor.add_price(arr)
    assert total ==total


budgetMatch_return = [{17.3: [['Sunny Queen 12 Extra Large Free Range Eggs 700g', '7.20'], ['Jazz Apple Snackers 1kg Punnet', '4.50'], ['Riverina Fresh Lactose Free Full Cream Milk 2l', '5.60']]},
                      {17.5: [['Woolworths 12 X-large Free Range Eggs 800g', '7.4'], ['Jazz Apple Snackers 1kg Punnet',
                                                                                      '4.50'], ['Riverina Fresh Lactose Free Full Cream Milk 2l', '5.60']]},
                      {17.65: [['Sunny Queen 12 Extra Large Free Range Eggs 700g', '7.20'], [
                          'Jazz Apple Snackers 1kg Punnet', '4.50'], ['Hunter Belle Full Cream Milk Unhomogenised 2l', '5.95']]},
                      {17.85: [['Woolworths 12 X-large Free Range Eggs 800g', '7.4'], [
                          'Jazz Apple Snackers 1kg Punnet', '4.50'], ['Hunter Belle Full Cream Milk Unhomogenised 2l', '5.95']]},
                      {19.3: [['Manning Valley 18 Large Free Range Eggs 900g', '6.80'], [
                          'Macro Mini Organic Apple 1kg', '6.90'], ['Riverina Fresh Lactose Free Full Cream Milk 2l', '5.60']]},
                      {19.65: [['Manning Valley 18 Large Free Range Eggs 900g', '6.80'], [
                          'Macro Mini Organic Apple 1kg', '6.90'], ['Hunter Belle Full Cream Milk Unhomogenised 2l', '5.95']]},
                      {19.7: [['Sunny Queen 12 Extra Large Free Range Eggs 700g', '7.20'], [
                          'Macro Mini Organic Apple 1kg', '6.90'], ['Riverina Fresh Lactose Free Full Cream Milk 2l', '5.60']]},
                      {19.9: [['Woolworths 12 X-large Free Range Eggs 800g', '7.4'], ['Macro Mini Organic Apple 1kg',
                                                                                      '6.90'], ['Riverina Fresh Lactose Free Full Cream Milk 2l', '5.60']]},
                      {20.05: [['Sunny Queen 12 Extra Large Free Range Eggs 700g', '7.20'], [
                          'Macro Mini Organic Apple 1kg', '6.90'], ['Hunter Belle Full Cream Milk Unhomogenised 2l', '5.95']]},
                      {20.25: [['Woolworths 12 X-large Free Range Eggs 800g', '7.4'], ['Macro Mini Organic Apple 1kg', '6.90'], ['Hunter Belle Full Cream Milk Unhomogenised 2l', '5.95']]}]

def test_price_budget_match(createAnalyzor):
    total_price_list_return = createAnalyzor.price_budget_match()
    # if all cost match budget, or user choose to keep going
    assert total_price_list_return == budgetMatch_return
    # if quit
    # assert total_price_list_return == None
    with pytest.raises(SystemExit):
        exitErr()

def test_get_path(createAnalyzor):
    createAnalyzor.get_path()

def test_output2csv(createAnalyzor):
    createAnalyzor.output2csv()
    with pytest.raises(SystemExit):
        exitErr()
