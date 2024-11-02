import time
import sys
import apachelabs

# Initialize the client
client = apachelabs.Apache(api_key="ujwvNZjEoG55S2UMQmYzoNKANcBA02pW")

# Initialize an empty list to store conversation history
conversation_history = []

def type_effect(text, delay=0.05):
    """Simulate typing effect by printing one character at a time."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Print a newline after the message

while True:
    user_input = input("You: ")
    
    # Exit the loop if user types '/bye'
    if user_input.strip().lower() == "/bye":
        print("Ending the conversation. Goodbye!")
        break
    
    # Append user message to conversation history
    conversation_history.append({"role": "user", "content": user_input})
    
    # Get model's response
    response = client.messages(
        model="apachelm-v3",
        max_tokens=1024,
        messages=conversation_history
    )
    

    # Check if response is a dictionary or a string
    if isinstance(response, str):
        response_content = response  # If it's a string, use it directly
    else:
        response_content = response['content']  # Adjust according to the response structure

    # Print the response with a typing effect
    type_effect(response_content)
    
    # Append model response to the conversation history
    conversation_history.append({"role": "assistant", "content": response_content})