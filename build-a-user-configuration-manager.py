
def add_setting(settings: dict, new_setting_tuple: tuple) -> str:
    key = str(new_setting_tuple[0]).lower()
    value = str(new_setting_tuple[1]).lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings: dict, updated_setting_tuple: tuple) -> str:
    key = str(updated_setting_tuple[0]).lower()
    value = str(updated_setting_tuple[1]).lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings: dict, key: str) -> str:
    key = str(key).lower()

    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(settings: dict) -> str:
    if not settings:
        return "No settings available."
    else:
        output = "Current User Settings:"
        for key, value in settings.items():
            capitalized_key = key.capitalize()
            output += f"\n{capitalized_key}: {value}"
        return output + "\n"

test_settings = {
    "theme": "light",
    "language": "english",
    "notifications": "enabled"
}

# ---------TESTING---------
print("--- Predefined Initial State ---")
print(view_settings(test_settings))

print("\n--- Attempting to Add an Existing Setting ---")
print(add_setting(test_settings, ("theme", "dark")))

print("\n--- Current Settings After Add Failure ---")
print(view_settings(test_settings))

print("\n--- Updating Settings ---")
print(update_setting(test_settings, ("THEME", "DARK")))
print(update_setting(test_settings, ("language", "spanish")))

print("\n--- Attempting to Update a Non-Existing Setting ---")
print(update_setting(test_settings, ("volume", "low")))

print("\n--- Current Settings After Updates ---")
print(view_settings(test_settings))

print("\n--- Deleting Settings ---")
print(delete_setting(test_settings, "notifications"))
print(delete_setting(test_settings, "LANGUAGE"))

print("\n--- Attempting to Delete a Non-Existing Setting ---")
print(delete_setting(test_settings, "VOLUME"))

print("\n--- Final Settings State (One setting remains: theme) ---")
print(view_settings(test_settings))
