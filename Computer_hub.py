import os

import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "What is your best red wine?\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "As a language model, I don't have personal preferences or the ability to taste wine. I can't provide you with a \"best red wine\" recommendation. \n\nTo find the best red wine for you, I need more information:\n\n* **What are your preferred flavors?**  Do you like fruity wines, earthy wines, or something in between? \n* **What's your budget?** Prices for red wines can vary greatly.\n* **What occasion are you buying the wine for?**  A special dinner party might call for a different wine than a casual weeknight meal.\n* **What food will you be pairing the wine with?** Some wines pair better with certain dishes than others.\n\nOnce you provide me with more details, I can help you find a great red wine that you'll love! \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Tell me more about this\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Please provide me with the context you'd like me to elaborate on! I need more information to understand what \"this\" refers to. \n\nFor example, are you referring to:\n\n* **A specific topic?** (e.g., \"Tell me more about the history of the Roman Empire.\")\n* **A previous statement?** (e.g., \"Tell me more about this red wine you mentioned.\")\n* **A concept?** (e.g., \"Tell me more about this theory of relativity.\")\n\nOnce you give me more information, I can provide you with a detailed explanation! 😊 \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Tell me more about it\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Please tell me what \"it\" refers to! I need more context to understand what you're asking about. \n\nFor example, are you referring to:\n\n* **A previous conversation?** (e.g., \"Tell me more about it. What else did you learn about the history of the Roman Empire?\")\n* **A specific topic?** (e.g., \"Tell me more about it. What are the different types of red wine?\")\n* **A concept or idea?** (e.g., \"Tell me more about it. What are the implications of quantum mechanics?\")\n\nThe more context you provide, the better I can understand your request and give you a helpful response. 😊 \n",
      ],
    },
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")