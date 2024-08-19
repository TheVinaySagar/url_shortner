# FastAPI URL Shortener

This is a simple URL shortener application built with FastAPI and PostgreSQL. The application allows you to shorten URLs and then redirect to the original URL using the shortened version.

## Features

- Shorten long URLs
- Redirect to the original URL using the shortened URL
- Simple HTML interface for inputting URLs and generating shortened URLs

## Requirements

- fastapi==0.95.1
- uvicorn==0.22.0
- sqlalchemy==2.0.20
- psycopg2-binary==2.9.7
- jinja2==3.1.2
- pydantic==2.0.1
- alembic==1.10.1

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/TheVinaySagar/url_shortener.git
cd url_shortener
```

### 2. Set Up a Virtual Environment (Optional but Recommended)

Create a virtual environment to isolate your project dependencies.

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install the Dependencies

Install the necessary Python packages using pip:

```bash

pip install -r requirements.txt
```
### 4. Set Up the PostgreSQL Database

1. Create a Database:
    Open your PostgreSQL client (like psql) and create a database:

```sql
CREATE DATABASE url_shortener;
```

2. Update the Database URL:
    In your .env file, set the DATABASE_URL to point to your PostgreSQL database:

```python
DATABASE_URL=postgresql://username:password@localhost/mydb
```
### 5. Apply Database Migrations

Use Alembic to apply the migrations and set up the database schema:

```bash
alembic upgrade head
```
### 6. Run the Application

Start the FastAPI application using Uvicorn:

```bash
uvicorn app.main:app --reload
```

