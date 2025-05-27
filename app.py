from flask import Flask , render_template
from flask import jsonify
app = Flask(__name__)

JOBS = [{
    'id' :1, 
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 100,000'
},
{
    'id' :2, 
    'title': 'FrontEnd Engineer',
    'location': 'Hyderabad, India',
    'salary': 'Rs. 80,000'
},
{
    'id' :3, 
    'title': 'Backend Engineer',
    'location': 'Delhi, India',
    'salary': 'Rs. 110,000'

},
{
    'id' :4, 
    'title': 'Data Scientist',
    'location': 'Mumbai, India',
    'salary': 'Rs. 120,000'
},
]

@app.route("/")
def function():     
    return  render_template('home.html', jobs = JOBS)

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host = "127.0.0.1", debug = True)

