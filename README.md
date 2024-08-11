# Semantic Search Engine
This project is a simple semantic search engine built using the all-mpnet-base-v2 AI model, designed for efficient sentence phrasing and semantic similarity search.

## Features
Semantic Search: Finds the most semantically similar sentences or phrases to a given query.
Efficient Encoding: Utilizes the all-mpnet-base-v2 model to encode sentences into dense vectors for comparison.
Python-Based: Built entirely in Python for easy integration and use.
Installation
To use this semantic search engine, you'll need to have Python installed. You can install the necessary dependencies using pip:
```
pip install -r requirements.txt
```
Note: Ensure that you have a compatible version of Python (3.7 or higher).

## Usage
To use the search engine, simply run the main script with your query:
```
python main.py --query "your search phrase"
```
The script will return the most semantically similar results based on the all-mpnet-base-v2 model.

## Model
This project leverages the all-mpnet-base-v2 model from Hugging Face's Transformers library. This model is known for its efficiency in sentence embedding, making it a great choice for semantic search tasks.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## Acknowledgments
Hugging Face for providing the all-mpnet-base-v2 model.
The Python community for their continuous support and contributions to open-source projects.
