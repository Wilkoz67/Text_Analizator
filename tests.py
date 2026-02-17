from analyzer import TextAnalyzer

def test_empty():
    ta=TextAnalyzer("")
    assert ta.word_count()==0

def test_words():
    ta=TextAnalyzer("Ala ma kota")
    assert ta.word_count()==3

def test_search():
    ta=TextAnalyzer("Ala ma kota. Ala lubi kota.")
    assert ta.search_word("ala")==2
