import re

class TextAnalyzer:
    def __init__(self, text, stopwords=None):
        self.raw = text
        self.stopwords = stopwords if stopwords else []
        self.text = self.normalize(text)
        self.words = self.tokenize()

    def normalize(self, text):
        text = text.lower()
        text = re.sub(r"[^\w\s.!?]", " ", text, flags=re.UNICODE)
        return text

    def tokenize(self):
        words = self.text.split()
        return [w for w in words if w not in self.stopwords]

    def char_count(self, spaces=True):
        return len(self.raw) if spaces else len(self.raw.replace(" ", ""))

    def word_count(self):
        return len(self.words)

    def sentence_count(self):
        return len(re.findall(r"[.!?]", self.raw))

    def paragraph_count(self):
        return len([p for p in self.raw.split("\n") if p.strip()])

    def avg_word_len(self):
        if not self.words: return 0
        return round(sum(len(w) for w in self.words)/len(self.words),2)

    def avg_sentence_len(self):
        sentences = re.split(r"[.!?]", self.raw)
        sentences = [s for s in sentences if s.strip()]
        if not sentences: return 0
        return round(sum(len(s.split()) for s in sentences)/len(sentences),2)

    def frequency(self):
        freq=[]
        for w in self.words:
            found=False
            for i in range(len(freq)):
                if freq[i][0]==w:
                    freq[i]=(w,freq[i][1]+1)
                    found=True
                    break
            if not found:
                freq.append((w,1))
        return freq

    def search_word(self, word):
        word = word.lower()
        clean_words = [re.sub(r"[^a-ząćęłńóśżź]", "", w) for w in self.words]
        return clean_words.count(word)


    def search_phrase(self, phrase):
        return self.raw.lower().count(phrase.lower())

