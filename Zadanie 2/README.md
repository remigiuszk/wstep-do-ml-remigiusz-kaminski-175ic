# Korzystanie z bilbioteki pandas do odczytu danych z arkuszu kalkulacyjnego csv

## 1. Metoda pd.read_csv()
Pozwala na odczyt danego pliku podanego w parametrze i przedstawienie go jako obiekt dataframe - obiekt przechowujący dane w formie tabeli, w której dane możemy obrabiać innymi metodami dostępnymi w bibliotece pandas

## 2. Metoda <dataframe>.sort_values
Metoda sortująca cały obiekt dataframe według kolumny podanej w parametrze. Dodatkowo przyjmuje sposób sortowania, np ascending = True (rosnąco)

## 3. Metoda <dataframe>.rename()
Umożliwia zmianę podanej kolumny na inną, przyjmuje w parametrze dwie wartości w następującym formacie: <br>
wartość1:wartość2, <br>
gdzie wartość1 to kolumna przeznaczona do edycji, a wartość2 to nazwa kolumny zastępująca poprzednią

## 4. Metoda <dataframe>.drop()
W kodzie korzystamy w niej aby usunąć dwie wyznaczone kolumny w dataframe. W parametrze wystarczy umieścić zmienną "columns" oraz przypisać do niej tablice nazw przeznaczonych do usunięcia kolumn, przykład: <br>
samochody.drop(columns=['model','przebieg'])

## 5. <dataframe>.tail()
Metoda wyświetlająca ostatnie x wierszy, gdzie x to liczba typu int podana w parametrze

## 6. <dataframe>['kolumna']
Ekstrakcja jednej kolumny z dataframe

## 7. <dataframe>['kolumna'].value_counts()
Zwraca każdą unikalną wartość w danej kolumnie wraz z ilością jej wystąpień

## 8. <dataframe>[<dataframe>.<kolumna>=="<wartość>"]
Zapis ten pozwala nam na ekstrakcje rekordów o podanej wartości w danej kolumnie

## 9 . pd.merge()
Za pomocą tej metody możemy złączyć dwie pożądane wartości z kolumn, używając dwóch obiektów stworzonych na zasadzie zapisu powyżej, dodatkowo dodajemy rodzaj połączenia "inner", które możemy znać np z SQL'a, polega on na tym, że kolumny zostaną połączone, tylko jeśli w obydwu z nich znajdują się wartości.

## 10. <dataframe>.pivot(columns='<kolumna>', values='<nazwa_kolumny>')
rozkład wierszy na kolumny, coś w stylu transpozycji
