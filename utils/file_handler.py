import json


def save_to_file(tasks, filename):

    try:

        with open(filename, "w") as file:

            json.dump(tasks, file, indent=4)

    except Exception as e:

        print(f"Error saving file: {e}")


def load_from_file(filename):

    try:

        with open(filename, "r") as file:

            return json.load(file)

    except FileNotFoundError:

        return []

    except json.JSONDecodeError:

        return []

    except Exception as e:

        print(f"Error loading file: {e}")

        return []