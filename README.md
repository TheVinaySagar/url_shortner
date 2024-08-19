2. Set Up a Virtual Environment (Optional but Recommended)

Create a virtual environment to isolate your project dependencies.

```bash

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. Install the Dependencies

Install the necessary Python packages using pip:

```bash

pip install -r requirements.txt
```
4. Set Up the PostgreSQL Database

    Create a Database:

    Open your PostgreSQL client (like psql) and create a database:

    ```sql
    CREATE DATABASE url_shortener;
    ```


Update the Database URL:

In your .env file, set the DATABASE_URL to point to your PostgreSQL database:

    ```bash
    DATABASE_URL=postgresql://username:password@localhost/url_shortener
    ```
5. Apply Database Migrations

Use Alembic to apply the migrations and set up the database schema:

    ```bash
    alembic upgrade head
    ```
6. Run the Application

Start the FastAPI application using Uvicorn:

    ```bash
    uvicorn app.main:app --reload
    ```

