import math


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

        if self.lowercase:
            raw_texts = [text.lower() for text in raw_texts]

        for text in raw_texts:
            text_words = text.split()
            vocab.update(set(text_words))

        vocab = list(vocab)
        vocab.sort()
        self._vocabulary = dict.fromkeys(vocab, 0)

        for text in raw_texts:
            for word in text.split():
                self._vocabulary[word] += 1
            self._list_of_ngrams.append(list(self._vocabulary.values()))
            self._vocabulary.update({}.fromkeys(self._vocabulary, 0))

        return self._list_of_ngrams


def tf_transform(count_matrix: []) -> []:
    tf_matrix = []

    for vec in count_matrix:
        number_of_word = sum(vec)
        tf_matrix_row = [round(i / number_of_word, 3) for i in vec]
        tf_matrix.append(tf_matrix_row)

    return tf_matrix


def idf_transform(count_matrix: []) -> []:
    result = list()
    document_count = len(count_matrix) + 1

    for col in range(len(count_matrix[0])):
        cur_sum = 0
        for row in range(len(count_matrix)):
            cur_sum += bool(count_matrix[row][col])
        result.append(cur_sum + 1)

    for i in range(len(result)):
        result[i] = math.log(document_count / result[i]) + 1

    return result


class TfidfTransformer():
    def fit_transform(self, matrix):
        tf = tf_transform(matrix)
        idf = idf_transform(matrix)

        tf_idf = []
        for text in tf:
            tf_idf.append([round(a * b, 3) for a, b in zip(text, idf)])

        return tf_idf


class TfidfVectorizer(CountVectorizer):
    def __init__(self) -> None:
        super().__init__()
        self._tfidf_transformer = TfidfTransformer()

    def fit_transform(self, corpus):
        count_matrix = super().fit_transform(corpus)
        return self._tfidf_transformer.fit_transform(count_matrix)


if __name__ == '__main__':
    corpus = ['Crock Pot Pasta Never boil pasta again',
                'Pasta Pomodoro Fresh ingredients Parmesan to taste'
            ]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)

    print(vectorizer.get_feature_names())
    print(tfidf_matrix)
