# NLP-Text-Summarizer-spaCy
NLP-Text-Summarizer-Spacy is a Streamlit app that uses SpaCy for text summarization. It enables users to input text, adjust the summary length, and generate concise summaries by identifying the most important sentences based on word frequency.

## **Features:**
- **Tokenization**: Breaks the input text into words and sentences.
- **Word Frequency Analysis**: Scores sentences based on the frequency of important words.
- **Adjustable Summary Length**: Users can adjust the summary length using a slider to select how much of the text to retain.
- **Custom Background**: Option to personalize the app with a custom background image.

## **How It Works:**
1. **Input Text**: Enter your text in the input box.
2. **Processing**: The app tokenizes the text, calculates word frequencies, and scores sentences based on word relevance.
3. **Summarization**: Generates a summary by selecting the top sentences based on their scores.
4. **Summary Output**: Displays the summary, with the length controlled by the percentage selected.

## **Installation**

To run the app locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/tanishqbololu/NLP-Text-Summarizer-spaCy.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd NLP-Text-Summarizer-Spacy
   ```

3. **Install dependencies**:
   ```bash
   # Install Streamlit
    pip install streamlit

    # Install SpaCy
    pip install spacy

    # Install NLTK
    pip install nltk
  

    # Base64 is part of the Python standard library, so no installation is required.
      ```

5. **Download the SpaCy model**:
   ```bash
   python -m spacy download en_core_web_md
   ```

6. **Run the app**:
   ```bash
   streamlit run app.py
   ```

## **Dependencies:**
- Streamlit
- SpaCy
- NLTK
- Base64

## **Usage:**
- Input text and adjust the summary length slider to generate a concise summary of your text.
