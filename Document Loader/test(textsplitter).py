from langchain_community.document_loaders import TextLoader
data=TextLoader(r"C:\Users\KIIT\Desktop\RAG Model\Document Loader\ML.txt")
docs=data.load()
print(docs[0].page_content) # or u can put metadata in plce of page_content. your choice 