# CS172 - Assignment 1 (Tokenization)

## Team member 1 - Marc Jimenez

###### Provide a short explanation of your design

**Parsing.py** takes in the documents located in the provided zip file and parses through them creating several dictionarys that hold information regarding the terms and documents. It does this by running our expected text preprocessing methods to remove punctuations and stop words. Next it will tokenize the text and create dictionaries called **term_termID_map, doc_docID_map, and doc_dict**. The first two dictionarys will hold information specifically to terms and documents that act as keys. For the **term_termID_map** it will hold the **(termID, termFrequency in corpus, and docFrequency)** of the key term. Next the **doc_docID_map** will hold **(docID, length of document)** of the key document. Finally, our last map, **doc_dict** will hold information for a key term's position on every document in our corpus specifically, **(doc_str, position)**. This will also differ as it will be a dictionary of lists of tuples while the two former dictionaries are dictionaries of tuples.

**Read_index.py** will simply use the commands below to access statistics on documents and terms.

###### Language used, how to run your code, if you attempted the extra credit (stemming), etc. 

To run the code make sure the parsing.py and read_index.py scripts are initialized.
1) python read_index.py --term <term>
2) python read_index.py --doc <docno>
3) python read_index.py --term <term> --doc <docno>

Python 3.7.7, extra credit was no attempted

