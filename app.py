from flask import Flask, render_template, jsonify



app = Flask(__name__)

JOBS =[
  {
    'id': 1,
    'title': 'Data Analysts',
    'location': 'Ghana, Accra',
    'Salary': 'GH¢ 2000'
    
  },
   {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Ghana, Kumasi',
    'Salary': 'GH¢ 2,500'
    
  },
 {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote'
    
    
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'Salary': '$ 12,500'
    
  },
]

@app.route("/")

def hello_world():
  return render_template('home.html', jobs = JOBS, company_name = 'Lamini')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug = True)
