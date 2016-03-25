from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/Advice-By-Year=<year>')
def advice_by_year(year):
	return render_template(year + "Advice.html", year = year)

@app.route('/resources/')
def resources():
	return render_template("resources.html")

@app.route('/interview-questions/')
def interview_questions():
	return render_template("interviewQuestions.html")
@app.route('/grad-school/')
def grad_school():
	return render_template("gradSchool.html")

@app.route('/senior-advice/')
def senior_advice():
	return render_template("seniorAdvice.html")



if __name__ == "__main__":
	app.run(debug=True)
