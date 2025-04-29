import openai
import json
import webbrowser
import urllib.parse
import time

# Replace with your OpenAI API key
openai.api_key = ["YOUR_OPENAI_API_KEY"]

# Step 1: Define the function
def open_google_maps(query):
    base_url = "https://www.google.com/maps/search/"
    search_url = base_url + urllib.parse.quote_plus(query)
    print(f"Opening: {search_url}")
    webbrowser.open(search_url)

# Step 2: Define tool in OpenAI format
function_definitions = [
    {
        "name": "open_google_maps",
        "description": "Opens Google Maps and searches for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The place to search on Google Maps, like 'Starbucks in Mumbai'"
                }
            },
            "required": ["query"]
        }
    }
]

# Step 3: Create assistant
assistant = openai.beta.assistants.create(
    name="Maps Assistant",
    instructions="You are a helpful assistant that answers location-related queries and opens Google Maps.",
    tools=[{"type": "function", "function": function_definitions[0]}],
    model="gpt-4-1106-preview"
)

# Step 4: Create a thread for the chatbot session
thread = openai.beta.threads.create()

print("Welcome to the AI Maps Assistant! Type 'exit' to quit.")

while True:
    user_input = input("\nYou: ")  # Get user input dynamically

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # Send user message to OpenAI Assistant
    message = openai.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_input
    )

    # Start the assistant run
    run = openai.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id
    )

    # Wait for the assistant response
    while True:
        run_status = openai.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        if run_status.status == "completed":
            break
        elif run_status.status == "requires_action":
            tool_calls = run_status.required_action.submit_tool_outputs.tool_calls
            for tool_call in tool_calls:
                func_name = tool_call.function.name
                arguments = json.loads(tool_call.function.arguments)
                if func_name == "open_google_maps":
                    open_google_maps(arguments["query"])

            # Submit tool output even if nothing to return (needed to finish run)
            openai.beta.threads.runs.submit_tool_outputs(
                thread_id=thread.id,
                run_id=run.id,
                tool_outputs=[
                    {
                        "tool_call_id": tool_calls[0].id,
                        "output": f"Opened Google Maps for {arguments['query']}"
                    }
                ]
            )
            break
        else:
            time.sleep(1)

    # Display assistant response
    messages = openai.beta.threads.messages.list(thread_id=thread.id)
    for msg in messages.data[::-1][:1]:  # Only show the latest message
        print(f"Assistant: {msg.content[0].text.value}")
