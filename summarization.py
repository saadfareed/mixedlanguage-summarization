import re
import string

def text_summarization(text, ratio):
    sentences = re.split(r'[.!?]+', text)  # split the text into sentences based on punctuation
    word_counts = [len(re.findall(r'\w+', sentence.translate(str.maketrans('', '', string.punctuation))))
                   for sentence in sentences]  # count the number of words in each sentence
    average_word_count = sum(word_counts) / len(word_counts)  # find the average word count
    summary = [sentence for sentence, word_count in zip(sentences, word_counts)
               if word_count > average_word_count * ratio]  # select sentences with more words than average
    return ' '.join(summary)

text = "This is a mixed language text. It contains both English and Urdu words. Text summarization is a technique " \
       "for condensing the important information from a large text into a shorter form, preserving the key details. " \
        "The goal of text summarization is to create a short version of the original text that retains its essence. " \
       "یہ اردو زبان کا متن ہے۔ مختصری خصوصیات بہت زبردست طور پر اصل متن کی کلیدی معلومات برآوردہ کرتے ہوئے ، " \
       "The goal of text summarization is to create a short version of the original text that retains its essence. " \

summary = text_summarization(text, 1.2)

print(summary)
