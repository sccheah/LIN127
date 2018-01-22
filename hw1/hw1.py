import nltk

wash = nltk.corpus.inaugural.words('1789-Washington.txt')

#for word in wash:
#    print(word)

portrait_freq = nltk.FreqDist(wash)

portrait_freq.tabulate(10)
