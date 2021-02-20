
# search engine

index = {}
index["brown"] = [1]
index["fox"] = [1, 2]
index["lion"] = [2, 4, 6]

words = ["brown", "fox"]

results = set()


# Union of the two sets
for word in words:
    for doc_id in index[word]:
        results.add(doc_id)

# can do
print(results)

