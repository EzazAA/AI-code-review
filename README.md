

<h1 align="center"> 🤖 AI Code Review Tool</h1>
<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/python-3.8%2B-00ccff?style=for-the-badge" alt="Python Version">
  </a>
  <a href="https://hacktoberfest.com">
    <img src="https://img.shields.io/badge/Hacktoberfest-🌱%20Active-FF1493?style=for-the-badge" alt="Hacktoberfest">
  </a>
  <img src="https://img.shields.io/github/issues/EzazAA/AI-code-review?style=for-the-badge" alt="Issues">
  <img src="https://img.shields.io/github/forks/EzazAA/AI-code-review?style=for-the-badge" alt="Forks">
</p>

## Overview
The **AI Code Review Tool** is a command-line application that utilizes OpenAI's API to provide intelligent feedback on Python code. This tool assists developers in improving their coding skills by offering constructive suggestions and modifications. Whether you're a beginner seeking to learn or an experienced programmer looking for optimization tips, this tool is designed to enhance your coding experience.

## Features
- 🚀 **Automatic Code Review**: Submit your Python code and receive instant feedback.
- 🛠️ **Code Suggestions**: Get actionable recommendations for improvements and optimizations.
- 🌟 **User-Friendly Interface**: Simple command-line interface for ease of use.
- 📂 **Dynamic File Handling**: Specify any Python file for review by entering its path.

## Table of Contents
- [Installation](#installation)
- [Creating an OpenAI API Key](#creating-an-openai-api-key)
- [Example](#example)
- [Common Use Cases](#common-use-cases)
- [Error Handling](#error-handling)
- [Code of Conduct](#code-of-conduct)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation
To use this application, ensure you have Python 3.x installed on your machine. Follow these steps to get started:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/python-code-review-tool.git
   cd python-code-review-tool


2. **Install required packages**:
   Install the `openai` package using pip:
   ```bash
   pip install openai
   ```

3. **Set your OpenAI API Key**:
   In the `main.py` file, replace `"your.api.key"` with your actual OpenAI API key.

## Creating an OpenAI API Key
To utilize the OpenAI API, you'll need to create an API key. Follow these steps:

1. 🌐 Go to the [OpenAI website](https://platform.openai.com/signup).
2. 📝 Sign up for an account or log in if you already have one.
3. 🔑 Navigate to the **API Keys** section from the dashboard.
4. ➕ Click on the **Create API Key** button.
5. 📋 Copy the generated API key and store it securely, as you’ll need it for your application.

   
## Example
Here’s a brief example of how to use the application:

1. **Run the application**:
   ```bash
   python main.py
   ```

2. **Enter the file path**: When prompted, provide the path to your Python file. For instance:
    ```sh
    Please enter the file location: d:/github/Open_source/AI-code-review/main.py
    ```
    Replace it with the full file path of your code.
    
3. **Feedback from OpenAI**: The tool will analyze the code and output feedback like this:
   ```
   The code you provided seems well-written and efficient.
   However, I noticed that you could use the `f-string` format for better readability.
   ```
## Common Use Cases
1. **Reviewing code for efficiency**: Utilize the tool to identify areas where your code can be optimized for better performance.
    ```sh
    Please enter the file location: inefficient_code.py
    ```
    Output:
    ```
    Feedback from OpenAI:
    The code you provided could be optimized by utilizing a more efficient algorithm. Consider using [Algorithm suggestion] instead of the current approach.
    ```
    
2. **Checking code style**: Ensure your code adheres to best practices and coding conventions for readability and maintainability.
    ```sh
    Please enter the file location: poorly_styled_code.py
    ```
    Output:
    ```
    Feedback from OpenAI:
    The code style could be improved by adhering to PEP 8 guidelines. For example, consider using more descriptive variable names and consistent indentation.
    ```

3. **Analyzing code for error handling**: Evaluate how well your code manages potential exceptions and provides robust error handling.
    ```sh
    Please enter the file location: code_with_error_handling.py
    ```
    Output:
    ```
    Feedback from OpenAI:
    The code has good error-handling practices implemented. You've effectively used try-except blocks to manage potential exceptions.
    ```
4. **Generating test cases**: Ask the tool to suggest appropriate test cases for your code to ensure its functionality and correctness.
    ```sh
    Please enter the file location: my_function.py
    ```
    Output:
    ```
    Feedback from OpenAI:
    Here are some test cases you could consider for your function: [Suggested test cases]
    ```

5. **Debugging code**: Use the tool to identify potential bugs or logical errors in your code.
    ```sh
    Please enter the file location: buggy_code.py
     ```
    Output:
    ```
    Feedback from OpenAI:
    I noticed a potential issue in your code on line [Line number]. Consider [Suggestion for improvement] to address this.
    ```

## Error Handling:
1. **File not found**: If the provided file path is incorrect, you'll see an error message like:
    ```python
    Error: The file 'invalid_path.py' was not found.
    ```
    Make sure to enter the correct path to the file.


2. **API key issues**: If the API key is invalid or missing, you might encounter an error message like:
   ```python
   Invalid API Key provided.
   ```
   Double-check that you have entered the correct API key in the `main.py` file.

3. **Rate limit exceeded**: If you exceed your OpenAI usage limit, you'll get a message:
    ```
    Sorry, you have exceeded your current usage limit. Please visit platform.openai.com to upgrade your plan.
    ```
   You can upgrade your plan or reduce your usage to continue using the tool.

## Code of Conduct
We adhere to a code of conduct that ensures a welcoming environment for all contributors. Please read our [Code of Conduct](CODE_OF_CONDUCT.md) for details on expected behavior and community standards.

## Contributing
We welcome contributions to this project! To contribute, please follow these steps:

1. **Fork the repository**.
2. **Create a new branch** for your feature or bug fix.
3. **Make your changes** and commit them.
4. **Push your changes** to your fork.
5. **Open a pull request** detailing your changes.

Please read our [Contributing Guidelines](CONTRIBUTING.md) for more information.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For questions or inquiries, feel free to reach out to the project maintainer:
- 📧 Email: [ezazalamahmed@gmail.com](mailto:ezazalamhmed@gmail.com)

---

Thank you for using the Python Code Review Tool. Happy coding! 🎉
