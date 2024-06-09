import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def summarize_text(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)

    freq_table = {}
    for word in words:
        word = word.lower()
        if word not in stop_words:
            if word in freq_table:
                freq_table[word] += 1
            else:
                freq_table[word] = 1

    sentences = sent_tokenize(text)
    sentence_value = {}

    for sentence in sentences:
        for word, freq in freq_table.items():
            if word in sentence.lower():
                if sentence in sentence_value:
                    sentence_value[sentence] += freq
                else:
                    sentence_value[sentence] = freq

    sum_values = 0
    for sentence in sentence_value:
        sum_values += sentence_value[sentence]

    average = int(sum_values / len(sentence_value))

    summary = ''
    for sentence in sentences:
        if (sentence in sentence_value) and (sentence_value[sentence] > (1.25 * average)):
            summary += " " + sentence

    return summary
