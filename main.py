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
        print(f"Error: The file '{file_name}' was not found. Please check the file path.")
    except PermissionError:
        print(f"Error: Permission denied when trying to read the file '{file_name}'. Check your permissions.")
    except IsADirectoryError:
        print(f"Error: The path '{file_name}' is a directory, not a file. Please provide a valid file path.")
    except UnicodeDecodeError:
        print(f"Error: Encoding error while reading the file '{file_name}'. The file may not be in the correct format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

def main():
    attempts = 3  # Maximum number of attempts to enter a valid file
    while attempts > 0:
        file_name = input("Please enter the file location: ")

        # Get the code from the provided file
        code = get_code(file_name)

        if code:
            try:
                # Get feedback from OpenAI
                feedback = get_code_review(code)
                print("Feedback from OpenAI:\n", feedback)
                break  # Exit the loop after successful processing
            except openai.error.RateLimitError:
                print("Sorry, you have exceeded your current usage limit. Please visit platform.openai.com to upgrade your plan.")
            except Exception as e:
                print(f"An error occurred while getting feedback: {e}")
                break  # Exit on unexpected error
        else:
            print("No code to review. Please try again.")
            attempts -= 1  # Decrease the number of attempts
            if attempts == 0:
                print("Exceeded maximum attempts. Exiting the program.")



if __name__ == "__main__":
    main()
