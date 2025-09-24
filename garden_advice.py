# Garden advice Python script

# Variable to hold gardening advice
advice = ""

# Season can be entered by user as 1 or 2. Enter 0 for none
while True:
    season = (
        input(
            "Which season would you like advice for?\n"
            "1: Summer\n"
            "2: Winter\n"
            "0: None\n>"
        )
        .strip()
        .lower()
    )
    # Determine advice based on season
    if season == "1":
        advice += "Water your plants regularly and provide some shade.\n"
        break
    elif season == "2":
        advice += "Protect your plants from frost with covers.\n"
        break
    elif season == "0":
        advice += "No advice for this season.\n"
        break
    else:
        print("Invalid input. Please enter a value from the menu.")

# Plant type can be entered by user as 1 or 2.
# There are currently only 2 supported plant types. Enter 0 to skip.
while True:
    plant_type = (
        input(
            "Which plant type would you like advice for?\n"
            "1: flower\n"
            "2: vegetable\n"
            "0: Other\n>"
        )
        .strip()
        .lower()
    )
    # Determine advice based on the plant type
    if plant_type == "1":
        advice += "Use fertiliser to encourage blooms."
        break
    elif plant_type == "2":
        advice += "Keep an eye out for pests!"
        break
    elif plant_type == "0":
        advice += "No advice for this type of plant."
        break
    else:
        print("Invalid input. Please enter a value from the menu.")


# Print the generated advice
print(advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
