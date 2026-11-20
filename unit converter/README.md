Unit Converter

A command-line Python program that converts values between common units of length, weight and temperature. It runs as an interactive cli menu, so you can do as many conversions as you like in one session.

Features

- Converts **length**, **weight**, and **temperature**
- Interactive menu that loops until you choose to exit
- Input validation: re-prompts on invalid units and rejects non-numeric values
- Clean, extensible design: adding a new unit takes one line
- Uses only the Python standard library, so there's nothing to install

Supported Units

| Category    | Units                                                                 |
|-------------|-----------------------------------------------------------------------|
| Length      | `m` (meter), `km` (kilometer), `cm` (centimeter), `mi` (mile), `ft` (foot), `in` (inch) |
| Weight      | `kg` (kilogram), `g` (gram), `lb` (pound), `oz` (ounce)               |
| Temperature | `c` (Celsius), `f` (Fahrenheit), `k` (Kelvin)                         |

Unit abbreviations are case-insensitive, so `KM` and `km` both work.

Requirements

- Python 3.6 or newer

Usage

--> clone the repository from github in vs:  ``` git clone https://github.com/drake-gif/mini-projects-python ```
Cd to unit converter folder to access the converter.py

Run the script:

```bash
python converter.py
```

Then follow the prompts: pick a category, enter a value, and choose the units to convert from and to.

Example session

```
--- PYTHON UNIT CONVERTER ---
1. Length (m, km, cm, mi, ft, in)
2. Weight (kg, g, lb, oz)
3. Temperature (c, f, k)
4. Exit
Select a category (1-4): 1
Enter the value to convert: 5
From unit (m, km, cm, mi, ft, in): km
To unit (m, km, cm, mi, ft, in): mi

Result: 5.0 km = 3.107 mi
```