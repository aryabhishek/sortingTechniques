def max_pairs(n, a):
    """
    Finds the maximum number of valid (i, j) pairs in the array 'a' of size 'n'.

    A pair (i, j) is valid if the product of LCM(a[i], a[j]) and HCF(a[i], a[j])
    is present in the array 'a'.

    Args:
        n: The size of the array.
        a: The integer array.

    Returns:
        The maximum number of valid pairs.
    """

    count = 0  # Initialize the count of valid pairs
    seen = set(a)  # Create a set for efficient lookups
    n = max(a)
    for i in range(n+1):
        for j in range(n+1):
            # Calculate the product of LCM and HCF, which is simply a[i] * a[j]
            product = i * j
            if product in seen:
                count += 1

    return count


# Example usage:
n = 2 
a = [10, 2]
result = max_pairs(n, a)
print("Maximum valid pairs:", result)