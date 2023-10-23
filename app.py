from flask import Flask,render_template,jsonify
app = Flask(__name__)

JOBS = [
  {
    'id' : 1,
    'title': 'Data Analyst',
    'location' : 'Indonesia',
    'Salary': 'Rp. 15.000.000'
  },
  {
    'id' : 2,
    'title': 'Programmer',
    'location' : 'Indonesia',
    'Salary': 'Rp. 25.000.000'
  },
  {
    'id' : 3,
    'title': 'Software Engineering',
    'location' : 'Indonesia'
  },
  {
    'id' : 4,
    'title': 'Dev Ops',
    'location' : 'Indonesia',
    'Salary': 'Rp. 10.000.000'
  }
]

@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name="Rico Malangi")

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)