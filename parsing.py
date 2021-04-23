import re
import os
import zipfile
from collections import defaultdict

# Regular expressions to extract data from the corpus
doc_regex = re.compile("<DOC>.*?</DOC>", re.DOTALL)
docno_regex = re.compile("<DOCNO>.*?</DOCNO>")
text_regex = re.compile("<TEXT>.*?</TEXT>", re.DOTALL)


with zipfile.ZipFile("ap89_collection_small.zip", 'r') as zip_ref:
    zip_ref.extractall()
   
# Retrieve the names of all files to be indexed in folder ./ap89_collection_small of the current directory
for dir_path, dir_names, file_names in os.walk("ap89_collection_small"):
    allfiles = [os.path.join(dir_path, filename).replace("\\", "/") for filename in file_names if (filename != "readme" and filename != ".DS_Store")]

stop_list = []
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

with open("stopwords.txt", "r") as f:
    for line in f:
        stop_list.extend(line.split())

for file in allfiles:
    with open(file, 'r', encoding='ISO-8859-1') as f:
        filedata = f.read()
        result = re.findall(doc_regex, filedata)  # Match the <DOC> tags and fetch documents

        for document in result[0:]:
            # Retrieve contents of DOCNO tag
            docno = re.findall(docno_regex, document)[0].replace("<DOCNO>", "").replace("</DOCNO>", "").strip()
            # Retrieve contents of TEXT tag
            text = "".join(re.findall(text_regex, document))\
                      .replace("<TEXT>", "").replace("</TEXT>", "")\
                      .replace("\n", " ")
                      
            # step 1 - lower-case words, remove punctuation, remove stop-words, etc. 
            
            text = text.lower()
            for element in text:
                if element in punctuation:
                    text = text.replace(element, '')

            for w in stop_list:
                pattern = r'\b'+w+r'\b'
                text = re.sub(pattern, '', text)
    
            # step 2 - create tokens 
            # step 3 - build index

            text = text.split()
            doc_dict = defaultdict(list)
            i = 0
            position = 0
            for term in text:
                if (term not in doc_dict):
                    doc_dict[term] = [[i, docno, position]]
                    i = i + 1
                    position = position + 1
                else:
                    # duplicate_key = [((doc_dict[term][0]), docno, text.index(term))]
                    doc_dict[term].append([doc_dict[term][0][0], docno, position])       
                    position = position + 1
            

           
print(len(doc_dict["home"]))