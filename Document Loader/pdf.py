from langchain_community.document_loaders import PyPDFLoader

data=PyPDFLoader(r"C:\Users\KIIT\Desktop\RAG Model\Document Loader\Mypdf.pdf")
docs=data.load()

print(docs[30])
