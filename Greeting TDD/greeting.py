def greet(name):
    if isinstance(name, str):
        return handle_string(name)

    """
        if name == "":
            return "Hello, my friend"
    
        if name.isupper():
            return f"HELLO, {name}!"

            return f"Hello, {name}."

    else:
        name1 = name[0]
        name2 = name[1]

        return f"Hello, {name1} and {name2}."
"""

def handle_string(the_str):
    if the_str == "":
        return "Hello, my friend."

    if the_str.isupper():
        return f"HELLO, {the_str}!"

    return f"Hello, {the_str}."

def handle_list(the_list):
    name1 = the_list[0]
    name2 = the_list[1]

    return f"Hello, {name1} and {name2}."


#return f"Hello, {name}." if name != "" else "Hello, my friend 
