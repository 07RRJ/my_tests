import itertools

def generate_suffixes(length=3):
    """Generates suffixes like 'a', 'b', ..., 'z', 'aa', 'ab', ..., 'zz', 'aaa' up to given length."""
    letters = "abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"
    suffixes = []

    for size in range(1, length + 1):  # From 1-letter to 'length'-letter combinations
        for combo in itertools.product(letters, repeat=size):
            suffixes.append("".join(combo))

    return suffixes

# Generate up to triple-letter suffixes ('aaa'... 'zzz')
suffix_list = generate_suffixes(3)

# Print the first 100 suffixes as an example
print(suffix_list[:100000000000])  