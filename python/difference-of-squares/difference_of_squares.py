from numpy import arange

def square_of_sum(count):
    """Sum of natural numbers up to count, squared

    Parameters
    ------------
    count: int
        Nth nautral number

    Returns
    ------------
    int: Sum of natural numbers up to count, squared

    """
    return arange(0,count+1).sum()**2

def sum_of_squares(count):
    """ Sum of squared natural number up to count.

    Parameters
    ------------
    count: int
        Nth nautral number

    Returns
    ------------
    int: Sum of squared natural number up to count
    """
    return (arange(0,count+1)**2).sum()


def difference(count):
    """ Difference between the square of the sum and the sum of the squares of the first N natural numbers.

    Parameters
    ------------
    count: int
        Nth nautral number

    Returns
    -----------
    int:
        Difference between the square of the sum and
        the sum of the squares of the first N natural numbers.

    """

    return square_of_sum(count) - sum_of_squares(count)
