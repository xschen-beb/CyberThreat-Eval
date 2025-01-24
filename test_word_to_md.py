from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("RecommendationDictionary.docx")
res = result.text_content
fo = open("RecDict.md", 'w')
fo.write(res)
print(res)