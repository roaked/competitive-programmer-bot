import requests
from bs4 import BeautifulSoup

# Function to retrieve and parse a problem statement from a hypothetical online source
def retrieve_problem(problem_id):
    # Assuming a hypothetical URL structure where problems are available
    url = f"https://example.com/problems/{problem_id}"
    
    # Send a GET request to fetch the problem page
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find and extract the elements containing problem information
        problem_statement = soup.find('div', class_='problem-statement').get_text()
        input_format = soup.find('div', class_='input-format').get_text()
        output_format = soup.find('div', class_='output-format').get_text()
        
        # Return the parsed problem information
        return {
            "Problem Statement": problem_statement.strip(),
            "Input Format": input_format.strip(),
            "Output Format": output_format.strip()
        }
    else:
        print("Failed to retrieve the problem.")
        return None

# Example: Retrieving and displaying a problem statement for problem ID '123'
problem_info = retrieve_problem('123')

if problem_info:
    print("Problem Statement:")
    print(problem_info["Problem Statement"])
    print("\nInput Format:")
    print(problem_info["Input Format"])
    print("\nOutput Format:")
    print(problem_info["Output Format"])
