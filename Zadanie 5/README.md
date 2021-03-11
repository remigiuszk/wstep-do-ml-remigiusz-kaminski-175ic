# SpaCy
darmowa opensourcowa biblioteka do NLP - przetwarzania języka naturalnego, pozwala na wszelkie operacje słownikowe oraz obróbke tekstów
## metoda nlp()
introduction_doc = nlp(introduction_text) <br>
Pozwala na przetworzenie podanego w parametrze tekstu i rozbicie go na pojedyncze wyrazy, każdy z nich będzie posiadał swoje miejsce w pamięci co pozwala na wykonanie operacji na każdym z nich osobno
Analogicznie, możemy przetworzyć dłuższy tekst i podzielić go na zdania. <br>
## list(about_doc.sents)
ta metoda pozwala na zapisanie poszczególnych zdań do osobnych miejsc w pamięci, które możemy później przeiterować pętlą
## Spacy umożliwa zastąpienie podstawowego separatora zdań (domyslnie kropki) na inny, dowolnie wybrany, w tym przypadku wielokropek
>>> def set_custom_boundaries(doc):
     # Adds support to use `...` as the delimiter for sentence detection <br>
     for token in doc[:-1]: <br>
        if token.text == '...': <br>
             doc[token.i+1].is_sent_start = True <br>
     return doc <br>
<br>
custom_nlp.add_pipe(set_custom_boundaries, before='parser')<br>
## Tokenizacja
Operacja ta pozwala podzielić tekst na najbardziej podstawowe jednostki - tokeny, dodatkowo SpaCy umożliwia wyświetlenie wielu parametrów na ich temat: <br>
print (token, token.idx, token.text_with_ws,
...            token.is_alpha, token.is_punct, token.is_space,
...            token.shape_, token.is_stop)

## Przykładowe wyjście: <br>
Gus 0 Gus  True False False Xxx False <br>

## Opis wyjścia: <br>
text_with_ws - drukuje token wraz ze spacją <br>
is_alpha - wykrywa czy tekst jest zlozony z liter alfabetu <br>
is_punct - wykrywa czy token jest znakiem (, .) <br>
is_space - wykrywa czy token jest spacją <br>
shape_ - drukuje kształt wyrazu <br>
is_stop - sprawdza czy jest słowem stopu(definicja później) <br>

## Spacy umożliwia również personelizacje tokenizacji, możemy ustalić takie parametry jak:
nlp.vocab - kontener przechowujacy specjalne przypadki oraz ich rozwiązanie, jak np emotikony <br>
prefix_search - fukcja która rozpoznaje znaki interpunkcyjne poprzedzające, takie jak np otwarcie nawiasu <br>
infix_finditer - funkcja przetwarzająca separatory, które nie są spacją <br>
suffix_search - funkcja rozpoznająca znaki interpunkcyjne kończące, jak np zamknięcie nawiasu <br>
token-match - opcjonalny bool który wkyrywa stringi, które nie powinny być rozdzielane, jak np URLe <br>

## Słowa stopu 
najbardziej powszechne słowa w języku, w angielskim np the, are but, they. Większość zdań muszą posiadać slowa stopu, aby miały sens. Sęk w tym, że słowa stopu są usuwane i pomijane podczas przetwarzania
for token in about_doc:
...     if not token.is_stop:
...         print (token) <br>

Można również wypisać tokeny nie posiadające słow stopu: <br>
 about_no_stopword_doc = [token for token in about_doc if not token.is_stop] <br>
 print (about_no_stopword_doc) <br>
## Lemmatization
Procesu usuwający odmiane wyrazu, np z wyrazu niebezpieczny, osiągamy wyraz niebezpieczeństwo. Zaletą tego procesu jest fakt, że możemy traktować różne odmiany jednego wyrazu jako jeden obiekt <br>
aby podejrzeć wyraz po lemmatyzacji, wystarczy że użyjemy właściwości .lemma_ <br>
for token in conference_help_doc: <br>
...     print (token, token.lemma_) <br>
## Częstotliwość występywania słów
SpaCy umożliwia analize na temat wzorów, jakie tworzą słowa w danym tekście. <br>
Możemy np wyświetlić pięć najczęściej występujących wyrazów, albo takie które są unikalne: <br>
 word_freq = Counter(words) <br>
 #5 commonly occurring words with their frequencies <br>
 common_words = word_freq.most_common(5) <br>
<br>
>>> unique_words = [word for (word, freq) in word_freq.items() if freq == 1] <br>
>>> print (unique_words) <br>
## Part of speech tagging
Klasyfikacja części mowy, SpaCy potrafi rozpoznać, jaką częścią mowy jest dany wyraz w tekście.<br>
print (token, token.tag_, token.pos_, spacy.explain(token.tag_))<br>
## Wyjście
Gus NNP PROPN noun, proper singular<br>

## Pozwala to również np na ekstrakcje tylko rzeczowników z danego tekstu:
 nouns = [] <br>
 adjectives = [] <br>
 for token in about_doc: <br> 
     if token.pos_ == 'NOUN': <br>
         nouns.append(token) <br>
        nouns <br>

## Wizualizacja - używanie displaCy
Narzędzie pozwalające na wizualizacje połączeń pomiędzy częściami mowy. <br>
<br>
     about_interest_text = ('He is interested in learning' <br>
     ' Natural Language Processing.') <br>
     about_interest_doc = nlp(about_interest_text) <br>
     displacy.serve(about_interest_doc, style='dep') <br>

## Funckcje preprocessing - przed wykonaniem przetwarzania
Są to funkcje wykonywane na chwile przed przetwarzaniem danego tekstu, umożliwają takie opcje jak: <br>
- zamiana wielkości liter
- lemmatyzacja każdego tokenu
- usuwanie znaków interpunkcyjnych
- usuwanie słów stopu













