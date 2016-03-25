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
	coding_question_sites = {
	"HackerRank": "https://www.hackerrank.com/",
	"LeetCode": "https://leetcode.com/",
	"Project Euler": "https://projecteuler.net/"

	}
	return render_template("resources.html", coding_question_sites = coding_question_sites)

@app.route('/interview-questions/')
def interview_questions():
	return render_template("interviewQuestions.html")

@app.route('/interview-questions/Strings-And-Arrays')
def strings_and_arrays_questions():
	return render_template("StringsAndArrays.html")

@app.route('/interview-questions/recursion-and-DP')
def recursion_and_DP():
	return render_template("recursionAndDP.html")

@app.route('/interview-questions/graphs')
def graphs():
	return render_template("graphs.html")


@app.route('/grad-school/')
def grad_school():
	return render_template("gradSchool.html")

@app.route('/senior-advice/')
def senior_advice():
	return render_template("seniorAdvice.html")



if __name__ == "__main__":
	app.run(debug=True)
