# klasy json, requests

json - pakiet służący do enkodowania i dekodowania danych(serializacji) w formaice JSON - JavaScript Object Notation, notacja ta jest bardzo popularna, używana np w RESTfulowych API

requests - pakiet służący do obsługi zapytań http

#metoda dump()
Przyjmuje następujące parametry: obiekt danych do zserialozowania, oraz obiekt pliku, na które mają zostać zapisane dane, metoda zapisuje wskazany obiekt w podanym pliku

#json.dumps()
metoda przyjmuje obiekt do zapisania do zmiennej, jest taka sama jak dump(), lecz nie wymaga pliku w parametrze

może przyjmować opcjonalne parametry, np jak "indent" ustalająćy wcięcie

#metody json.load() i json.loads()

loads() - ładowanie obiektu ze stringu

load() - analogicznie do dump() - ładowanie obiektu json z pliku

# response.get()
metoda pozwalająca na wykonaniu zapytania do api pod danym adresem w parametrze (używając metody http.GET)

# typ complex
Następuje gdy nastąpi interakcja liczby rzeczywistej, oraz nierzeczywistej, tworząc umowny typ danych complex

