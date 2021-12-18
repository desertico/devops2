# content of test_sample.py
def suma(x):
    return x + 1
def resta(x):
    return x - 1
def dividir(x):
    return x / 2
def mult(x):
    return x * 5
def iguales(x):
    return x - 10

def test_answer():
    assert suma(4) == 5
def test_answer2():
    assert resta(10) == 9
def test_answer3():
    assert dividir(4) == 2
def test_answer4():
    assert mult(3) == 15
def test_answer5():
    assert iguales(14) == 4
    
