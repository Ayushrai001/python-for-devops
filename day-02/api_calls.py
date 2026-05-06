# Import requests library to make HTTP/API calls
import requests

# Import json module to handle JSON data (read/write)
import json

# Import os module to access environment variables (for secure token usage)
import os


# Define function to fetch GitHub repositories using API
def get_repo_using_api():
    
    # Take GitHub username as input from user
    user_name = input("\nEnter the GitHub user name: ")
    
    # Fetch GitHub token from environment variable (secure way)
    token = os.getenv("GITHUB_TOKEN")
    
    # Construct GitHub API URL dynamically using username
    url = f"https://api.github.com/users/{user_name}/repos"
    
    # Define headers for API request
    headers = {
        "Accept": "application/json"   # Specify that we want response in JSON format
    }

    # If token is available, add Authorization header
    if token:
        headers["Authorization"] = f"Bearer {token}"   # Secure authentication

    # Send GET request to GitHub API with headers
    response = requests.get(url, headers=headers)

    # Create empty list to store repository names
    repo_name = []

    # Check if API call was successful (HTTP status code 200)
    if response.status_code == 200:
        
        # Convert API response into Python data (JSON → dict/list)
        data = response.json()

        # Ensure response is a list (valid repo data)
        if isinstance(data, list):
            
            # Loop through each repository object in the list
            for repo in data:
                
                # Extract repository name and append to list
                repo_name.append(repo['name'])
                
                # Print repository name in terminal
                print(repo['name'])
        
        # If response is not a list, print unexpected response
        else:
            print("Unexpected response:", data)

    # If API call failed, print error message with status code
    else:
        print(f"API Error {response.status_code}: {response.text}")
        return   # Exit function if error occurs

    # Open (or create) a file named output.json in write mode
    with open("output.json", "w") as file:
        
        # Write repository names list into JSON file with indentation
        json.dump(repo_name, file, indent=2)


# Call the function to execute the program
get_repo_using_api()
