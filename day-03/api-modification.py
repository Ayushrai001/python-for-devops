import requests

def fetch_user_data(api_url):# Function to fetch user data from the API with error handling
    
    try: #try block to handle potential exceptions during API call
        response = requests.get(api_url, timeout=5) # Send GET request to the API with a timeout of 5 seconds
        response.raise_for_status()  # Check if the request was successful
        return response.json()  # Return the JSON data as a Python dictionary
    
    except requests.exceptions.HTTPError as http_err: # Handle HTTP errors (e.g., 404, 500)
        print(f"HTTP error occurred: {http_err}")
    
    except requests.exceptions.ConnectionError: # Handle connection errors (e.g., network issues)
        print("Connection error occurred. Please check your network connection.")
    
    except requests.exceptions.Timeout: # Handle timeout errors (e.g., server taking too long to respond)
        print("The request timed out. Please try again later.")
    
    except requests.exceptions.RequestException as err: # Handle any other request-related errors
        print(f"An unexpected error occurred: {err}")
    
    return None  # Return None if there was an error

def display_user_data(users): # Function to display user data in a readable format
    if not users: #if statement to check if the users list is empty or None
        print("No user data available.")# Check if the users list is empty or None
        return # Exit the function if there is no user data to display
    print("\nUser Details:\n")# Print header for user details
    
    for user in users: # Loop through each user in the list
        print(f"Name: {user['name']}") # Print user's name
        print(f'"Email: {user["email"]}') # Print user's email
        print(f"City: {user['address']['city']}") # Print user's city from their address

def main(): # Main function to execute the program
    api_url = "https://jsonplaceholder.typicode.com/users" # API endpoint to fetch user data
    users = fetch_user_data(api_url) # Fetch user data from the api_url
    display_user_data(users) # Display the fetched user data

if __name__ == "__main__":# Check if the script is being run directly (not imported as a module)
    main() # Call the main function to run the program
    
    