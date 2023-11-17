import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud ,STOPWORDS
from PIL import Image

def word_plot(column,name ,text):
    
    comments = df['text'].loc[column ==name ].values    
    
    word_cloud = WordCloud( width = 640, height = 640, background_color = 'black',
                stopwords = STOPWORDS).generate(str(comments))     # stopwords are a,an,the
    
    fig = plt.figure( figsize = (8, 5), facecolor = 'k', edgecolor = 'k')
    plt.subplot()
    plt.imshow(word_cloud, interpolation = 'bilinear')
    plt.suptitle("Most frequent words in " +  text , y = 1.06,color = "white")
    plt.tight_layout(pad = 0)
    plt.axis('off')
    plt.show()
    
word_plot(df['category'],'tech' ,'Technology')
word_plot(df['category'],'business' ,'Business')
word_plot(df['category'],'politics' ,'Politics')
word_plot(df['category'],'entertainment' ,'Entertainment')
