"""
fetch_users.py
---------------
A simple Python script to fetch and display user information from a public API.
This script demonstrates GET requests, JSON handling, and basic data iteration in Python.
"""

import requests

def fetch_users():
    """Fetch user data from the given public API and display selected details."""
    url = "https://jsonplaceholder.typicode.com/users"
    
    try:
        # Send GET request
        response = requests.get(url, timeout=10)

        # Check if request was successful
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            return
        
        # Parse JSON response
        users = response.json()

        # Handle empty data
        if not users:
            print("No user data found.")
            return
        
        # Loop through users and display required details
        for i, user in enumerate(users, start=1):
            name = user.get("name", "N/A")
            username = user.get("username", "N/A")
            email = user.get("email", "N/A")
            city = user.get("address", {}).get("city", "N/A")
            
            print(f"User {i}:")
            print(f" Name: {name}")
            print(f" Username: {username}")
            print(f" Email: {email}")
            print(f" City: {city}")
            print("-" * 30)

        # Optional Bonus: Filter users whose city starts with 'S'
        print("\nOptional Bonus\n","-" * 30 ,"\nUsers whose city name starts with 'S':")
        filtered_users = [u for u in users if u.get("address", {}).get("city", "").startswith("S")]
        
        if not filtered_users:
            print("No users found with city name starting with 'S'.")
        else:
            for i, user in enumerate(filtered_users, start=1):
                print(f"User {i}:")
                print(f" Name: {user['name']}")
                print(f" Username: {user['username']}")
                print(f" Email: {user['email']}")
                print(f" City: {user['address']['city']}")
                print("-" * 30)

    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching data: {e}")

if __name__ == "__main__":
    fetch_users()
