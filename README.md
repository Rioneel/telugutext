# Telugu Text Tokenizers for LLM Training

This repository contains Python scripts designed for tokenizing Telugu text, specifically aimed at preparing datasets for training large language models (LLMs). These scripts facilitate efficient text processing and are optimized for Telugu, enabling better performance for NLP tasks in the language.

## Features

- **BERT-based Tokenization**: Includes tokenizers compatible with the BERT architecture for Telugu text.
- **Script Conversion**: Converts raw Telugu text into tokenized formats suitable for machine learning pipelines.
- **Search and Retrieval**: Contains utilities for token-based search in datasets.

## Scripts Overview

1. **`berttokenizer2.py`**:  
   Implements a tokenizer tailored for Telugu text based on BERT. Includes functionality for handling complex scripts and diacritics.

2. **`convert4.py`**:  
   Provides utilities to preprocess and convert raw Telugu text into tokenized datasets for model training.

3. **`scriptx2.py`**:  
   Focuses on specific tokenization tasks, such as handling unique Telugu character sets and generating embeddings.

4. **`search4.py`**:  
   A search utility that allows for efficient token-based search within Telugu text datasets.

## Requirements

- Python 3.8 or higher
- Required libraries:  
  Install dependencies using the following command:
  ```bash
  pip install -r requirements.txt
