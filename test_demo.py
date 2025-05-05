#Немного про модули и их импорт
#import random
import pytest


#my_list=['text', 'one', 'two']
#print(random.choice(my_list))

@pytest.fixture()


def before_after():
    print('Before test') #предусловия
    yield #возврат к выполнению функции  test_demo2
    print('\nAFfter Test ') #постусловия


def test_demo1():
    assert 1==1
def test_demo2(before_after):
    assert 2==3
