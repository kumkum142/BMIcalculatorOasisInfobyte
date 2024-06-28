print("\n\n")
print("\t\tBMI Calculator\n\n")


def calculate_bmi(weight, height, system='metric'):
    """
    Calculate BMI (Body Mass Index) given weight and height.
    
    Parameters:
    - weight: float, weight in kilograms (if metric) or pounds (if imperial)
    - height: float, height in meters (if metric) or inches (if imperial)
    - system: str, either 'metric' or 'imperial' (default is 'metric')
    
    Returns:
    - float, BMI value
    """
    if system == 'imperial':
        bmi = (weight * 703) / (height ** 2)
    else:  # assuming metric
        bmi = weight / (height ** 2)
    
    return bmi

def interpret_bmi(bmi):
    """
    Interpret BMI value into a category.
    
    Parameters:
    - bmi: float, BMI value
    
    Returns:
    - str, interpretation of BMI category
    """
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 25:
        return 'Normal weight'
    elif 25 <= bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

def main():
    print("Welcome to BMI Calculator!\n")
    print("Please select your preferred system:")
    print("1. Metric (kg, meters)")
    print("2. Imperial (pounds, inches)\n")
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        weight = float(input("\nEnter your weight in kilograms: "))
        height = float(input("\nEnter your height in meters: "))
        bmi = calculate_bmi(weight, height, 'metric')
    elif choice == '2':
        weight = float(input("\nEnter your weight in pounds: "))
        height = float(input("\nEnter your height in inches: "))
        bmi = calculate_bmi(weight, height, 'imperial')
    else:
        print("\nInvalid choice. Please enter either 1 or 2.\n")
        return
    
    bmi_category = interpret_bmi(bmi)
    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"You are in the '{bmi_category}' category.")

if __name__ == "__main__":
    main()


print("\n\n")