# Telegram bot web E2E тестирование
Cервис для анализа свойств и корректности работоспособности сервисов и услуг, доступных через web-интерфейс

## Концепция:
Данный сервис дает возможность отправить ссылку на web-приложение, описать сценарий тестирования и прикрепить тесты, а на выходе получить журнал и видеозапись с взаимодействием тестов и страниц web-приложения.


## Что нужно сделать:
- На данный момент за прием и выполнение отвечает телеграм бот в планах перевести на web front
- Использование Allure для вывода отчетов
- Углубление в pytest для более функционального web тестирования

## Дополнительно


- Apache License 2.0
- Docker-compose
- Скорость работы 
- Масштабируемость 
- Простота поддержки
- Читаемость тестов



- Frameworks:
    - Pystest
    - Allure
    - Selenium 4


## Getting Started
Creat a virtual environment:

```bash
$ python -m venv venv
$ source venv/bin/activate
```

Install dependencies:

```bash
$ pip3 install --no-cache-dir -r requirements.txt
```

## Start Selenoid Server:
```bash
$ docker-compose up
```

## To run tests in Chrome and Firefox Browser:
```bash
$ pytest -vv -q --browser_name="chrome" -q --browser_name="firefox" --alluredir=results/allure_report
```

## To run tests in Chrome Browser:
```bash
$ pytest -vv -q --browser_name="chrome" --alluredir=results/allure_report
```

## To run tests in Firefox Browser:
```bash
$ pytest -vv -q --browser_name="firefox" --alluredir=results/allure_report
```

## To run tests in local Chrome Browser:
```bash
$ pytest -vv -q --browser_name="local" --alluredir=results/allure_report
```

## To run tests in parallel mode:
To run more than one test simultaneously, just add the **-n** parameter informing the maximum number of tests to be run simultaneously, the maximum possible number is limited by the number of threads that the processor has to run the tests.
For example to run 2 tests at the same time in chrome and firefox:
```bash
$ pytest -n2 -vv -q --browser_name="chrome" -q --browser_name="firefox" --alluredir=results/allure_report
```


## Reports
> You must have the allure client installed

Run the command below to generate the test report:

```bash
$ allure generate --clean results/allure_report -o results/allure_result 
```

To view the report in the browser:

```bash
$ allure open results/allure_result
```

