Testing

В тестовом задании 2 автотестирование происходит с помощью Travis Ci, которому нужен конфигурационный файл travil.yml c указанием аргументов для параметров теста в файле и для запуска автотеста. Вывод результатов в Allure возможно с помощью библиотеки allure через указание директории (pytest allure-dir=%directory% где будут размещены файлы allure, используемые для отображения результатов и степов в браузере. Для выполнения автотестов Travis Ci в Docker travis.yml вписываются соответствующие команды.

## Тестовый план по 1 заданию

- Будут написаны 2 html страницы с формами: страница с формирование заявки на закупку (указываются марка, количество, модель и т.д.) и страница с отображением всех ранее оформленных заявок для их корректировки. Соответственно на 1 странице делается sql запрос INSERT, а во второй SELECT *, затем после вывода заявок DELETE либо UPDATE после запроса на стороне сервера. Печать осуществляется с помощью кнопки, которая будет создана на 2-ой странице где отображены все данные о заявках.
- Будут подняты 2 сервера: sql и IBM MQ через привязку библиотеки python pymqi 
- mq сервер принимает сообщение с запросом, парсит значения формы и выполняет запрос в SQL
- с учетом того что пользователи работают одновременно скорее всего потребуется многопоточность и распалалеливание вышесказанного функционала c помощью библиотеки threading. Будет создан пул из 500 потоков, которые будут принимать сообщения от mq и дальнейшие действия с этим сообщениям будут происходить в отдельном потоке. Таким образом будет возможна обработка запросов 500 пользоватлей одновременно.

### Протестировать можно нагруженность: 
Соответственно чтобы cкорость сохранения и выгрузки заявок составляла не более 3 секунды:
- Импортируем библиотеку time и фиксируем время до начала обработки запроса
- После окончания обработки текущее время отнимаем от зафиксированного ранее и определяем время обработки сохранения либо выгрузки
- Значение сравнивается с числом 3 вида "assert value < 3"

Cкорость формирования отчета тестируется точно также.