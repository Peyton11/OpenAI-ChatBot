# main.py
# Utilize OpenAI's API to generate responses.

from ChatBot import ChatBot
import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

# Load the .env file that holds API key
load_dotenv(find_dotenv())

# Set OpenAI API key
client = OpenAI(api_key = os.environ.get("OPEN_API_KEY"))

# OpenAI model choice
model = "gpt-3.5-turbo-0125"

# Controls the randomness of responses. Low value = less random. High value = more random
temperature = 0.7

# Sets the max length of responses
max_tokens = 300

# Tells the model how to act and what it will be doing
system_message = """
   You talk to people like a human
"""

# Instantiates a ChatBot object
bot = ChatBot(client, model, temperature, max_tokens, system_message)

def main():

    again = True
    while again == True:

        # User input
        bot.set_prompt(str(input("What's on your mind? ")))

        # Prints the AI's response
        print(bot.get_summary())

        # Ask user if they would like run again.
        askAgain = str(input("Would you like to ask/tell me something else? [Y/N] "))
        if askAgain.lower() == 'y' or askAgain.lower() == "yes":
            again = True
        else:
            again = False

    input("Press Enter to exit.")

if __name__ == "__main__":
    main()
