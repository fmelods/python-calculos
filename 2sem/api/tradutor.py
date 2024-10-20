"""
Install the Google AI Python SDK
 
$ pip install google-generativeai
"""
 
import os
import google.generativeai as genai

def tradutor(texto_usuario,lingua_destino):
 
  genai.configure(api_key="AIzaSyCKiQyClOrktiBXtT13oCpI_k_Ygk6ypwg")
  
  # Create the model
  generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
  }
  
  
  texto = input("Entre com as informações: ")
  lingua_destino = input("Entre com a língua de destino: ")
  
  model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    system_instruction='''Você agora é um tradutor de línguas, 
                        onde o usuário deverá lhe informar o texto e a língua de destino,
                        você deverá detectar a língua de origem, 
                        O retorno desta solicitação deverá ser 
                        necessariamente no formato JSON 
                        conforme o exemplo a seguir:
                        {
                            "lingua_origem": "Portugues",
                            "texto_origem": "Olá",
                            "lingua_destino":"Ingles",
                            "texto_destino": "Hi"
                          }
                          observação: não inclua o termo JSON na sáida.
                          '''
  )
  
  chat_session = model.start_chat(
    history=[
      {
        "role": "user",
        "parts": [
          f"{texto}: a língua de destino é :{lingua_destino}",
        ],
      },
    ]
  )
  
  response = chat_session.send_message(texto)
  return response.text
 
import json
texto_retorno = json.loads(response.text)
print(texto_retorno)
print()
print(f"A língua de origem detectada: {texto_retorno['lingua_origem']}") 
print(f"O texto digitado foi: {texto_retorno['texto_origem']}")
print(f"A língua de destino solicitada: {texto_retorno['lingua_destino']}")
print(f"O texto traduzido: {texto_retorno['texto_destino']}")

texto = input("Entre com o texto a ser traduzido: ")
lingua_destino = input("Entre com a língua de destino: ")
texto_retorno = tradutor(texto,lingua_destino)

print (texto_retorno)