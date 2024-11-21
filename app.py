import streamlit as st 
import base64

def add_bg_image(image_file):
    with open(image_file, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    bg_image = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_string}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(bg_image, unsafe_allow_html=True)

# Add background image
add_bg_image("bg.png")


st.title("Text Summarizer 🗟")
st.subheader('🧠 Overview:')
st.write("Text Summarizer lets you customize and generate concise summaries by selecting the percentage of content you want to keep, highlighting the most relevant sentences with advanced NLP. Get to the key points quickly and easily.")

text = st.text_area("Input the text you want to summarize...📝")


import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

xInput = st.slider("**Length Adjuster**: Select the percentage of the summary length 🔧", min_value=1, max_value=100, value=10)

if st.button('Summarize✨'):
    if text.strip():

        nlp = spacy.load("en_core_web_md")
        doc=nlp(text.strip())

        tokens = [token.text for token in doc]


        #Word freq.
        word_frequencies = {}
        for word in doc:
            if word.text.lower() not in STOP_WORDS:
                if word.text.lower() not in punctuation:
                    if word.text not in word_frequencies.keys():
                        word_frequencies[word.text] = 1
                    else:
                        word_frequencies[word.text] += 1

        #Max word frequency:                
        max_word_freq = max(word_frequencies.values())

        for word in word_frequencies.keys():
            word_frequencies[word] = word_frequencies[word]/max_word_freq

        #Sentence Tokens: 
        sentence_tokens = [sent for sent in doc.sents]

        sentence_scores = {}


        for sent in sentence_tokens:
                for word in sent:
                    word_lower = word.text.lower()  # Convert to lowercase
                    if word_lower in word_frequencies.keys():
                        sentence_scores[sent] = sentence_scores.get(sent, 0) + word_frequencies[word_lower]
                        
        from heapq import nlargest
        select_length = int(len(sentence_tokens) * (xInput/100))


        #Summary
        summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)

        final_summary = [word.text for word in summary]

        st.subheader("Summary")
        if not final_summary:
            st.warning('⚠️ The summary seems too short. Try increasing the length adjustment percentage.')
        else:
            st.success(" ".join(final_summary))
    else:
        st.error("Please enter text..")
        
st.markdown("""
    ---
    <div style="text-align: center;">
        Created by Tanishq Bololu 😁<br>
        🚀 <a href="https://www.linkedin.com/in/tanishqbololu/" target="_blank">LinkedIn</a>
    </div>
""", unsafe_allow_html=True)
