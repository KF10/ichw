#!/usr/bin/env python3

"""currency.py:  provide a 'exchange' function which return the 
amount of another currency when you want to convert a certain 
amount of currency to another.

__author__ = "Kuangwenyu"
__pkuid__  = "1800013245"
__email__  = "w.y.kuang@pku.edu.cn"
"""

from urllib.request import urlopen
import json

def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float
    """
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from={0}&to={1}&amt={2}'.
                  format(currency_from, currency_to, amount_from))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    ret_dict = json.loads(jstr) # 将jstr转为字典
    convert = ret_dict['to']
    mylist = convert.split()
    amount_to = float(mylist[0])
    return amount_to

def test_exchange():
    """test the 'exchange' function.
    """
    assert(17.13025 == exchange('USD', 'CNY', 2.5))
    assert(2.1589225 == exchange('USD', 'EUR', 2.5))
    assert(0.018484513053739 == exchange('AOA', 'AUD', 3.7))
    
def test_all():
    """test all cases.
    """
    test_exchange()
    print('All tests passed')
    
def main():
    """main module
    """
    test_all()
    
if __name__ == '__main__':
    main()
