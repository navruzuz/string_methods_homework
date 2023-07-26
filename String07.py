def main(s):
    """
    A variable of type str is given. Check that it consists of letters only.
    Args:
        s: str
    Returns:
        bool: answer
    """
    s='python1'
    return s.isalpha()
print(main('python1'))