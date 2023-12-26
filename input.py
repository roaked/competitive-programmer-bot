import requests

api_token = 'YOUR_API_TOKEN'

headers = {
    'Authorization': f'Bearer {api_token}'
}

def fetch_problems_with_details():
    url = 'https://leetcode.com/api/problems/all/'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        problems = response.json()['stat_status_pairs']

        for problem in problems:
            title = problem['stat']['question__title']
            category = problem['difficulty']['level'] 
            problem_id = problem['stat']['question_id']

            problem_details_url = f'https://leetcode.com/problemset/{title}/'
            problem_response = requests.get(problem_details_url, headers=headers)
            if problem_response.status_code == 200:
                problem_html = problem_response.text

                print(f"Title: {title}")
                print(f"Category: {category}")
                print(f"Problem ID: {problem_id}")

                print("Parsed Problem Statement: ")
                print("Parsed Input Format: ")
                print("Parsed Output Format: ")
                print("\n")

            else:
                print(f"Failed to fetch details for problem ID: {problem_id}")

    else:
        print("Failed to fetch problems.")

fetch_problems_with_details()
