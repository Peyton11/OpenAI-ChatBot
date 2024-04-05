# ChatBot.py
# Implemenation for ChatBot class

from openai import OpenAI

class ChatBot:

    # Initialize object with parameters. Prompt will be initialized from user input.
    def __init__(self, client, model, temperature, max_tokens, system_message):
        self.client = client
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.system_message = system_message

        self.prompt = ""
        self.messages = [
            {"role": "system", "content": self.system_message},
            {"role": "system", "content": self.prompt}
        ]

    # Sets the prompt
    def set_prompt(self, prompt):
        self.prompt = prompt

    # Returns the AI's response after the prompt
    def get_summary(self):
        completion = self.client.chat.completions.create(
            model = self.model,
            messages = self.messages,
            temperature = self.temperature,
            max_tokens = self.max_tokens,
        )
        return completion.choices[0].message.content
