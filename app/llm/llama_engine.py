import ollama
MODEL = "llama3"

def ask_llama(prompt:str):
 response =ollama.chat(
  model=MODEL,
  messages = [
   {"role": "user", "content": prompt}
  ]
 )
 return response["message"]["content"]