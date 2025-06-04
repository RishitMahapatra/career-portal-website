from flask import Flask , render_template
from flask import jsonify, request
from database import engine #importing the engine connection from the database.py Note that other files can be also treated as modules
from sqlalchemy import text 
from database import add_app_to_db
from database import load_jobs_from_db, load_job_from_db , load_application

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
        return "Page Not Found :(", 404 
    return render_template("job_page.html", job = job)

from flask import Flask, render_template, request, redirect, url_for
# other imports...

from flask import request, redirect, url_for

@app.route("/job/<id>/apply", methods=["GET", "POST"])
def apply_to_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Job not found", 404    

    if request.method == "POST":
        application_data = {
            "full_name": request.form.get("full_name"),
            "email": request.form.get("email"),
            "linkedin_url": request.form.get("linkedin_url"),
            "education": request.form.get("education"),
            "work_experience": request.form.get("work_experience"),
            "resume_url": request.form.get("resume_url")
        }

        # ✅ Store in DB
        add_app_to_db(id, application_data)

        # ✅ Redirect to success page
        return redirect(url_for("show_success", id=id))

    return render_template("application_form2.html", job=job)


@app.route("/job/<id>/apply/success")
def show_success(id):
    job = load_job_from_db(id)
    return render_template("success.html", job=job)




if __name__ == "__main__":
    app.run(host = "127.0.0.1", debug = True)

