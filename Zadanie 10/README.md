# Opis poszczególnych sposobów wykonywania operacji
## Standardowe, I/O bound problems - problemy związane z urządzeniami wyjścia/wejścia
Podczas standardowego przetwarzania możemy natknąc się na problem, który polega na czekanie przez program na wejście/wyjście z zewnętrznego źródła, występują często, gdy program <br>
pracuje z elementami wolniejszymi niż procesor komputera.
![image](https://user-images.githubusercontent.com/56388404/110837667-d0d68f80-82a1-11eb-9583-6c62852d0888.png)
Diagram ukazuje podział, w którym komputer oczekuje na zewnętrzne dane, oraz kiedy przetwarza - niebieskie prostokąty - przetwarzanie, czerwone - oczekiwanie. Na pierwszy rzut oka widać, że jest to nieoptymalne. <br>

W przypadku programów nie wykonujących operacji np w filesystemie, lub dostepu do sieci są one bezpośrednio związane z procesorem. Dla porównania diagram przetwarzania takiego programu:
![image](https://user-images.githubusercontent.com/56388404/110837963-33c82680-82a2-11eb-90f5-65d617b33197.png)
Czas realizacji I/O: 14.34741997718811 seconds <br>
Czas realizacji CPU: 25.685487985610962 seconds <br>

## Przetwarzanie z wykorzystanem wątków
Rozdzielając operacje pomiędzy wątkami, niezależnie działającymi od siebie operacjami, możemy zniwelować okres oczekiwania do minimum sprytnie przechodząc między nimi, widoczne jest to na diagramie
![image](https://user-images.githubusercontent.com/56388404/110838343-a507d980-82a2-11eb-9fe2-3a7641bcebd7.png)
Czas realizacji I/O: 3.65730357170105 seconds <br>
Czas realizacji CPU: 16.797247409820557 seconds <br>

## Przetwarzanie z wykorzystaniem Asyncio
Przetwarzanie asynchroniczne, oznacza to w skrócie, że poszczególne zadania, jakie są wykonywane przez proces, grupowane są w taki sposób, aby dwa procesy mogły wykonywać jednocześnie operacje nie zachodzące na siebie. Np jeśli chcielibyśmy kazać dwum procesom wykonywać operacje na urządzeniach wejścia/wyjścia, np zapis pliku, to nie mogłyby one pracować jednocześnie, natomiast gdy jeden z procesów wykonuje opreacje wejścia/wyjścia, a drugi operacje obliczeniowe na procesorze, moga one pracować równocześnie, zapewnia to doskonałą efektywność wykonywanych procesów, gdyż kolokwialnie mówiąc, nie wchodzą sobie w drogę, a zazębiają się, tworzac ciąg operacji które mogą wykonywać jednocześnie.
![image](https://user-images.githubusercontent.com/56388404/110839209-9c63d300-82a3-11eb-90c2-4e76f48d6818.png)
Czas realizacji I/O: 1.68 seconds <br>
Czas realizacji CPU: 20.303478956222534 seconds <br>

## Przetwarzanie z wykorzystaniem multiprocessingu
Multiprocessing pozwala wykorzystać fakt, że nowoczesne procesory są podzielone rdzenie, bądź niefizyczne podgrupy. Dzięki temu, mogą pracować niezależnie od siebie, w efekcie nakładając operacje na siebie bez przerywania sobie nawzajem.
![image](https://user-images.githubusercontent.com/56388404/110839560-f9f81f80-82a3-11eb-958a-da44179f1773.png)
![image](https://user-images.githubusercontent.com/56388404/110839574-fcf31000-82a3-11eb-875b-02f416d29570.png)
![image](https://user-images.githubusercontent.com/56388404/110839584-011f2d80-82a4-11eb-8895-173deebb5da1.png)
Czas realizacji I/O: 5.83 seconds <br>
Czas realizacji CPU: 16.049935817718506 <br>



