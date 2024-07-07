from langchain.text_splitter import RecursiveCharacterTextSplitter

with open("../../assets/泡沫.txt") as f:
    content = f.read()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,  # 切分的文本块大小
    chunk_overlap=20,  # 切分的文本块重叠大小
    length_function=len,  # 长度函数
    add_start_index=True,  # 是否添加开始索引
)

text = text_splitter.create_documents([content])
print(text)
