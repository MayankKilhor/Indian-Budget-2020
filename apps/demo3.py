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
    mask2 = Image.open('map.jpg')
    img = Image.open('wordcloud.png')
    mask = np.array(mask2)
    st.image(img)
    # wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='white', collocations=False, stopwords = STOPWORDS, mask=mask).generate(article.text)

    # fig= plt.figure(figsize=(10,10), facecolor="k")
    # plt.axis("off")
    # plt.tight_layout(pad=0)
    # plt.imshow(wordcloud, interpolation='bilinear')
    # # plt.show()
    # st.write(fig)
