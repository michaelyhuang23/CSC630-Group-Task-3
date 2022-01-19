import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

data = pd.read_csv("Fake Email.csv")
cc = Counter()
for i, row in data.iterrows():
	txt = data['title']
	date = data['date']
	for word in txt.split():
		cc[word.lower()]+=1

front = cc.most_common()[:3]
print(front)
front = [fr[0] for fr in front]

counter = {}
for i, row in data.iterrows():
	c = Counter()
	txt= data['title']
	date = data['date']
	for word in txt.split():
		if word in front:
			c[word]+=1
	if date not in counter: counter[date] = Counter()
	counter[date].update(c)

colors = ['red', 'green', 'blue']

for date in counter.keys():
	c = counter[date]
	for k, v in c.items():
		idx = front.index(k)
		plt.scatter()

