import greeting 

def test_greet_name_is_valid():
    assert greeting.greet("Bob") == "Hello, Bob."

def test_greet_name_is_empty():
    assert greeting.greet("") == "Hello, my friend."

def test_greet_two_names():
    assert greeting.greet(["Jill", "Jane"]) == "Hello, Jill and Jane."