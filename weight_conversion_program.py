try:
    weight = float(input("Enter your weight: "))
    unit = input("Kilograms (K) or Pound (L)?: ")

    if unit == 'K':
        weight = weight * 2.205
        unit = "Lbs."
        print(f"The result is {round(weight, 1)} {unit}")
    elif unit == 'L':
        weight = weight / 2.205
        unit = "Kgs."
        print(f"The result is {round(weight, 1)} {unit}")
    else:
        print("wtf?")

except ValueError:
    print("wtf?")
    exit()
