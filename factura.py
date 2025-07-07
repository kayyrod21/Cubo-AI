def calculate_total_with_vat(amount, vat_percentage=21):
    """
    Calculate the total amount after applying VAT (IVA).

    :param amount: Base amount (float or int)
    :param vat_percentage: VAT percentage to apply (default is 21)
    :return: Total amount including VAT
    """
    if amount < 0:
        raise ValueError("Amount must be non-negative")
    if vat_percentage < 0:
        raise ValueError("VAT percentage must be non-negative")

    total = amount + (amount * vat_percentage / 100)
    return round(total, 2)


# Example usage
if __name__ == "__main__":
    base = float(input("Enter base amount: "))
    total = calculate_total_with_vat(base)
    print(f"Total with VAT: {total}")
