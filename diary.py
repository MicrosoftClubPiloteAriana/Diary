import json
import getpass
from datetime import datetime

# File paths
users_file = "users.json"
diary_folder = "diaries"

# Function to load user data
def load_users():
    try:
        with open(users_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save user data
def save_users(users_data):
    with open(users_file, "w") as file:
        json.dump(users_data, file, indent=2)

# Function to create a new user
def create_user(username, password):
    users_data = load_users()
    if username not in users_data:
        users_data[username] = {"password": password, "diary": {}}
        save_users(users_data)
        return True
    else:
        return False

# Function to login
def login(username, password):
    users_data = load_users()
    if username in users_data and users_data[username]["password"] == password:
        return users_data[username]
    else:
        return None

# Function to save diary entry
def save_entry(username, title, content):
    users_data = load_users()
    user_data = users_data.get(username, {"password": "", "diary": {}})
    user_diary = user_data["diary"]
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user_diary[date] = {"title": title, "content": content}
    users_data[username] = user_data
    save_users(users_data)
    return True

# Function to search for entries
def search_entries(username, query):
    user_data = load_users().get(username)
    if user_data:
        user_diary = user_data["diary"]
        
        # Filter entries based on title or date matching the query
        results = [
            (date, entry["title"], entry["content"])
            for date, entry in user_diary.items()
            if query.lower() in entry["title"].lower() or query in date
        ]
        
        return results
    else:
        return []

# Function to display all entries
def display_entries(username):
    user_data = load_users().get(username)
    if user_data:
        user_diary = user_data["diary"]
        return [(date, entry["title"]) for date, entry in user_diary.items()]
    else:
        return []

# Function to edit an entry
def edit_entry(username, query):
    users_data = load_users()
    if username in users_data:
        user_diary = users_data[username]["diary"]

        # Filter entries based on title or date matching the query
        matching_entries = [
            (date, entry)
            for date, entry in user_diary.items()
            if query.lower() in entry["title"].lower() or query in date
        ]

        if matching_entries:
            print("Matching entries:")
            for idx, (date, entry) in enumerate(matching_entries, start=1):
                print(f"{idx}. Date: {date}\n   Title: {entry['title']}\n   Content: {entry['content']}")

            choice = input("Select the entry to edit (1, 2, etc.): ")
            try:
                selected_entry = matching_entries[int(choice) - 1]
                date_to_edit, entry_to_edit = selected_entry

                edit_option = input("Enter 'title' or 'content' to edit: ")
                if edit_option.lower() == "title" or edit_option.lower() == "content":
                    new_value = input(f"Enter new {edit_option}: ")

                    if edit_option.lower() == "title":
                        entry_to_edit["title"] = new_value
                    elif edit_option.lower() == "content":
                        entry_to_edit["content"] = new_value

                    save_users(users_data)  # Update the user data without reloading
                    return True
                else:
                    print("Invalid edit option. Please choose 'title' or 'content'.")
            except (ValueError, IndexError):
                print("Invalid selection. Please enter a valid number.")
        else:
            print("No matching entries found.")

    return False

# Function to get user input securely
def get_secure_input(prompt):
    return getpass.getpass(prompt)

# Command-line interface
while True:
    print("\n1. Create User\n2. Login\n3. Exit")
    choice = input("Select an option (1/2/3): ")

    if choice == "1":
        username = input("Enter a username: ")
        password = get_secure_input("Enter a password: ")
        if create_user(username, password):
            print("User created successfully.")
        else:
            print("Username already exists. Please choose a different one.")

    elif choice == "2":
        username = input("Enter your username: ")
        password = get_secure_input("Enter your password: ")
        user_session = login(username, password)
        if user_session:
            print(f"Welcome, {username}!")
            
            while True:
                print("\n1. Add Entry\n2. Search Entries\n3. Display All Entries\n4. Edit Entry\n5. Logout")
                user_choice = input("Select an option (1/2/3/4/5): ")

                if user_choice == "1":
                    title = input("Enter entry title: ")
                    content = input("Enter entry content: ")
                    save_entry(username, title, content)
                    print("Entry saved successfully.")

                elif user_choice == "2":
                    query = input("Enter search query (title or date): ")
                    search_results = search_entries(username, query)
                
                    if search_results:
                        print("Search results:")
                        for idx, (date, title, content) in enumerate(search_results, start=1):
                            print(f"{idx}. Date: {date}\n   Title: {title}\n   Content: {content}")
                    else:
                        print("No matching entries found.")

                elif user_choice == "3":
                    display_results = display_entries(username)
                    if display_results:
                        print("All Entries:")
                        for date, title in display_results:
                            print(f"{date} - {title}")
                    else:
                        print("No entries to display.")

                elif user_choice == "4":
                    query = input("Enter search query (title or date): ")
                    if edit_entry(username, query):
                        print("Entry edited successfully.")
                    else:
                        print("Error editing entry. Please try again.")


                elif user_choice == "5":
                    break

        else:
            print("Invalid username or password. Please try again.")

    elif choice == "3":
        break

    else:
        print("Invalid choice. Please enter a valid option.")
        