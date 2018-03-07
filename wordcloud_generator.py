import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import re 
from collections import Counter

# load df containing lyrics, set lyrics column as a series
file = pd.read_csv('kanye_lyrics.csv', sep=';', header=None)
lyrics_text = file.iloc[:,1]
lyrics_text = str(lyrics_text)

# clean data with regex
no_paran = re.sub("[\(\[].*?[\)\]]", "", lyrics_text)
cleaned = re.sub('(\n+)(?=[A-Z])', ' ', no_paran)

kanye_mask = np.array(Image.open("kanye.jpg"))

# figure
wordcloud = WordCloud(mask=kanye_mask).generate(cleaned)
plt.figure(figsize=(15,15))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()

count = Counter(cleaned)