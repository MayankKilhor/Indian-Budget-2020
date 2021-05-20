import numpy as np
import pandas as pd
import streamlit as st

from PIL import Image
from newspaper import Article
import plotly.express as px
from operator import itemgetter
import math
import nltk
from nltk import tokenize
from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize

def app():
    st.markdown("""
                    # Module 2:  Budget Speech Text Visualization 
                    #
                    ## Description
                    Speech analysis of the speakers often tends to the interests of the governments for the planned years and can give a significant insight into where the common man can expect changes and increments over the course of the year. Hence analysis of the Budget speech is crucial in understanding the ideology of the government as well as the sectors that the budget will focus on in the forefront which helps in future planning and social security for the middle class.

                    
                    ## Inference
                    ->   The text visualisation shows that the speaker has focused heavily on Tax, coming from 2018-2019 where GST was first enforced nationwide we can see how the government is trying to change certain parameters to smoothen the process of tax elevations, followed by tax is the word Proposed, Signifying that the government is ambitious and looks ahead in the long run, judging by the current trends in the economy and flailing opportunities for employment, it shows that schemes are being proposed but not followed through.
                    
                    ->   Shallow Promises often lead to the demise of trust in the government. Furthermore we can see that a lot of comparison has been done from the previous year and the word government comes up often.
                    
                    _______________________________________________________________________________________________
                    
                    ## DATASET

                    [link](https://www.indiatoday.in/business/budget-2020/story/full-text-of-budget-2020-speech-by-finance-minister-nirmala-sitharaman-1642337-2020-02-01#:~:text=Hon'ble%20Speaker%2C,for%20the%20year%202020%2D2021.&text=In%20May%202019%2C%20Prime%20Minister,with%20all%20humility%20and%20dedication)

                    #####""")
    st.markdown("""
                ____________________________________________________________________
                Finance Minister Nirmala Sitharaman, in her Budget speech, announced major tax reliefs for the salaried class and reduced the tax rate for different slabs for an individual income of up to Rs 15 lakh per annum, if a taxpayer opts for foregoing exemptions and deduction.
                
                We extracted the complete text of her speech and did various visualizations on that.


                ** _ Word Cloud _ ** - This word cloud helps to visualize and summarize all sorts of data which can be obtained from the Budget Speech. For better representation of the data and to make it more visually appealing, we also created a word cloud in the shape of the Indian Map.""")
    
    article = Article("https://www.indiatoday.in/business/budget-2020/story/full-text-of-budget-2020-speech-by-finance-minister-nirmala-sitharaman-1642337-2020-02-01#:~:text=Hon'ble%20Speaker%2C,for%20the%20year%202020%2D2021.&text=In%20May%202019%2C%20Prime%20Minister,with%20all%20humility%20and%20dedication.")
    article.download()
    article.parse()

    img = Image.open('wordcloud/wordcloud.png')

    
    st.image(img)

    st.markdown("""
                ____________________________________________________________________
                ** _ Bar chart _ ** - We created a bar chart to show the most frequently used words in the Budget Speech. We see an extremely high usage of the word Tax.""")
    

    def word_count(sentence):
        translate = sentence.maketrans({char: None for char in "'.,:*!"})
        cleaned_words = sentence.lower().translate(translate).split()
        word_counter = {}
        for word in cleaned_words:
            if word in word_counter:
                word_counter[word] += 1
            else:
                word_counter[word] = 1
        return word_counter
    word_counter = word_count(article.text)
    df = pd.Series(word_counter).to_frame()
    df.reset_index(level=0, inplace=True)
    df.columns = ['Word','WordCount']
    


    nltk.download('punkt')

    nltk.download('stopwords')


    
    stop_words = set(stopwords.words('english'))

    total_words = article.text.split()
    total_word_length = len(total_words)

    total_sentences = tokenize.sent_tokenize(article.text)
    total_sent_len = len(total_sentences)


    tf_score = {}
    for each_word in total_words:
        each_word = each_word.replace('.','')
        if each_word not in stop_words:
            if each_word in tf_score:
                tf_score[each_word] += 1
            else:
                tf_score[each_word] = 1

    # Dividing by total_word_length for each dictionary element
    tf_score.update((x, y/int(total_word_length)) for x, y in tf_score.items())

    def check_sent(word, sentences): 
        final = [all([w in x for w in word]) for x in sentences] 
        sent_len = [sentences[i] for i in range(0, len(final)) if final[i]]
        return int(len(sent_len))

    idf_score = {}
    for each_word in total_words:
        each_word = each_word.replace('.','')
        if each_word not in stop_words:
            if each_word in idf_score:
                idf_score[each_word] = check_sent(each_word, total_sentences)
            else:
                idf_score[each_word] = 1

    # Performing a log and divide
    idf_score.update((x, math.log(int(total_sent_len)/y)) for x, y in idf_score.items())

    tf_idf_score = {key: tf_score[key] * idf_score.get(key, 0) for key in tf_score.keys()}

    def get_top_n(dict_elem, n):
        result = dict(sorted(dict_elem.items(), key = itemgetter(1), reverse = True)[:n]) 
        return result

    pop_words = get_top_n(tf_idf_score, 50).keys()
    df1 = df.loc[df['Word'].isin(pop_words)].nlargest(12,'WordCount')
    df1 = df1.drop([1070,1444], axis=0)
    fig = px.bar(df1, x='Word', y='WordCount', color='WordCount')
    st.plotly_chart(fig)

