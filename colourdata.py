#dataset
color_to_rgb = {
    'red': [255, 0, 0],
    'green': [0, 255, 0],
    'blue': [0, 0, 255],
    'yellow': [255, 255, 0],
    'pink': [255, 192, 203],
    'purple': [128, 0, 128],
    'teal': [0, 63, 52],  # New entry
    'pale green': [127, 255, 127],  # New entry
    'orange': [255, 165, 0],  # New entry
    'dodger blue': [0, 90, 255],  # New entry
    'brown': [165, 42, 42],  # New entry
    'sky blue': [116, 186, 236]  # New entry
}

rgb_to_color = {tuple(v): k for k, v in color_to_rgb.items()}

def find_complement(color_name):
    # Check if the color name exists in the dictionary
    if color_name.lower() in color_to_rgb:
        rgb = color_to_rgb[color_name.lower()]  # Get the RGB value of the color
        complement = [255 - x for x in rgb]  # Subtract each RGB component from 255
        complement_name = rgb_to_color.get(tuple(complement), "Unknown")  # Find the complement color name
        return rgb, complement, complement_name  # Return the RGB, complement, and complement name
    else:
        return None, None, None  # Return None if color not found

# Start the loop
while True:
    # Taking user input during runtime
    color_input = input("Enter a color name (e.g., 'pink', 'blue', etc.): ")
    rgb_value, complement, complement_name = find_complement(color_input)

    if rgb_value:
        # If the color exists in the dictionary, print the formatted output in two lines
        print(f"Given color: '{color_input}', its RGB values: {rgb_value}")
        print(f"The complementing color: '{complement_name}' with RGB values: {complement}")
    else:
        # If the color isn't found, inform the user
        print("Color not found.")

    # Ask the user if they want to try another color or finish
    user_choice = input("Would you like to try another color? Enter 1 to continue or 0 to finish: ")
    if user_choice == "0":
        print("Thank you for using the program! Goodbye.")
        break  # Exit the loop if the user chooses to finish
    elif user_choice != "1":
        print("Invalid input. Exiting program.")
        break  # Exit the loop if the user enters something other than 1 or 0
