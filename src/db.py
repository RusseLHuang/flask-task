import sqlalchemy as db
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import g
from flask import current_app

Base = declarative_base()

def get_db():  
  if "db" not in g:
    db_host = current_app.config['DB_HOST']
    db_port = current_app.config['DB_PORT']
    db_user = current_app.config['DB_USER']
    db_pass = current_app.config['DB_PASS']
    db_name = current_app.config['DB_NAME']

    g.db = db.create_engine(f'mysql+mysqlconnector://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}')
  
  return g.db

def get_db_session():
  if "db" not in g:
    engine = get_db()
    g.db.Session = sessionmaker(bind=engine)
  
  return g.db.Session

def close_db(e=None):
  """If this request connected to the database, close the
  connection.
  """
  db = g.pop("db", None)

  if db is not None:
    db.dispose()

def init_app(app):
  app.teardown_appcontext(close_db)
  with app.app_context():
    get_db()