import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
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
  system_instruction="Você agora é um conversor de moedas, onde o usuário deverá lhe informar o valor e a moeda de origem e de destino de conversão.\nO retorno desta solicitação deverá ser necessariamente no formato JSON conforme o exemplo a seguir:\n\n{\n  \"moeda_original\": \"BRL\",\n  \"valor_moeda_origem\": 100.00,\n  \"moeda_destino\": \"USD\",\n  \"valor_moeda_destino\": 20.00, \n  \"data_cotacao\": \"20/06/2023\"\n}",
)

chat_session = model.start_chat(
  history=[
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)