#!pip3 install openai
#!pip3 install pyttsx3

import openai
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

openai.api_key = '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'
messages = [{"role": "system", "content":
			"You are a intelligent assistant."}]

print('ChatGPT: Hello! How may I help you?')
engine.say('Hello! How may I help you?')
engine.runAndWait()  

while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    engine.say(reply)
    engine.runAndWait()           
    messages.append({"role": "assistant", "content": reply})
