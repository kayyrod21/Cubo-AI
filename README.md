# Cubo AI – IVA Invoice Calculator 🇸🇻🤖

This project is part of the **Cubo AI practical test** and contains a 
Python function to calculate the total invoice amount after applying VAT 
(IVA).

---

## 🧠 Functionality

The function `calculate_total_with_vat()` takes:

- A base amount (before tax)
- An optional VAT percentage (defaults to **21%**)

It returns the total amount including VAT.

---

## 💡 Usage Example

```python
from factura import calculate_total_with_vat

total = calculate_total_with_vat(100)
print(total)  # Output: 121.0

