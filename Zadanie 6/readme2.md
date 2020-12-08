# 1. Otwieranie pliku
Demonstracja otwarcia pliku, sluzy do tego metoda open(), w parametrze której podajemy ścieżke do pliku.

# 2. Zamykanie pliku po skończonych operacjach
Dwa warianty:
try - finally - pozwala na zamieszczenie bloku kodu do wykonania pomiędzy keywordami try i finally, po zakończeniu wykonywania bloku plik jest zamykany,
nawet jeśli w trakcie wystąpi błąd
slowo kluczowe with - pozwala na wykonanie bloku kodu zawartego pod slowem kluczowym with, a następnie zamknięcie pliku

# 3. Drugi argument pozycyjne
Metoda open pozwala na dodanie drugiego algorytmu, przedstawiającego tryb otwierania pliku, roróżniamy następujące warianty:
domyślny bądź 'r' - readonly - plik tylko do odczytu
'w' - edytowanie, przycinanie, zastępywanie pliku
rb/wb/ - odczyt/zapisywanie za pomocą danych binarnych

# 4. Typy plików
W zależności od tego, w jaki sposób otworzymy plik, zostanie nam zwrócony inny typ, jest to ukazane w zadaniach w kodzie.

# 5. Surowy plik
Jak mówi poradnik: “generally used as a low-level building-block for binary and text streams.” - jest on oznaczony typem _io.FileIO, jak go otworzyć jest widoczne w kodzie

# 6. Odczytywanie treści
a) metoda .read() pozwala na odczytanie treści całego pliku, gdy nie podamy parametru, bądź umieścimy w nim -1, możemy też podać parametr size, co odpowiada wartości bitowej
b)metoda .readline() również przyjmuje parametr size i taka ilość znaków z danej linii zostanie odczytana
c) metoda .readlines() zwraca treść pliku jako listę wyrazów

#7. Iterowanie wyrazów
Rozróżniamy trzy sposoby:
a) za pomocą metody .readline() iterujemy po wszystkich liniach dokumentu
b) za pomocą .readlines iterujemy w podobny sposób
c) sposób bardziej "pythonowski", zwyczajnie iterujemy po obiekcie odczytanego pliku

# 8. Zapisywanie do pliku
Dwie metody:
write(string) - zapisuje string w parametrze do pliku
writelines(seq) - zapisuje wpisane sekwencje do pliku, trzeba ręcznie dodać zakończeinia linii

