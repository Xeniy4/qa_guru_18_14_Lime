## Простые тесты для интернет-магазина Lime

[Lime](https://lime-shop.com/ru_ru)

---
> Оперативно интерпретируя подиумные тренды, LIMÉ поощряет креативный подход 
> к составлению гардероба. Каждый потребитель выбирает среди многообразия ассортимента то, 
> что лучше всего отражает его индивидуальность.
 
<img src="https://cache-limeshop.cdnvideo.ru/limeshop/static/3101.jpg">


Список проведенных проверок:
- Авторизация
- Поиск магазина
- Карточки товара
- Подписка на рассылку
- Работа поиска

---

Проект реализован с использованием актуальных инструментов:  
 <img src="media/icons/python.svg" width="50">  <img src="media/icons/selene.png" width="50"> <img src="media/icons/pytest.png" width="50"> <img src="media/icons/jenkins.png" width="50"> <img src="media/icons/selenoid.png" width="50"> <img src="media/icons/allure_report.png" width="50"> <img src="media/icons/allure_testops.png" width="50"> <img src="media/icons/jira.png" width="50"> <img src="media/icons/tg.png" width="50">  


- Язык программирования `Python`
- Фреймворк для написания UI тестов `Selene` с использованием `Selenium WebDriver`
- Фреймворк модульного тестирования `Pytest`
- Выполнение удаленного запуска тестов с помощью `Jenkins` с использованием `Selenoid`
- Фреймворки для сбора отчетности и хранения файлов тестирования `Allure Report`
- Инструмент для сбора и хранения статистики тестов `Allure TestOps`
- Интеграция с системой управления проектами `Jira` + `Allure TestOps`
- Краткие отчеты в `Telegram` отправляет `Telegram Bor`

---

### Локальный запуск
Перед запуском в корне проекта создать файл .env с содержимым:
```
SELENOID_LOGIN=user1
SELENOID_PASS=1234
SELENOID_URL=selenoid.autotests.cloud
```

Для локального запуска необходимо выполнить:
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest .
```

---
### Удаленный запуск тестов выполняется в Jenkins
Посмотреть и запустить можно на странице проекта в [Jenkins](https://jenkins.autotests.cloud/job/018_Xeniy4_Lime/).

Для запуска тестов необходимо:
1. Перейти на [проект](https://jenkins.autotests.cloud/job/018_Xeniy4_Lime/)
2. Нажать на кнопку `Build now`
3. Дождаться окончания тестирования
4. Нажать на кнопку `Allure Report` <img src="media/icons/allure_report.png" width="15">

Откроется страница отчета

<img src="media/images/AllureReport.png">

Детальная информация с шагами и аттачментами отображается в разделе `Suites`

<img src="media/images/AllureReport2.png">

### Статистика отчета хранится в Allure TestOps
Последний отчет можно посмотреть по [ссылке](https://allure.autotests.cloud/project/4689/test-cases/37241?treeId=0)  
Для просмотра статистики после запуска в Jenkins в шаге 4 необходимо нажать на кнопку `Allure TestOps` <img src="media/icons/allure_testops.png" width="15">

<img src="media/images/TestOps1.png">

Детальная информация по тест-кейсам

<img src="media/images/TestOps2.png">

Дашборд со статистикой и графиками запусков

<img src="media/images/TestOps3.png">


### Интеграция с Jira
[Задача-1428](https://jira.autotests.cloud/browse/HOMEWORK-1428)

<img src="media/images/Jira.png">


### Отчет о результатах тестирования в Telegram
Отчеты приходят в канал [Allure_channel](https://t.me/Allure_channel_autotests)

<img src="media/images/telegram.png">








