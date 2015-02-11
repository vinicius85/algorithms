#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

dataset = []
stoplist={'shopping','tal','todo','mais','seu','na','dos','da','um', 'nao', 'uma', 'nesse', 'veja', 'encontre', 
	       'que', 'no', 'dia', 'hoje', 'ou' , 'por', 'seus', 'do', 'os',  'esses', 'pode', 'tambem',
	       'voce', 'em', 'ja', 'as', 'ser', 'esta', 'tem' , 'como', 'todos','feira',  'confira', 'faca',
	       'ficar', 'comprar', 'bom', 'mas', 'esse', 'ter', 'entao', 'muita', 'quem', 'preparamos',
	       'se', 'ainda', 'vamos', '','ate', 'nossos', 'encontra','faz', 'lo','nos','tipo', 'qualquer',
	       'sem', 'sua', 'nessas', 'essa', 'melhor', 'mesmo', 'quer','garantir', 'estar',
	       'ao', 'so', 'muito','ta','nunca', 'suas', 'garanta', 'anos', 'ai','vai', 'algumas',
	       'aqui', 'ele' ,  'aquela', 'sempre', 'olhada', 'sabado', 'isso', 'alguns', 'entre', 'aos', 'bem','elas','das', 'nosso','sao','vindo'}

f = io.open('output.log', 'r')
for line in f:
	post = line.split('\t')[1]
	print post
	dataset.append(post)

print '[cluster] extracting features...\n'

vectorizer = TfidfVectorizer(max_df=0.5, max_features=10000,
                                 min_df=2, stop_words=stoplist,
                                 use_idf=True, strip_accents='unicode')

X = vectorizer.fit_transform(dataset)

print '[cluster] n_samples: %d, n_features: %d' % X.shape

km = KMeans(n_clusters=3, init='k-means++', max_iter=200, n_init=1,verbose=1)
km.fit(X)

c0 = []
c1 = []
c2 = []

i = 0 
for label in km.labels_:
	if    label==0:
		c0.append(dataset[i])
	elif label==1:
		c1.append(dataset[i])
	elif label==2:
		c2.append(dataset[i])
	i+=1

print 'C0='+str(len(c0))+' , C1='+str(len(c1))+' , C2='+str(len(c2) )

f = io.open('cluster-output.log', 'w')
	
f.write(unicode('Cluster#0 -------------------\n\n'))
for instance in  c0:
		f.write(instance)
		f.write(unicode('\n'))

f.write(unicode('Cluster#1 -------------------\n\n'))
for instance in  c1:
		f.write(instance)
		f.write(unicode('\n'))
			
f.write(unicode('Cluster#2 -------------------\n\n'))
for instance in  c2:
		f.write(instance)
		f.write(unicode('\n'))
			
f.close()

order_centroids = km.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(3):
	print("Cluster %d: \n" % i)
	for ind in order_centroids[i, :10]:
		print(' %s' % terms[ind])