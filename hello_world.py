#!/usr/bin/env python3
"""
A simple greeting module for the test repository.
这是一个简单的问候模块。
"""


def greet(name="World"):
    """
    Generate a greeting message.
    
    Args:
        name (str): The name to greet. Defaults to "World".
    
    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}! 你好，{name}！"


def farewell(name="World"):
    """
    Generate a farewell message.
    
    Args:
        name (str): The name to say goodbye to. Defaults to "World".
    
    Returns:
        str: A farewell message.
    """
    return f"Goodbye, {name}! 再见，{name}！"


if __name__ == "__main__":
    # Example usage
    print(greet())
    print(greet("Python"))
    print(farewell("Python"))
