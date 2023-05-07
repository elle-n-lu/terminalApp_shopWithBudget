import pytest
import sys
sys.path.append('..')
from userinpu import userinput

shoplist = {'Egg': ['700g', 'large'],
            'Apple': ['1kg'],
            'milk': ['2L']}

@pytest.fixture(scope='module')
def createUserInpu():
    return userinput()


def test_get_budget( monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "100")
    budget = float(input('print your budget:'))
    assert budget == float('100')

def test_get_shoplist(createUserInpu):
    with open('shopl.txt', "r") as file1:
        file1.read()
        shoplist_return = createUserInpu.get_shoplist()
        assert shoplist_return ==shoplist
