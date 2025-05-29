import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text 

db_user = 'root'
db_password = 'password'
db_host = 'localhost'
db_port = 3306
db_name = 'careerbridge'

DATABASE_URL = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(DATABASE_URL)





    