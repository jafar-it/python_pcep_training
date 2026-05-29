# build a temperature conversion module

def celsius_to_fahrenheit(c: float) -> float:
    return c * 9/5 + 32

def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5/9

def celsius_to_kelvin(c: float) -> float:
    return c + 273.15

def kelvin_to_celsius(k: float) -> float:
    if k < 0:
        raise ValueError(f"Kelvin cannot be negative: {k}")
    return k - 273.15

# Conversion routing table
_CONVERSIONS = {
    ("C", "F"): celsius_to_fahrenheit,
    ("F", "C"): fahrenheit_to_celsius,
    ("C", "K"): celsius_to_kelvin,
    ("K", "C"): kelvin_to_celsius,
    ("F", "K"): lambda f: celsius_to_kelvin(fahrenheit_to_celsius(f)),
    ("K", "F"): lambda k: celsius_to_fahrenheit(kelvin_to_celsius(k)),
}

def convert(value: float, from_unit: str, to_unit: str) -> float:
    if from_unit == to_unit:
        return value
    fn = _CONVERSIONS.get((from_unit.upper(), to_unit.upper()))
    if not fn:
        raise ValueError(f"Cannot convert {from_unit} → {to_unit}")
    return round(fn(value), 2)

# Tests
print(convert(100, "C", "F"))     # 212.0
print(convert(212, "F", "C"))     # 100.0
print(convert(0, "K", "C"))       # -273.15
print(convert(373.15, "K", "C"))  # 100.0

try:
    convert(-1, "K", "C")
except ValueError as e:
    print(f"Error: {e}")