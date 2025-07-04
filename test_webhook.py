#!/usr/bin/env python3
# test_webhook.py - Script para testar o webhook localmente

import requests
import json

# URL do webhook local
webhook_url = "http://127.0.0.1:5000/webhook"

def test_webhook(message, user_number="5511999999999"):
    """Testa o webhook enviando uma mensagem simulada"""
    data = {
        "from": user_number,
        "text": message
    }
    
    try:
        response = requests.post(webhook_url, json=data)
        print(f"\n--- TESTE: '{message}' ---")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        print("-" * 50)
        return response.json()
    except requests.exceptions.ConnectionError:
        print(f"Erro: Não foi possível conectar ao servidor. Certifique-se de que o Flask está rodando em {webhook_url}")
        return None
    except Exception as e:
        print(f"Erro: {e}")
        return None

if __name__ == "__main__":
    print("=== TESTE DO WEBHOOK ===")
    
    # Teste do menu
    test_webhook("oi")
    
    # Teste do Jokenpo
    test_webhook("1")
    test_webhook("pedra")
    
    # Teste da Forca
    test_webhook("menu")
    test_webhook("2")
    test_webhook("a")
    test_webhook("e")
    
    # Teste da Adivinhação
    test_webhook("menu")
    test_webhook("3")
    test_webhook("50")
    test_webhook("25")
