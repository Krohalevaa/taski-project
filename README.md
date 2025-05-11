# Taski Project

Docker-based microservice application, состоящая из четырёх сервисов:

- **db**: PostgreSQL 13  
- **backend**: Python-сервис (FastAPI/Django)  
- **frontend**: SPA (React/Vue/Angular)  
- **gateway**: Nginx (реверс-прокси + статика)

---

## 🚀 Быстрый старт

1. Клонируйте репозиторий и перейдите в папку проекта:
   ```bash
   git clone https://github.com/Krohalevaa/taski-project.git
   cd taski-project
   ```

2. Скопируйте пример `.env.example` в `.env` и задайте свои параметры:
   ```bash
   cp .env.example .env
   # Отредактируйте .env:
   # POSTGRES_USER=taski
   # POSTGRES_PASSWORD=changeme
   # POSTGRES_DB=taski_db
   # DATABASE_URL=postgresql://taski:changeme@db:5432/taski_db
   # SECRET_KEY=your_secret_key_here
   # REACT_APP_API_URL=http://localhost:8000/api
   ```

3. Поднимите весь стек:
   ```bash
   docker-compose up --build -d
   ```

4. Откройте в браузере:
   - API:  http://localhost:8000/api/  
   - Приложение: http://localhost/

---

## 🎯 Архитектура

```text
┌───────────┐     ┌───────────┐     ┌───────────┐     ┌───────────┐
│  Clients  │ →→  │  Gateway  │ →→  │  Backend  │ →→  │    DB     │
│ (Browser, │     │ (Nginx)   │     │ (FastAPI) │     │(Postgres) │
│  Mobile)  │     └───────────┘     └───────────┘     └───────────┘
│           │ ↘                           ↑
│    SPA    │  └─── Static files (vol) ──┘
└───────────┘
```

- **gateway** (`./gateway/`)  
  Nginx-конфиг: реверс-прокси для API и отдача статики из Docker-volume `static`.  
- **backend** (`./backend/`)  
  Python-приложение на FastAPI или Django.  
- **frontend** (`./frontend/`)  
  SPA-приложение на React/Vue, сборка в папку `build/`.  
- **db**  
  Официальный образ Postgres:13, данные хранятся в volume `pg_data`.  

---

## ⚙️ Переменные окружения

Пример `.env.example`:
```dotenv
# База данных
POSTGRES_USER=taski
POSTGRES_PASSWORD=changeme
POSTGRES_DB=taski_db
DATABASE_URL=postgresql://taski:changeme@db:5432/taski_db

# Backend
SECRET_KEY=your_secret_key_here

# Frontend
REACT_APP_API_URL=http://localhost:8000/api
```

---

## 📂 Структура проекта

```
.
├── backend/                    # Python-сервис
│   ├── app/                    # Исходники приложения
│   └── Dockerfile
├── frontend/                   # SPA-приложение
│   ├── src/
│   └── Dockerfile
├── gateway/                    # Nginx (реверс-прокси + статика)
│   └── Dockerfile
├── docker-compose.yml          # Dev-конфигурация
├── docker-compose.production.yml
├── .env.example                # Пример переменных окружения
└── README.md
```

---

## 🛠️ Полезные команды

- `docker-compose up --build -d`  
  Запустить все сервисы в фоне.  
- `docker-compose logs -f backend`  
  Смотреть логи бэкенда.  
- `docker-compose exec backend bash`  
  Зайти в контейнер бэкенда.  
- `docker-compose down`  
  Остановить и удалить все контейнеры.

---

## 🤝 Вклад

1. Сделайте Fork репозитория.  
2. Создайте ветку:  
   ```bash
   git checkout -b feature/my-feature
   ```  
3. Внесите изменения и залейте их:  
   ```bash
   git commit -am "Добавил новую фичу"
   git push origin feature/my-feature
   ```  
4. Откройте Pull Request.  

---

## 📄 Лицензия

Проект распространяется под [MIT License](LICENSE).  

---

*Автор: Анна Крохалева*  
*Ссылка: https://taski-myhost.zapto.org*  
```