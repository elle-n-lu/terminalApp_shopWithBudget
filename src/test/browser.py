import pytest
from bs4 import BeautifulSoup
import sys
sys.path.append('..')
from brow import brow

test_item = 'milk'

# initialize the brow module, provide a fake search item 'milk'
@pytest.fixture(scope='module')
def createBrow():
    return brow(test_item)

def test_get_soup_pages(createBrow):
    soup, page = createBrow.get_soup_pages()
    assert type(soup) == BeautifulSoup
    assert type(page) == str
    # assert type(page) == None

def test_get_title_price(createBrow):
    titlericeList_return = createBrow.get_title_price()
    assert type(titlericeList_return) == list
    assert len(titlericeList_return) == 1
    

