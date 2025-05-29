from flask import Flask , render_template
from flask import jsonify
from database import engine #importing the engine connection from the database.py Note that other files can be also treated as modules
from sqlalchemy import text 


app = Flask(__name__)



def load_jobs_from_db():
    with engine.connect() as conn:
    
        result = conn.execute(text("select * from jobs"))
    
        jobs = []
        for row in result.all():
            jobs.append(dict(row._mapping))
    return jobs       #this function would return the list of jobs 





@app.route("/")
def function():     
    jobs = load_jobs_from_db() #this would call the function to get the list of jobs from the db 
    return  render_template('home.html', jobs = jobs) #name used in home.html = name used in getting the list 

@app.route("/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)


if __name__ == "__main__":
    app.run(host = "127.0.0.1", debug = True)

