import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import altair as alt
import numpy as np
import pandas as pd

data = pd.read_csv("Fake Email.csv")
cc = Counter()
ndates = []
for i, row in data.iterrows():
    txt = row['title']
    date = row['date']
    try:
        ndates.append(date.split(' ')[0]+" "+date.split(', ')[1])
    except:
        ndates.append('Jan 2015')
        continue
    for word in txt.split():
        cc[word.lower()]+=1

data['date']=ndates

front = cc.most_common()[:3]
print(front)
front = [fr[0] for fr in front]

counter = {}
for i, row in data.iterrows():
	c = Counter()
	txt= row['title']
	date = row['date']
	for word in txt.split():
		if word in front:
			c[word]+=1
	if not date in counter: counter[date] = Counter()
	counter[date].update(c)

src = []
for date in counter.keys():
	c = counter[date]
	for k, v in c.items():
		src.append((date, k, v, ''))

df = pd.DataFrame(src, columns=['date','word','count','col'])


colors = ['red', 'green', 'blue']
cols = []
for i, row in df.iterrows():
	cols.append(colors[front.index(row['word'])])

df['col'] = cols
print(df)
df = df[['date','col','count']]
    


alt.Chart(df).mark_line().encode(
    x='date',
    y='count',
    color='word'
)