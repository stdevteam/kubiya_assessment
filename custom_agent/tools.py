import random


def generate_simple_math_task(query: str) -> str:
    """
    A simple function which will generate a simple math task
    :return: generated task
    """
    signs = ("+", "-", "*", "/")
    return f"\nSolve this: {random.randint(0, 100)} {signs[random.randint(0, len(signs) - 1)]} {random.randint(0, 100)}"
