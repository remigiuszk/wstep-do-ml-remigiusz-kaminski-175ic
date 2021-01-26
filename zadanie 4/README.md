# Web scraping z Beautiful Soup oraz zapis danych do excela za pomocą openpyxl

## Zaczynamy od stworzenia trzech różnych arkuszy w naszym workbooku, odpowiadające trzem zadaniom do wykonania:
wb to nasz obiekt workbook, nazwa metody create_sheet mówi sama za siebie
gielda = wb.create_sheet("Giełda")
linki = wb.create_sheet("Linki")
filmweb = wb.create_sheet("Filmweb")

## Część 1 - giełda - zadanie polega na ekstrakcji danych ze strony przedstawiającej dane giełdowe, z trzech podstron różnych firm oznaczonych trzyznakowym skrótem, który będzie wyszukiwany losowo

## Generacja trzyznakowego kodu firmy

def code_generator(size=3, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars)for _ in range(size))
    
Definiujemy funkcje o nazwie code_generator, która w parametrze przyjmie rozmiar 3, oraz typ znaków, z którego ma składać się kod, następnie iterujemy "size" ilość razy zwracając losowy znak o typie podanym w parametrze

## Definicja funkcji sprawdzającej, czy otwarta strona nie jest stroną z błędem:

def get_right_pages(code):
    url = "https://stooq.pl/q/?s=" + code
    result_code = rq.get(url)
    result_text = result_code.text
    print(url)
    soup = BeautifulSoup(result_text, "html.parser")
    try:
        get_data("Kurs", soup)
        results.append(result_code)
    except AttributeError:
        return

w parametrze przyjmuje kod, przechodzi do niej, oraz próbuję pobrać Kurs, jeżeli się nie uda, wychodzi, będziemy tę funkcję później zapętlać, aby uzyskać 5 prawidłowych stron

## Definicja metody pobierającej określony element określony tagiem podanym w parametrze

def get_data(attribute, soup):
    ref = soup.find(text=attribute).parent.find("span")
    if ref.text == "":
        return 0
    if attribute == "Transakcje":
        return int(ref.text.replace(" ", ""))
    return float(ref.text.replace(" ", ""))
    
w parametrze podajemy string z nazwą atrybutu, do pożądanej wartości, której się odnosi, oraz obiekt typu soup przygotowywany podczas egzekucji metody get_right_pages

## Metoda wypełniająca arkusz ściągniętymi danymi
def fill_sheet(results):
    i = 0
    for col in gielda.iter_cols(min_row=1, max_col=4, max_row=5):
        for cell in col:
              soup = BeautifulSoup(results[i].text, "html.parser")
              if cell.col_idx == 1:
                cell.value = soup.find(id="ta_s").findChild(id='f10').text
              elif cell.col_idx == 2:
                cell.value = get_data("Kurs", soup)
              elif cell.col_idx == 3:
                 cell.value = get_data("Zmiana", soup)
              elif cell.col_idx == 4:
                cell.value = get_data("Transakcje", soup)
              i += 1
              if i == 5:
                i = 0

iterujemy kolumny oraz wiersze, stopniowo uzupełniając o dane, poprzez wywołanie metody soup_find

## Wywołanie metod oraz wyświetlenie wyniku
while len(results) < 5:
    generated_code = code_generator()
    get_right_pages(generated_code)
    print(results)
fill_sheet(results)

for col in gielda.iter_cols(min_row=1, max_col=4, max_row=5):
        for cell in col:
            print("Cell: ",cell," Value: ",cell.value)
            
## Część 2 - linki - zapisanie wszystkich odnośników na stronie - wybrałem ebay

url = "https://www.ebay.com/"
result = rq.get(url)
result_txt = result.text
soup = BeautifulSoup(result_txt, "html.parser")
lista_znalezionych = soup.find_all('a', href=True)
lista_linkow = []
for znaleziony in lista_znalezionych:
    link = znaleziony.get("href")
    if url not in link:
        link = "https://www.ebay.com/" + link
    lista_linkow.append(link)
    i = 0
for row in linki.iter_rows(min_row=1, max_row=len(lista_linkow)):
    for cell in row:
        cell.value = lista_linkow[i]
        i += 1
for row in linki.iter_rows(min_row=1, max_row=len(lista_linkow)):
    for cell in row:
        print("Cell: ",cell," Value: ",cell.value)

W zasadzie nie ma tu nic nowego, warta uwagi jest metoda: 
## soup.find_all('a', href=True)
która zbiera wszystkie elementy "a" z tagiem href, co odpowiada za odnośnik, innymi słowy link, który nas interesuje, następnie sprawdzamy czy link nie znajduje się już na liście i uzupełniamy arkusz

## Część 3 - filmweb - zebranie informacji o danym filmie
W tym bloku kodu mamy prezentacje różnych wariantów metody find, czy to przez klasę, czy div, czy itemprop, po zebraniu danych za jej pomocą uzuepłniamy arkusz i zapisujemy go wraz z dwoma pozostałymi

    
    
