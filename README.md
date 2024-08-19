2. Set Up a Virtual Environment (Optional but Recommended)

Create a virtual environment to isolate your project dependencies.

bash

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the Dependencies

Install the necessary Python packages using pip:

bash

pip install -r requirements.txt

4. Set Up the PostgreSQL Database

    Create a Database:

    Open your PostgreSQL client (like psql) and create a database:

    sql

CREATE DATABASE url_shortener;

Update the Database URL:

In your .env file, set the DATABASE_URL to point to your PostgreSQL database:

bash

    DATABASE_URL=postgresql://username:password@localhost/url_shortener

5. Apply Database Migrations

Use Alembic to apply the migrations and set up the database schema:

bash

alembic upgrade head

6. Run the Application

Start the FastAPI application using Uvicorn:

bash

uvicorn app.main:app --reload

7. Access the Application

Open your web browser and navigate to:

arduino

http://127.0.0.1:8000/

Here, you can enter a long URL, and the application will generate a shortened URL.
Usage
Shortening a URL

    Enter a long URL into the text box on the homepage.
    Click the "Shorten URL" button.
    The shortened URL will be displayed, and you can click it to test the redirection.

Redirection

When you click on the shortened URL, you will be redirected to the original long URL.
Troubleshooting
Common Issues

    Port Already in Use: If you get an error that port 8000 is already in use, either stop the process using that port or run Uvicorn on a different port:

    bash

    uvicorn app.main:app --reload --port 8001

    Database Connection Issues: Ensure your PostgreSQL server is running and the connection details in your .env file are correct.

Debugging

If you encounter issues, check the console output for error messages. You can also visit the FastAPI and Uvicorn documentation for further assistance.
License

This project is licensed under the MIT License. See the LICENSE file for more information.
Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
Contact

For any questions or suggestions, feel free to reach out at your.email@example.com.

markdown


### **How to Use This `README.md`**

- **Replace the placeholders** like `https://github.com/yourusername/url_shortener.git` with your actual repository URL and contact information.
- **Add any additional instructions** specific to your project or environment if necessary.

This `README.md` file is designed to guide users through the setup, installation, and usage of your FastAPI URL Shortener project. It also provides troubleshooting tips and general information about the project.

