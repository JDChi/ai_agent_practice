# from langchain.document_loaders import TextLoader
#
# text_loader = TextLoader("../../assets/loader.md")
# result = text_loader.load()
# print(result)

from langchain_community.document_loaders import CSVLoader

csv_loader = CSVLoader("../../assets/loader.csv")
result = csv_loader.load()
print(result)
