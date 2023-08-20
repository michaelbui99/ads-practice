from ads_practice.stack import Stack


def test():
    stack = Stack()
    stack.push(5)
    stack.push(7)
    stack.push(9)

    assert stack.pop().unwrap() == 9
    assert stack.size == 2

    stack.push(11)
    assert stack.pop().unwrap() == 11
    assert stack.pop().unwrap() == 7
    assert stack.peek().unwrap() == 5
    assert stack.pop().unwrap() == 5
    assert stack.pop().has_value == False

    stack.push(42)
    assert stack.peek().unwrap() == 42
    assert stack.size == 1
