from flask import Flask , render_template
from flask import jsonify
from database import engine #importing the engine connection from the database.py Note that other files can be also treated as modules
from sqlalchemy import text 
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)






@app.route("/")
def function():     
    jobs = load_jobs_from_db() #this would call the function to get the list of jobs from the db 
    return  render_template('home.html', jobs = jobs) #name used in home.html = name used in getting the list 

@app.route("/jobs")  
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)


@app.route("/job/<id>") #for single job page 
def show_job(id):
    job = load_job_from_db(id)
    if not job: #if the job list is empty 
        return "Page Not Found", 404 
    return render_template("job_page.html", job = job)


if __name__ == "__main__":
    app.run(host = "127.0.0.1", debug = True)

