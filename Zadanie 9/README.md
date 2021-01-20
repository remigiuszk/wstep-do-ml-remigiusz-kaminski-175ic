#Opis metod OpenCV
####Do wyświetlania przetworzonych obrazów w notebooku użyłem innej biblioteki, OpenCV otwierał mi je w nowym oknie
##img.shape()
jedna z podstawowych metod, w programie używamy jej do zwrócenia szerokości, wysokości oraz głębokości obrazka(liczbe kanałów obrazka, w tym przypadku 3 - od RGB)

##cv2.imshow()
jako parametry przyjmuje nazwe obrazka oraz obiektu obrazu, wyświetla dany obraz w nowym oknie
##cv2.waitKey(0)
czeka na klawisz od użytkownika, potrzebne jest to aby okno z obrazem za szybko się nie zamknęło
##(B, G, R) = image[15, 99]                 
##print("R={}, G={}, B={}".format(R, G, B)) 
Zapis ten pozwala nam odczytać dane z kanałów w danym pikselu, wartości w nawiasie kwadratowym przedstawiają położenie porządanego piksela w rzędach i kolumnach
##ROI
region of interest - obszar obrazu który jest rozpoznawany jako istotny, np twarz człowieka na zdjeciu
##image2[20:280, 260:490] 
zapis ten pozwala na przycięcie obrazu wg parametrów, które podajemy wg wzoru:
obraz[wysokoscStart:wysokoscKoniec, szerokoscStart,szerokoscKoniec]
## resize(image, (200, 200)) 
zmiana rozdzielczości obrazka na rozmiar podany w parametrach
## imutils.resize(image, width=300)
metoda z biblioteki imultis pozwalajaca na automatyczne przeskalowanie obrazu do danego rozmiaru z zachowaniem proporcji
##cv2.getRotationMatrix2D(center, -45, 1.0)
ten zapis pozwala na stworzenie macierzy obrotu o 45 stopni wg wskazowek zegara
##cv2.warpAffine(image, M, (w, h))
metoda pozwalająca na zakrzywienie obrazu korzystając ze wcześniej zadeklarowanej macierzy
##cv2.GaussianBlur(image, (11, 11), 0) 
Rozmycie gaussa, w parametrach podajemy obraz, oraz kernel jako wejście
##cv2.rectangle(output, (490, 260), (280, 20), (0, 255, 255), 2) 
Rysowanie prostokątu na podanym zdjęciu, parametry:
1 - zdjecie
2 - szerokosc koniec, poczatek
3 - wysokosc koniec, poczatek
4 - kolor
5 - grubosc linii
##cv2.circle(output, (390, 170), 20, (255, 0, 0), -1)
rysowanie koła na obrazie - parametry:
1- zdjecie
2 - współrzędne środka koła
3 - promień w pikselach
4- kolor
5-typ linii
##cv2.line(output, (180, 200), (390, 170), (0, 0, 255), 5)
rysowanie linii na obrazie - parametry:
1 - zdjecie
2 - początek
3- koniec
4- kolor
5- grubość linii
##cv2.putText(output, "OpenCV + Jurassic Park!!!", (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
Wstawianie tkestu do obrazku - parametry:
1 - obraz,
2 - treść
3 - lokacja
4 - font
5 - skala
6 - kolor
7 - grubość
##cv2.Canny(gray, 30, 150)
wyodrębnianie krawędzi z obrazu w skali szarości, jako parametry przyjmuje szary obraz oraz progi wykrywania
## cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
filtrowanie obrazu po podanych progach skali szarości
##cv2.erode(mask, None, iterations=5)
Usuwanie szumów, w parametrze podajemy obraz oraz liczbe iteracji, które zostaną wykonane usuwając zbędne piksele powstałe przy thresholdingu



