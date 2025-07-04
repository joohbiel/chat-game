# 🧪 Guia Completo de Testes - Chat Game

## 📋 **Pré-requisitos para Testes**

1. **Ambiente Virtual Ativo:**
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

2. **Dependências Instaladas:**
```bash
pip install -r requirements.txt
```

## 🎯 **Métodos de Teste**

### **1. Teste Individual dos Jogos**

#### **Teste do Jokenpô:**
```bash
python src/games/jokenpo.py
```
**Resultado esperado:** Teste automático com 4 cenários (pedra, papel, tesoura, entrada inválida)

#### **Teste da Forca:**
```bash
python src/games/forca.py
```
**Resultado esperado:** Simulação de jogo com tentativas de letras

#### **Teste da Adivinhação:**
```bash
python src/games/adivinhacao.py
```
**Resultado esperado:** Simulação de tentativas de números

### **2. Teste do Servidor Flask**

#### **Iniciar o Servidor:**
```bash
python src/main.py
```
**Resultado esperado:**
```
* Serving Flask app 'main'
* Debug mode: on
* Running on http://127.0.0.1:5000
```

#### **Teste da Página Inicial:**
- Abra o navegador em: `http://127.0.0.1:5000`
- **Resultado esperado:** "Olá, mundo! Este é o seu chatbot de jogos!"

### **3. Teste Automatizado Completo**

#### **Executar Script de Teste:**
```bash
python test_webhook.py
```

**Cenários testados automaticamente:**
1. ✅ Comando "oi" - Menu principal
2. ✅ Escolha "1" - Iniciar Jokenpô
3. ✅ Jogada "pedra" - Rodada de Jokenpô
4. ✅ Comando "menu" - Voltar ao menu
5. ✅ Escolha "2" - Iniciar Forca
6. ✅ Tentativa "a" - Letra no jogo da Forca
7. ✅ Tentativa "e" - Outra letra na Forca
8. ✅ Comando "menu" - Voltar ao menu
9. ✅ Escolha "3" - Iniciar Adivinhação
10. ✅ Tentativa "50" - Número na Adivinhação
11. ✅ Tentativa "25" - Outro número na Adivinhação

### **4. Teste Manual com Postman/Insomnia**

#### **Endpoint de Teste:**
- **URL:** `POST http://127.0.0.1:5000/webhook`
- **Headers:** `Content-Type: application/json`

#### **Exemplos de Payloads:**

**Menu Principal:**
```json
{
    "from": "5511999999999",
    "text": "oi"
}
```

**Iniciar Jokenpô:**
```json
{
    "from": "5511999999999",
    "text": "1"
}
```

**Jogar Jokenpô:**
```json
{
    "from": "5511999999999",
    "text": "pedra"
}
```

**Iniciar Forca:**
```json
{
    "from": "5511999999999",
    "text": "2"
}
```

**Tentar letra na Forca:**
```json
{
    "from": "5511999999999",
    "text": "a"
}
```

### **5. Teste de Casos Extremos**

#### **Entradas Inválidas:**
```bash
# Teste com comando inexistente
curl -X POST http://127.0.0.1:5000/webhook \
  -H "Content-Type: application/json" \
  -d '{"from": "5511999999999", "text": "comando_inexistente"}'

# Teste com entrada vazia
curl -X POST http://127.0.0.1:5000/webhook \
  -H "Content-Type: application/json" \
  -d '{"from": "5511999999999", "text": ""}'

# Teste sem campo "text"
curl -X POST http://127.0.0.1:5000/webhook \
  -H "Content-Type: application/json" \
  -d '{"from": "5511999999999"}'
```

## ✅ **Checklist de Validação**

### **Funcionalidades Básicas:**
- [ ] Servidor inicia sem erros
- [ ] Página inicial acessível
- [ ] Webhook responde com status 200
- [ ] Menu principal exibe opções corretas

### **Jogo Jokenpô:**
- [ ] Aceita "pedra", "papel", "tesoura"
- [ ] Rejeita entradas inválidas
- [ ] Retorna resultado da partida
- [ ] Mostra escolha do bot

### **Jogo Forca:**
- [ ] Inicia com palavra oculta
- [ ] Aceita letras individuais
- [ ] Atualiza palavra conforme acertos
- [ ] Conta vidas/tentativas incorretas
- [ ] Detecta vitória/derrota

### **Jogo Adivinhação:**
- [ ] Gera número secreto
- [ ] Aceita números válidos
- [ ] Fornece dicas (maior/menor)
- [ ] Conta tentativas restantes
- [ ] Detecta vitória/derrota

### **Navegação:**
- [ ] Comando "menu" funciona em qualquer momento
- [ ] Estados dos jogos são mantidos por usuário
- [ ] Troca entre jogos funciona corretamente

## 🐛 **Resolução de Problemas Comuns**

### **Erro: "ModuleNotFoundError"**
- **Solução:** Certifique-se de estar no diretório raiz do projeto

### **Erro: "Address already in use"**
- **Solução:** Pare outros servidores na porta 5000 ou mude a porta

### **Erro: "Connection refused"**
- **Solução:** Verifique se o servidor Flask está rodando

### **Respostas inesperadas:**
- **Solução:** Verifique os logs do console do Flask para debug

## 📊 **Métricas de Sucesso**

- ✅ **100%** dos testes automáticos passando
- ✅ **0** erros de sintaxe ou importação
- ✅ **3** jogos completamente funcionais
- ✅ **Navegação** fluida entre jogos
- ✅ **Estados** mantidos corretamente por usuário

## 🚀 **Próximos Passos**

Após validar todos os testes:
1. Deploy em servidor de produção
2. Integração com API real do WhatsApp
3. Implementação de novos jogos
4. Persistência de dados dos usuários
5. Analytics e métricas de uso
