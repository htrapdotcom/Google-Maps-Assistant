# AI-Powered Google-Maps-Assistant
This mini project demonstrates the creation of an AI assistant using the OpenAI API that can interact with the user to understand location-based queries and automatically open Google Maps with the relevant search. It leverages OpenAI's function calling to connect natural language with a practical tool (Google Maps).

## Features

* **Natural Language Processing:** Understands user requests for locations using OpenAI's language models.
* **Google Maps Integration:** Automatically opens Google Maps in the default web browser with the searched location.
* **Interactive Chat Interface:** Provides a command-line interface for users to interact with the assistant.

## Requirements

* Python 3.6 or higher
* OpenAI Python library (`openai`)
* An OpenAI API key

## Setup

1.  **Install Python:** Ensure you have Python 3.6 or a later version installed on your system.
2.  **Install the OpenAI library:**
    ```bash
    pip install openai
    ```
3.  **Obtain an OpenAI API key:** You'll need an API key from OpenAI.  Visit the OpenAI website to create an account and get your API key.
4.  **Replace API key in the script:** Open the `agent2.py` file and replace the placeholder with your actual OpenAI API key:
    ```python
    openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your key
    ```

## Usage

1.  **Run the script:**
    ```bash
    python agent2.py
    ```
2.  **Interact with the assistant:** Type your location-based queries in the command line. For example:
    * "Show me the nearest coffee shops"
    * "Find restaurants in New York City"
    * "Directions to the Eiffel Tower"
3.  **Exit:** Type "exit" to end the conversation.

## Code Explanation

* `agent2.py`:  The main Python script that handles user input, communicates with the OpenAI API, and opens Google Maps.
* The script defines a function `open_google_maps()` to open Google Maps with a given query using the `webbrowser` module.
* OpenAI's function calling is used to tell the model that `open_google_maps` is available as a tool.
* The script creates an OpenAI Assistant and a Thread to manage the conversation.
* The script enters a loop to continuously:
    * Get user input.
    * Send the input to the OpenAI Assistant.
    * Handle the Assistant's response, including calling the `open_google_maps` function if necessary.
    * Display the Assistant's responses to the user.

## Limitations

* This is a basic example and might not handle complex or ambiguous queries perfectly.
* Error handling is minimal.
* Requires an active internet connection and a valid OpenAI API key.

## Future Enhancements

* Improve error handling and input validation.
* Add support for more complex queries and follow-up questions.
* Implement a more user-friendly interface (e.g., a web interface).
* Incorporate additional tools or functions beyond Google Maps.

## Author

Parth

## License

MIT License
