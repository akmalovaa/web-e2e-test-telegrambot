# Telegram bot web E2E тестирование
Cервис для анализа свойств и корректности работоспособности сервисов и услуг, доступных через web-интерфейс

[Demo video](https://github.com/akmalovaa/web_e2e_test_telegrambot/blob/main/demo.mp4) (на видео без отправки отчетов, на текущий момент есть возможность отправлять Allure отчеты)

## Концепция:
Данный сервис дает возможность отправить ссылку на web-приложение, описать сценарий тестирования, а на выходе получить отчеты и видеозапись с взаимодействием тестов и страниц web-приложения.


## Что нужно доделать:
- для telegram бота сделать отдельный контейнер + poetry
- web front лучше чем телеграм бот (лучше переписать на django)
- pytest нормальные тесты и возможность принимать раличные тест кейсы

## Под капотом
- Pystest
- Allure
- Selenium 4
- Python-telegram-bot


## Запуск


```bash
python -m venv venv
source venv/bin/activate
```

## Зависимости

```bash
pip3 install --no-cache-dir -r requirements.txt
```

## Запуск сервисов:
```bash
docker-compose up
```

```bash
pytest -vv -q --browser_name="chrome" --alluredir=results/projects/{id}/reports
```

## Chrome:
```bash
pytest -vv -q --browser_name="chrome" --alluredir=results/allure_reports
```

## Firefox:
```bash
pytest -vv -q --browser_name="firefox" --alluredir=results/allure_report
```


## Firefox + Chrome:
```bash
$ pytest -n2 -vv -q --browser_name="chrome" -q --browser_name="firefox" --alluredir=results/allure_report
```


## Отчеты Allure

Использовать API документация http://allure:5050

