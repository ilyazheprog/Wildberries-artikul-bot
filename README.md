# wb-artikul-backend-test-assignment

## Конфигурация
Создайте файл `.env` в корне проекта:
```
TOKEN=XXXXXXX

DB_ENGINE=postgresql+psycopg
DB_USER=wb
DB_PSWD=wb
DB_DB=wb
DB_HOST=db
DB_PORT=5432
DB_ECHO=True

BACKEND_AUTH_TOKEN=HHRU_TEST_WB
BACKEND_PORT=8080
BACKEND_URL=http://back:8000

WB_GET_DETAILS_URL=https://card.wb.ru/cards/v1/detail?appType=1&curr=rub&dest=-1257786&spp=30&nm=
WB_MINUTES_TO_UPDATE_SUBSCRIPTIONS=30
```

## Запуск
```bash
docker compose up -d --build
#или
docker-compose up -d --build
```

OpenAPI DOC: `http://127.0.0.1:${BACKEND_PORT}`
