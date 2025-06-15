
# 📦 Imagem base com Python
FROM python:3.11-slim

# 🔧 Diretório de trabalho no container
WORKDIR /app

# 🧾 Copia arquivos necessários
COPY . .

# 🐍 Instala dependências
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# 🗃️ Garante que a pasta db existe
RUN mkdir -p db

# ✅ Comando de inicialização
CMD ["bash", "start.sh"]
