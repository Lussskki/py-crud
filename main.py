import json
import os

# Function to load data from the JSON file
def load_data():
    file_path = os.path.join("db", "db.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
        return data
    else:
        return {}

# Function to save data to the JSON file
def save_data(data):
    file_path = os.path.join("db", "db.json")
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)

# Function to add a new record
def add_record(name, email):
    data = load_data()
    new_id = max(data.get("users", []), key=lambda x: x.get("id", 0)).get("id", 0) + 1
    new_user = {"id": new_id, "name": name, "email": email}
    data.setdefault("users", []).append(new_user)
    save_data(data)

# Function to update a record by ID
def update_record(user_id, new_name, new_email):
    data = load_data()
    users = data.get("users", [])
    for user in users:
        if user["id"] == user_id:
            user["name"] = new_name
            user["email"] = new_email
            break
    save_data(data)

# Function to delete a record by ID
def delete_record(user_id):
    data = load_data()
    users = data.get("users", [])
    data["users"] = [user for user in users if user["id"] != user_id]
    save_data(data)

# Example usage
add_record("John Doe", "john@example.com")
update_record(1, "Updated John Doe", "updated_john@example.com")
delete_record(1)
