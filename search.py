import os
import txtai
import pandas
from fastapi import FastAPI
import uvicorn

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

app = FastAPI()

def main(reload: bool):
    global embeddings
    if reload:
        embeddings.close()
    embeddings = txtai.Embeddings({
        "path": "sentence-transformers/all-mpnet-base-v2",
        # Other Models...
        # "path": "sentence-transformers/paraphrase-mpnet-base-v2",
        # "path": "sentence-transformers/paraphrase-MiniLM-L6-v2",
        # "path": "sentence-transformers/paraphrase-albert-small-v2",
        # "path": "sentence-transformers/paraphrase-albert-base-v2",
        "content": True
    })
    data = pandas.read_csv("data.csv")
    txtai_data = []
    for i, text in data.iterrows():
        txtai_data.append((text["ID"], text["PRODUCT"], None))
    embeddings.index(txtai_data)

@app.get("/search")
async def search(query: str):
    search_result = embeddings.search(query, limit=10)
    results = {}
    for index, result in enumerate(search_result):
        results[index] = result
    return results

@app.get("/reload")
async def reload(key: str = None):
    if key == "update100":
        main(True)
        return {"status": "success"}
    else:
        return {"status": "failed"}

if __name__ == "__main__":
    main(False)
    uvicorn.run(app, host="0.0.0.0", port=8000)
