# FastAPI app for virtual internship

# How to start:

- clone this repository
- connect your database(sql_app/database.py)
- create migration files(alembic revision --autogenerate -m 'any_name')
- migrate in database(alembic upgrade head)
- run server(uvicorn main:app --reload)


File '.env.example' includes environment variables required to connect the database.



