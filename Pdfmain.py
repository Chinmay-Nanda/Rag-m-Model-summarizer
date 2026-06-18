from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()

data=PyPDFLoader(r"C:\Users\KIIT\Desktop\RAG Model\Document Loader\Mypdf.pdf")
docs=data.load()

template=ChatPromptTemplate.from_messages(
    [("system","Yor are a helpful assistance that summarizes the pdf"),
     ("human","{data}")]
)

model=ChatMistralAI(model="mistral-small-2506")
prompt=template.format_messages(data=docs[20].page_content) # only page 20 becuase full pdf sending will be out of range 

result=model.invoke(prompt)
print(result.content)
