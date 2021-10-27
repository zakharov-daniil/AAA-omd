class CountVectorizer():
    def __init__(self, lowercase=True):
        self.lowercase = lowercase
        self._vocabulary = {}
        self._list_of_ngrams = []

    def get_feature_names(self):
        return list(self._vocabulary.keys())

    def fit_transform(self, raw_texts):
        """Заполняет словарь из всех текстов и выдаёт набор n-грамм текстов"""
        vocab = set()
        self._vocabulary = {}
        self._list_of_ngrams = []
        
        for text in raw_texts:
            if self.lowercase:
                text_words = text.lower().split()
            else:
                text_words = text.split()
            vocab.update(set(text_words))

        vocab = list(vocab)
        vocab.sort()
        self._vocabulary = dict.fromkeys(vocab, 0)

        for text in raw_texts:
            if self.lowercase:
                for word in text.lower().split():
                    self._vocabulary[word] += 1
            else:
                for word in text.split():
                    self._vocabulary[word] += 1
            self._list_of_ngrams.append(list(self._vocabulary.values()))
            self._vocabulary.update({}.fromkeys(self._vocabulary, 0))
        return self._list_of_ngrams


if __name__ == '__main__':
    vec = CountVectorizer()
    corpus = ['Crock Pot Pasta Never boil pasta again', 'Pasta Pomodoro Fresh ingredients Parmesan to taste']
    count_matrix = vec.fit_transform(corpus)
    print(vec.get_feature_names())
    print(count_matrix)

    corpus2 = ['This is the first document',
               'This document is the second document',
               'And this is the third one',
               'Is this the first document']
    count_matrix2 = vec.fit_transform(corpus2)
    print(vec.get_feature_names())
    print(count_matrix2)
