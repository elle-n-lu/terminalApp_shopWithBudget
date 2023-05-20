import pytest
import sys
sys.path.append('..')
from userinpu import Userinput

shoplist = {'Egg': ['700g', 'large'],
            'Apple': ['1kg'],
            'milk': ['2L']}

# initalize the userinput object, set the scope to be module, so the function following can be called as the attribute of the object 
@pytest.fixture(scope='module')
def createUserInpu():
    return Userinput()


def test_get_budget( monkeypatch):
    # mock user input as 100
    monkeypatch.setattr('builtins.input', lambda _: "100")
    budget = float(input('print your budget:  '))
    assert budget == float('100')

def test_get_shoplist(createUserInpu):
    with open('shopl.txt', "r") as file1:
        file1.read()
        for line in file1:
            lines = line.strip()
            product= lines.split(',')[0]
            amount = lines.split(',')[1:]
            shoplist[product] = amount
    assert shoplist == shoplist
    
