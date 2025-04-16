# 🧠 Chat RAG Local com LangChain + OpenAI + Chroma

Este projeto implementa um chatbot com RAG (Retrieval-Augmented Generation) local, que permite conversar com documentos .pdf ou .txt utilizando LangChain, ChromaDB e os modelos da OpenAI.

## 🚀 Funcionalidades

- Faça perguntas sobre qualquer PDF ou TXT
- Vetorização e recuperação de conteúdo com ChromaDB
- Modelos da OpenAI (gpt-4o e text-embedding-ada-002)
- Vetores persistidos em disco (reutilizáveis)
- Suporte a .env para chave segura da API

## 📁 Estrutura do Projeto

chat_rag_local/  
├── chroma_db/             # Vetores armazenados automaticamente pelo Chroma  
├── main.py                # Código principal da aplicação  
├── .env                   # Chave da API OpenAI (não subir para o GitHub!)  
├── requirements.txt       # Dependências do projeto  
├── .gitignore             # Arquivos e pastas ignoradas no Git  
└── README.md              # Este arquivo 😄

## 🛠️ Como rodar o projeto

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/chat_rag_local.git
cd chat_rag_local
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv .venv
.\.venv\Scripts ctivate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure sua chave da OpenAI:  
Crie um arquivo chamado `.env` na raiz do projeto com o seguinte conteúdo:
```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

5. Execute o projeto:
```bash
python main.py
```

Você verá a mensagem:
📚 Pergunte algo sobre o documento. Digite 'sair' para encerrar.

## 🧠 Tecnologias utilizadas

- Python 3.10+
- LangChain
- ChromaDB
- OpenAI API
- dotenv

## 🛡️ Avisos

- Nunca suba sua chave da OpenAI para o GitHub!
- A pasta chroma_db/ está no .gitignore — ela é recriada automaticamente
- Compatível com modelos: gpt-4o, o3-mini, text-embedding-ada-002

## 📬 Contato

Feito com 💜 por Simone Tatiane do Canto  
Projeto para fins de aprendizado com RAG e LangChain
