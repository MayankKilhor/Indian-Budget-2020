import streamlit as st

def app():
    from newspaper import Article
    article = Article("https://www.indiatoday.in/business/budget-2020/story/full-text-of-budget-2020-speech-by-finance-minister-nirmala-sitharaman-1642337-2020-02-01#:~:text=Hon'ble%20Speaker%2C,for%20the%20year%202020%2D2021.&text=In%20May%202019%2C%20Prime%20Minister,with%20all%20humility%20and%20dedication.")
    article.download()
    article.parse()
    # st.write(article.text)
    # from wordcloud import WordCloud
    import matplotlib.pyplot as plt
    from PIL import Image
    import numpy as np
    import pandas as pd
    mask2 = Image.open('map.jpg')
    img = Image.open('wordcloud.png')
    mask = np.array(mask2)
    
    st.image(img)

    import plotly.express as px

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
    from nltk import tokenize
    from operator import itemgetter
    import math
    import nltk

    nltk.download('punkt')
    from nltk.corpus import stopwords
    nltk.download('stopwords')

    from nltk.tokenize import word_tokenize
    
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
    # wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='white', collocations=False, stopwords = STOPWORDS, mask=mask).generate(article.text)

    # fig= plt.figure(figsize=(10,10), facecolor="k")
    # plt.axis("off")
    # plt.tight_layout(pad=0)
    # plt.imshow(wordcloud, interpolation='bilinear')
    # # plt.show()
    # st.write(fig)
