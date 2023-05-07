from userinpu import userinput
from brow import brow
from analyzor import analyzor


try:
    #get userinput instance
    userinputs = userinput()
    # get budget input
    budget = userinputs.get_budget()
    # get shoplist input
    user_dict = userinputs.get_shoplist()
    search_lists = []
    # search all items in browser
    for item in user_dict:
        browser = brow(item)
        search_lists += browser.get_title_price()
    browser.closewindow()
    analize = analyzor(budget, user_dict, search_lists)
    c = analize.output2csv()
    print('execution end')

finally:
    print('end of listing, leaving')