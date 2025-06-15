
# 🤖 Bot Rochinha Pé Duro Supremo (2025)

Este é o repositório do **Bot Rochinha Pé Duro**, uma solução de inteligência artificial para geração de sinais automatizados de apostas em futebol, com integração via Telegram, aprendizado contínuo e três modos distintos de operação.

---

## 🔧 Funcionalidades Principais

- ✅ Geração de sinais com base em inteligência artificial
- 📡 Coleta de dados reais via API-Football
- ⚖️ Detecção de valor esperado (EV) usando fair odds
- 🤖 Três modos ativos:
  - `modo_precision` — Foco em precisão e alto EV
  - `modo_fusion` — Equilíbrio entre segurança e volume
  - `modo_laboratorio` — Mercados experimentais com aprendizado contínuo
- 🧠 IA adaptativa com base em erros e acertos
- 📬 Envio automático de sinais para o Telegram
- 📊 Registro de sinais, resultados e ROI em banco de dados

---

## 🚀 Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/rochinha-pe-duro.git
cd rochinha-pe-duro
```

### 2. Configure o `config.json`

Edite o arquivo `config.json` com seu token do bot do Telegram e seu chat_id:

```json
{
  "telegram_token": "SEU_TOKEN",
  "telegram_chat_id": "SEU_CHAT_ID"
}
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute localmente

```bash
python run_scheduler.py
```

### 5. Ou use no Render

- Configure como **Background Worker**
- Build Command: `pip install -r requirements.txt`
- Start Command: `python run_scheduler.py`

---

## 📁 Estrutura do Projeto

- `main.py` / `run_scheduler.py`: entrada principal e agendador
- `core/`: funcionalidades como envio no Telegram, aprendizado e utils
- `modes/`: lógica dos modos de IA (`fusion`, `precision`, `laboratorio`)
- `db/`: banco de dados com sinais e aprendizado
- `config.json`: credenciais do Telegram
- `start.sh`: script opcional para execução

---

## 📊 Exemplos de Sinais

```
[Precision] Sinal com valor: Santos x Flamengo - Resultado + Over 1.5 @ 2.10 (EV 6.5%)
[Fusion] Aposta encontrada: Corinthians x São Paulo - Mais de 2.5 gols @ 1.98
[Lab] Mercado experimental: Palmeiras x Botafogo - Gol após 75 minutos @ 3.00
```

---

## 👤 Autor

Projeto criado por **Eduardo Rocha** – 2025  
Foco: bots inteligentes para apostas esportivas com alta taxa de assertividade.

---

## 🧠 Licença

Uso privado com fins educacionais e de demonstração. Modificações autorizadas mediante crédito ao autor original.
