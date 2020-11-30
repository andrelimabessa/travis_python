from .context import string_func

def test_stringLength():
    assert string_func.stringLength("andre") == 5 

def test_stringToLower():
    assert string_func.stringToLower("Andre") == 'andre'

def test_stringToUpper():
    assert string_func.stringToUpper("Andre") == 'ANDRE'

def test_capitalizeString():
    assert string_func.capitalizeString("linus") == 'Linus'
