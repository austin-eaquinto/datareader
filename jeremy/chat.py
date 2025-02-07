import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAIL_API_KAY"))

messages = [
    {"role": "system", "content": "You are helping find movies based on the user's requests."}
]

while True:
    print("You")
    user_input = input("> ")
    if user_input.lower() == "quit":
        break

    messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        assistant_response = response.choices[0].message.content
        print("\nAssistant:", assistant_response)

        messages.append({"role": "assistant", "content": assistant_response})

    except Exception as e:
        print(f"\nError: {str(e)}")
    
print("\nChat ended")