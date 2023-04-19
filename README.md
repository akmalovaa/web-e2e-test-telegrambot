# Telegram bot web E2E тестирование
Cервис для анализа свойств и корректности работоспособности сервисов и услуг, доступных через web-интерфейс

[Demo video](https://github.com/akmalovaa/web_e2e_test_telegrambot/blob/main/demo.mp4) (на видео без отправки отчетов, на текущий момент есть возможность отправлять Allure отчеты)

## Концепция:
Cервис который дает возможность отправить web ссылку, описать сценарий тестирования, а на выходе получить отчеты + видеозапись с взаимодействием тестов и страниц web-приложения.


## Что нужно доделать:
- telegram бота собрать в docker как отдельный сервис и добавить в общий docker-compose (python image + poetry)
- web front удобнее, чем телеграм бот (лучше переписать на django)
- pytest модули для тестов и возможность принимать раличные тест кейсы на входе

## Под капотом
- Pytest
- Allure
- Selenium
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

## Для дебага:
```bash
pytest -vv -q --browser_name="chrome" --alluredir=results/projects/{id}/reports
```

Chrome:
```bash
pytest -vv -q --browser_name="chrome" --alluredir=results/allure_reports
```

Firefox:
```bash
pytest -vv -q --browser_name="firefox" --alluredir=results/allure_report
```

Firefox + Chrome:
```bash
pytest -n2 -vv -q --browser_name="chrome" -q --browser_name="firefox" --alluredir=results/allure_report
```


## Отчеты Allure

Использовать API документацию http://allure:5050

## Аналоги

OpenSource проекты

[Testsigma](https://github.com/testsigmahq/testsigma) - шикраный проект, есть все задуманное, кроме записи видео

[Salvation](https://github.com/hanwenlu2016/Salvation) - задумкая такая же, только уже продумано и сделано на django - можно сделать форк, подправить некоторые мометы и собрать в единый docker-compose

