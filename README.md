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

AUTH_TOKEN=HHRU_TEST_WB
BACKEND_PORT=8080
BACKEND_URL=http://back:8000
```

## Запуск
```bash
docker compose up -d --build
#или
docker-compose up -d --build
```

OpenAPI DOC: `http://127.0.0.1:${BACKEND_PORT}`
