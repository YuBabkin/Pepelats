Проект Пепелац. 
============================

Проект на языке python призван организовать работу с данными данными tle, рассчётами положения спутников по алгоритмам SGP и всё такое...

* * *

В проекте:

### класс ReadTLE

в классе есть следующие поля:

- name --- имя спутника
- line1 --- первоя строка
- line2 --- вторая!
- MJD --- модифицированная юлианская дата привязки эфемерид аппарата

 И вот такие функции:

- **ReadTLE_sat**(catalog_file, SatName) --- чтение каталога ТЛЕ полностью
- **ReadFullTLE**(catalog_file) --- чтение информации из каталога по определённому спутнику
- **GetLine**(SatName) --- возвращает данные по спутнику

### модуль sgp4 

Написан нам неизвестным хорошим человеком, мы позаимствовали этот молуль и ничего внутри не меняли.

* * *

#### Планируем устроить следующий функционал: 

- чтение данных каталогов *.tle
- для произвольного спутника (по его имени) выводить данные о параметрах его орбиты
- рассчёт геоцентрических координат спутника на произвольный момент времени
- построение графиков зависимостей всяких величин от времени

* * *

