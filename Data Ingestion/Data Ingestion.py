# path_chunked_docs ->
# chunked_buying_guides ->
chunked_docs = []
chunked_buying_guides = []
for path_chunked_doc in paths_chunked_docs:
  with open(path_chunked_doc, 'r') as f:
    chunked_docs.append( json.load(f) )

for path_chuked_buying_guide in paths_chunked_buying_guides:
  with open(path_chuked_buying_guide, 'r') as f:
    chunked_buying_guides.append( json.load(f) )
