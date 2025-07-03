# src/utils/whatsapp_client.py
import requests

# Este é um client SIMULADO de WhatsApp.
# Em um projeto real, você usaria uma API como Twilio for WhatsApp,
# ou a API Oficial do WhatsApp Business, ou bibliotecas como pywhatkit
# para automação via WhatsApp Web (não recomendado para chatbots robustos).

def send_whatsapp_message(to_number, message_text):
    """
    Simula o envio de uma mensagem para o WhatsApp.
    Em um cenário real, aqui você faria uma requisição para a API do WhatsApp.
    """
    print(f"\n--- SIMULANDO ENVIO PARA {to_number} ---")
    print(f"Mensagem: {message_text}")
    print("-------------------------------------------\n")
    # Para um teste real com pywhatkit (requer WhatsApp Web aberto e logado):
    # import pywhatkit
    # try:
    #     # O número deve incluir o código do país (ex: +5511987654321)
    #     pywhatkit.sendwhatmsg_instantly(to_number, message_text, wait_time=15, tab_close=True)
    #     print("Mensagem enviada com pywhatkit (verifique o WhatsApp Web).")
    # except Exception as e:
    #     print(f"Erro ao enviar com pywhatkit: {e}")
    return {"status": "success", "message": "Mensagem simulada enviada"}