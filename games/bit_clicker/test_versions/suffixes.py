import itertools
from decimal import Decimal

def generate_suffixes(length=3):
    """Generates suffixes like 'a', 'b', ..., 'z', 'aa', 'ab', ..., 'zz', 'aaa' up to given length."""
    letters = "abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"
    suffixes = []

    for size in range(1, length + 1):  # From 1-letter to 'length'-letter combinations
        for combo in itertools.product(letters, repeat=size):
            suffixes.append("".join(combo))

    return suffixes

def remove_exponent(d):
    """Remove unnecessary decimals from numbers."""
    return d.quantize(Decimal(1)) if d == d.to_integral() else d.normalize()

def millify(n, precision=2, drop_nulls=True, suffix_length=3):
    """Convert large numbers into a human-readable format with dynamically generated suffixes."""
    
    # Standard suffixes (same as before)
    standard_suffixes = ['', 'K', 'M', 'B', 'T', 'Qa', 'Qi', 'Sx', 'Sp', 'Oc', 'No']
    
    # Dynamically generate more suffixes beyond the standard ones
    extra_suffixes = generate_suffixes(suffix_length)
    
    # Combine both lists (standard + dynamically generated)
    suffixes = standard_suffixes + extra_suffixes

    n = Decimal(n)
    if n < 1000:  # No suffix needed for numbers < 1,000
        return str(n)

    # Determine suffix index (use Decimal.log10() to avoid float issues)
    suffix_index = min(len(suffixes) - 1, int(n.log10() // 3))
    
    # Scale number down
    result = f"{n / (Decimal(10) ** (3 * suffix_index)):.{precision}f}"
    
    # Remove unnecessary decimals (e.g., 1.00M → 1M)
    if drop_nulls:
        result = remove_exponent(Decimal(result))

    return f"{result}{suffixes[suffix_index]}"

# Example Usage:
print(millify(12345678901234567890))  # Should return "12.34Qa"
print(millify(10**300))  # Should return dynamically generated suffixes beyond 'No'
