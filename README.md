# FastAPI Book CRUD API

This project exposes a `book` table CRUD API with FastAPI and SQLAlchemy.

## Endpoints

- `GET /` redirects to Swagger UI at `/docs`
- `GET /hello`
- `GET /api`
- `POST /books`
- `GET /books`
- `GET /books/{book_id}`
- `PUT /books/{book_id}`
- `DELETE /books/{book_id}`

## Local Run

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

If `DATABASE_URL` is not set, the app uses local SQLite at `books.db`.

## Render PostgreSQL

1. Create a PostgreSQL database in Render.
2. Copy the Internal Database URL or External Database URL.
3. Set it as the `DATABASE_URL` environment variable on your Render web service.
4. Deploy the app. On startup, FastAPI will create the `book` table automatically.

The app converts Render-style `postgres://...` URLs to the SQLAlchemy `postgresql+psycopg://...` format automatically.
