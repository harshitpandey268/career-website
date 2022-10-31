from flask import Flask, render_template

app = Flask(__name__)
JOBS = [{
  'id': 1,
  'title': 'Machine Learning Engineering Intern',
  'location': 'Bengaluru',
  'salary': '10,00,000'
}, {
  'id': 2,
  'title': 'Data Science Engineering Intern',
  'location': 'New-Delhi',
  'salary': '1,00,00,000'
}, {
  'id': 3,
  'title': 'Software Developer Intern',
  'location': 'Pune',
  'salary': '10,00,00,000'
}]


@app.route("/")
def hello_people():
  return render_template('home.html', jobs=JOBS)


print(__name__)
if __name__ == "__main__":
  app.run('0.0.0.0', debug=True)