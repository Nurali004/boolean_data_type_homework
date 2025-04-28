def main(a):
    """
    Check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return (a**0.5)**2 ==a

a=int(input("sonni kiriting:"))
print(main(a))