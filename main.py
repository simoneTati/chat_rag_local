import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA

# Carregar variáveis de ambiente (.env)
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Caminho onde os vetores do Chroma serão salvos/carregados
CHROMA_PATH = "./chroma_db"

# 1. Carregar o documento
def carregar_arquivo(caminho):
    if caminho.endswith(".pdf"):
        loader = PyPDFLoader(caminho)
    elif caminho.endswith(".txt"):
        loader = TextLoader(caminho, encoding="utf-8")
    else:
        raise ValueError("Formato não suportado. Use .pdf ou .txt")
    return loader.load()

# 2. Quebrar o conteúdo em pedaços menores
def processar_documento(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_documents(docs)

# 3. Criar ou carregar o banco vetorial com Chroma
def criar_ou_carregar_vetores(docs):
    embeddings = OpenAIEmbeddings(
        model="text-embedding-ada-002",
        api_key=openai_api_key
    )

    # Se o banco vetorial já existe, carrega
    if os.path.exists(CHROMA_PATH):
        return Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)

    # Se não existe, cria a partir dos documentos e persiste automaticamente
    vectordb = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=CHROMA_PATH
    )
    return vectordb

# 4. Iniciar o chatbot
def iniciar_chat(vetores):
    llm = ChatOpenAI(
        model="gpt-4o",
        api_key=openai_api_key,
        temperature=0  # mais objetivo
    )

    qa = RetrievalQA.from_chain_type(llm=llm, retriever=vetores.as_retriever())

    print("\n📚 Pergunte algo sobre o documento. Digite 'sair' para encerrar.")
    while True:
        pergunta = input("\nVocê: ")
        if pergunta.strip().lower() in ["sair", "exit", "quit"]:
            break
        resposta = qa.invoke({"query": pergunta})
        print("Bot:", resposta['result'])

# 5. Função principal
def main():
    caminho = input("Digite o caminho do arquivo (.pdf ou .txt): ").strip()
    docs = carregar_arquivo(caminho)
    partes = processar_documento(docs)
    vetores = criar_ou_carregar_vetores(partes)
    iniciar_chat(vetores)

# Execução
if __name__ == "__main__":
    main()


