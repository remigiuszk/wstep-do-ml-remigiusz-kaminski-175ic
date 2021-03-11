# klasy json, requests

## json - pakiet służący do enkodowania i dekodowania danych(serializacji) w formaice JSON - JavaScript Object Notation, notacja ta jest bardzo popularna, używana np w RESTfulowych API

## requests - pakiet służący do obsługi zapytań http

## metoda dump()
Przyjmuje następujące parametry: obiekt danych do zserialozowania, oraz obiekt pliku, na które mają zostać zapisane dane, metoda zapisuje wskazany obiekt w podanym pliku

## json.dumps()
metoda przyjmuje obiekt do zapisania do zmiennej, jest taka sama jak dump(), lecz nie wymaga pliku w parametrze

może przyjmować opcjonalne parametry, np jak "indent" ustalająćy wcięcie

## metody json.load() i json.loads()

loads() - ładowanie obiektu ze stringu

load() - analogicznie do dump() - ładowanie obiektu json z pliku

# response.get()
metoda pozwalająca na wykonaniu zapytania do api pod danym adresem w parametrze (używając metody http.GET)

# typ complex
Następuje gdy nastąpi interakcja liczby rzeczywistej, oraz nierzeczywistej, tworząc umowny typ danych complex

# CSV
## csv.reader(csv_file, delimiter=',')
Pozwala na odczyt pliku csv, jako parametry przyjmuje plik do odczytu, oraz separator, którym oddzielone są dane, w tym przypadku jest to przecinek
## csv_reader = csv.DictReader(csv_file)
Odczyt słownikowy, aby program mógł rozpoznać ile i jakie kolumny podajemy w pliku, należy dodać do nich nagłówki, pierwsza linia powinna wskazywać nazwy kolumn, w których pod spodem zawarte są dane. Na podstawie tego metoda potrafi rozpoznać jakie dane ma odczytać.
## Opcjonalne parametry metody reader()
delimiter - separator, o którym była mowa wcześniej
quotechar - znak oznaczający cytat
escapechar - wskazuje domyslny znak wychodzący z separatora
## zapis pliku CSV - metoda csv.writer()
przyjmuje w parametrach: plik do zapisu, separator, znak oznaczający cytat, oraz parametr "quoting" który pozwala na ustalenie rodzaju cytowania.
## csv.QUOTE_MINIMAL
domyślny przypadek, w którym cytowane będą linie, w które będą zawierać separator, bądź quotechar
## csv.QUOTE_ALL
będą cytowane wszystkie pola
## csv.QUOTE_NONNUMERIC
cytowane będą wszystkie pola nienumeryczne, a numeryczne będą skonwertowane do typu float
## csv.QUOTE_NONE
brak cytacji, trzeba podać parametr escapechar
## zapis ze slownikiem - metoda csv.DictWriter
Analogicznie jak do odczytu, musimy przygotować w zmiennej nazwy pól deklarując je w tablicy: <br>
fieldnames = ['emp_name', 'dept', 'birth_month'] <br>
następnie przekazujemy go w parametrze: <br>
writer = csv.DictWriter(csv_file, fieldnames=fieldnames) <br>
posiadając obiekt writer, możemy go wykorzystać do operacji zapisu:
 writer.writeheader() <br>
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'}) <br>
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'}) <br>
## parsowanie za pomocą pandas
pandas posiada gotową metodę do odczytu plików csv, wystarczy w jej parametrze podać plik, a stworzony zostanie za jego pomocą dataframe <br>
df = pandas.read_csv('hrdata.csv')
oczywiście metoda read_csv posiada również opcjonalne parametry: <br>
index_col = podajemy w nim nazwę kolumny, która bedzie indexowana, na podstawie której grupowane bedą rekordy
parse_dates = podjemy w nim nazwę kolumny, w której chcemy żeby pola były parsowane na daty
header = nagłówek
names = tablica z nazwami kolumn
## zapis za pomocą pandas
df.to_csv('hrdata_modified.csv') <br>
metoda pozwalająca na sparsfowanie dataframe do csv i zapisanie go

