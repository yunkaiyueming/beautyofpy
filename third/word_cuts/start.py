import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba

from PIL import Image
import numpy as np

abel_mask = np.array(Image.open("alice_mask.png"))

text_from_file_with_apath = open('data.txt').read()

wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)

my_wordcloud = WordCloud(background_color="white", mask=abel_mask).generate(wl_space_split)

plt.imshow(my_wordcloud)
plt.axis("on")
plt.savefig('sample4.png')
#plt.show()