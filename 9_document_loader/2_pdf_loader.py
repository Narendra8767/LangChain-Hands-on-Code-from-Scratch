from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r'C:\Users\narendra tekale\Langchain_campusx\9_document_loader\dl-curriculum.pdf')

docs = loader.load()

print(len(docs))

print(docs[0].page_content)