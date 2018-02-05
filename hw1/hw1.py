import nltk

# returns tuple of total # of words and
#   10 most frequent words
def get_inaugural_data(filename):
    words = nltk.corpus.inaugural.words(filename)
    portrait_freq = nltk.FreqDist(words)

    return (len(words), portrait_freq)

# performs the same operation as get_inaugural_data, but user uses own file
def get_own_file_data(filename):
    data = nltk.corpus.PlaintextCorpusReader('.', [filename])
    portrait_words = data.words(filename)
    portrait_freq = nltk.FreqDist(portrait_words)

    return (len(portrait_words), portrait_freq)

# get avg sent len from a file in inaugural corpus
def get_avg_sentence_len(filename):
    # put into list of sentences
    sents = (nltk.corpus.inaugural.sents(filename))
    total_words = 0

    for words in sents:
        total_words += len(words)

    return (total_words / len(sents))


def get_own_file_avg_sent_len(filename):
    f = open(filename)
    raw = f.read()
    total_words = 0
    sents = nltk.sent_tokenize(raw)

    for words in sents:
        total_words += len(words.split())

    #print (total_words)
    return (total_words / len(sents))

def main():
    wash_result = get_inaugural_data('1789-Washington.txt')
    wash_avg_len = get_avg_sentence_len('1789-Washington.txt')
    print ('1789-Washington.txt: ' + str(wash_result[0]) + ' words')
    wash_result[1].tabulate(12)
    print ("Average sentence length: " + str(wash_avg_len))
    print ('')

    obama_result = get_inaugural_data('2009-Obama.txt')
    obama_avg_len = get_avg_sentence_len('2009-Obama.txt')
    print ('2009-Obama.txt: ' + str(obama_result[0]) + ' words')
    obama_result[1].tabulate(12)
    print("Average sentence length: " + str(obama_avg_len))
    print ('')

    trump_result = get_own_file_data('2017-Trump.txt')
    trump_avg_len = get_own_file_avg_sent_len('2017-Trump.txt')
    print ('2017-Trump.txt: ' + str(trump_result[0]) + ' words')
    trump_result[1].tabulate(13)
    print ("Average sentence length: " + str(trump_avg_len))
    print ('')




# if hw1.py is top-level program
if __name__ == '__main__':
    main()
