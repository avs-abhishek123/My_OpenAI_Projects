import nltk
nltk.download('all')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

def summarize(text, n):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    # Tokenize the sentences into words
    words = [word_tokenize(sentence) for sentence in sentences]
    # Remove stop words from the words
    filtered_words = [[word for word in sentence if word.lower() not in stopwords.words('english')] for sentence in words]
    # Compute the frequency of each word
    freq_dist = FreqDist([word for sentence in filtered_words for word in sentence])
    # Identify the n most frequent words
    top_n_words = [word[0] for word in freq_dist.most_common(n)]
    # Find the sentences that contain the most frequent words
    important_sentences = [sentence for sentence in sentences if any(word in sentence for word in top_n_words)]
    # Join the important sentences into a summary
    summary = " ".join(important_sentences)
    return summary
