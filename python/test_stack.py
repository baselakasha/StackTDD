import pytest
from stack import Stack

@pytest.fixture
def my_stack():
    yield Stack()

def test_new_stack_empty(my_stack):
    assert my_stack.isEmpty()

def test_stack_not_empty_after_one_push(my_stack):
    my_stack.push(0)
    assert my_stack.isEmpty() is False

def test_stack_empty_after_one_push_and_one_pull(my_stack):
    my_stack.push(0)  
    my_stack.pull()
    assert my_stack.isEmpty()

def test_stack_not_empty_after_two_pushes_and_one_pull(my_stack):
    my_stack.push(123)
    my_stack.push(999)
    my_stack.pull()
    assert my_stack.isEmpty() is False

def test_pulling_empty_stack_should_throw_error(my_stack):
    with pytest.raises(Stack.UnderFlow):
        my_stack.pull()

def test_one_push_one_pull_should_return_same_element(my_stack):
    my_stack.push("999")
    element = my_stack.pull()
    assert element == "999"

def test_two_pushes_one_pull_should_return_same_element(my_stack):
    my_stack.push(1)
    my_stack.push(9)
    assert my_stack.pull() is 9

def test_two_pushes_two_pulls_should_return_same_element(my_stack):
    my_stack.push(1)
    my_stack.push(9)
    my_stack.pull()
    assert my_stack.pull() is 1