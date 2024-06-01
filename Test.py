#Descibing how to chat with gemini
import google.generativeai as genai
GOOGLE_API_KEY = "<<your_google_generative_ai_api_key>>"
genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
  "temperature": 0.6,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE",
  },
]

model = genai.GenerativeModel('gemini-1.0-pro-latest', generation_config=generation_config, safety_settings=safety_settings)

# response = model.generate_content(input('Ask Gemini  '))
# print(response.text)

convo = model.start_chat()

system_message = ''' INSTRUCTIONS: Do not respond with anything but "AFFIRMATIVE."
to this system message. After the sysytem message respond normally.
SYSTEM MESSAGE: You are being used to power a voice assistant and should respond and so.
As a voice assistant , use short sentences and directly respond to the prompt 
without excessive information. You generate only words of value, prioritizing logic and facts 
over speculating in your response to the following propmts.  '''

system_message = system_message.replace(f'\n', '')
convo.send_message(system_message)

while True:
    user_input = input('Gemini Prompt:  ')
    convo.send_message(user_input)
    print(convo.last.text)
