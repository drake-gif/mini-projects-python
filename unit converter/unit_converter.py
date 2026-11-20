# Conversion factors relative to base units (meter for length, kilogram for weight)
LENGTH_FACTORS = {
    "m": 1.0,
    "km": 1000.0,
    "cm": 0.01,
    "mi": 1609.34,
    "ft": 0.3048,
    "in": 0.0254,
}

WEIGHT_FACTORS = {
    "kg": 1.0,
    "g": 0.001,
    "lb": 0.453592,
    "oz": 0.0283495,
}

def convert_standard(value, from_unit, to_unit, factors):
    """Converts linear units by converting to a base unit first."""
    base_value = value * factors[from_unit]
    return base_value / factors[to_unit]

def convert_temperature(value, from_unit, to_unit):
    """Handles non-linear temperature formulas."""
    if from_unit == to_unit:
        return value
    
    # Convert input to Celsius first
    if from_unit == "f":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "k":
        celsius = value - 273.15
    else:
        celsius = value

    # Convert from Celsius to target unit
    if to_unit == "f":
        return (celsius * 9 / 5) + 32
    elif to_unit == "k":
        return celsius + 273.15
    return celsius

def get_valid_unit(prompt, valid_units):
    """Prompts the user until a valid unit abbreviation is entered."""
    while True:
        unit = input(prompt).strip().lower()
        if unit in valid_units:
            return unit
        print(f"Invalid unit. Choose from: {', '.join(valid_units)}")

def main():
    while True:
        print("\n--- PYTHON UNIT CONVERTER ---")
        print("1. Length (m, km, cm, mi, ft, in)")
        print("2. Weight (kg, g, lb, oz)")
        print("3. Temperature (c, f, k)")
        print("4. Exit")

        choice = input("Select a category (1-4): ").strip()

        if choice == "4":
            print("Goodbye!")
            break

        if choice not in {"1", "2", "3"}:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            continue

        try:
            value = float(input("Enter the value to convert: "))
        except ValueError:
            print("Invalid number. Please enter a numeric value.")
            continue

        if choice == "1":
            units = list(LENGTH_FACTORS.keys())
            from_u = get_valid_unit(f"From unit ({', '.join(units)}): ", units)
            to_u = get_valid_unit(f"To unit ({', '.join(units)}): ", units)
            result = convert_standard(value, from_u, to_u, LENGTH_FACTORS)
        elif choice == "2":
            units = list(WEIGHT_FACTORS.keys())
            from_u = get_valid_unit(f"From unit ({', '.join(units)}): ", units)
            to_u = get_valid_unit(f"To unit ({', '.join(units)}): ", units)
            result = convert_standard(value, from_u, to_u, WEIGHT_FACTORS)
        elif choice == "3":
            units = ["c", "f", "k"]
            from_u = get_valid_unit("From unit (c, f, k): ", units)
            to_u = get_valid_unit("To unit (c, f, k): ", units)
            result = convert_temperature(value, from_u, to_u)

        print(f"\nResult: {value} {from_u} = {result:.4g} {to_u}")

if __name__ == "__main__":
    main()
