# Garden advice Python script


# Function for user to choose the season
def request_season(advice):
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
            return advice
        elif season == "2":
            advice += "Protect your plants from frost with covers.\n"
            return advice
        elif season == "0":
            advice += "No advice for this season.\n"
            return advice
        else:
            print("Invalid input. Please enter a value from the menu.")


# Function for user to choose the plant type
def request_plant_type(advice):
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
            return advice
        elif plant_type == "2":
            advice += "Keep an eye out for pests!"
            return advice
        elif plant_type == "0":
            advice += "No advice for this type of plant."
            return advice
        else:
            print("Invalid input. Please enter a value from the menu.")


# Set variable for advice
advice = ""

# Run the functions to request user input and return the updated
# 'advice' variable in each case.
advice = request_season(advice)
advice = request_plant_type(advice)

# Print the generated advice
print(advice)

# TODO: Examples of possible features to add:
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
