import openai

# Set your OpenAI API key
openai.api_key = "your.api.key"

# Ask the user for the file location
file_name = input("Please enter the file location: ")

# Function to get a code review from OpenAI
def get_code_review(code):
    prompt = f"Please review this Python code and provide feedback and modify if needed:\n\n{code}"
    
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",  # Use GPT-3.5
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()

# Function to read and format code from the file
def get_code(file_name):
    try:
        with open(file_name, "r") as f:
            code_list = f.readlines()
        code_list = [line.strip() for line in code_list if line.strip()]  # Remove empty lines
        code = '\n'.join(code_list)  # Join code into a single string with newlines
        return code
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return None

# Get the code from the provided file
code = get_code(file_name)

if code:
    try:
        # Get feedback from OpenAI
        feedback = get_code_review(code)
        print("Feedback from OpenAI:\n", feedback)
    except openai.error.RateLimitError:
        print("Sorry, you have exceeded your current usage limit. Please visit platform.openai.com to upgrade your plan.")
else:
    print("No code to review.")
