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



def load_jobs_from_db():   #loading all the jobs in the apply section 
    with engine.connect() as conn:
    
        result = conn.execute(text("select * from jobs"))
    
        jobs = []
        for row in result.all():
            jobs.append(dict(row._mapping))
    return jobs       #this function would return the list of jobs 


def load_job_from_db(id):   #loading the single job for the job page to be displayed 
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs where id = :val"), 
                             {"val": id})
        rows = result.all()
        if len(rows)== 0 : #does not exist 
            return None 
        else: 
            return dict(rows[0]._mapping) #important to put mapping 

    