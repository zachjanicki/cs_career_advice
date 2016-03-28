from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/firstInternship/')
def firstInternship():
	return render_template('firstInternship.html')

@app.route('/Advice-By-Year=<year>')
def advice_by_year(year):
	return render_template(year + "Advice.html", year = year)

@app.route('/resources/')
def resources():
	coding_question_sites = {
	"HackerRank": "https://www.hackerrank.com/",
	"LeetCode": "https://leetcode.com/",
	"Project Euler": "https://projecteuler.net/",
	"CodeFights": "https://codefights.com/home"
	}
	Tutorials = {
		"Learning Python The Hardway": "http://learnpythonthehardway.org/book/"

	}
	Readings = {
	"Advice from Tim Connors":"https://docs.google.com/document/d/1Ni0deBDKRRWgb5xHY748Ptw6AHhw8Z3mg6LMDFOiAHw/edit",
	"5 Essential Interview Questions": "https://sites.google.com/site/steveyegge2/five-essential-phone-screen-questions",
	"Hacking a Google Interview":"https://courses.csail.mit.edu/iap/interview/materials.php"
	}

	Other = {
	"28 interview questions": "http://www.ardendertat.com/2012/01/09/programming-interview-questions/",
	"Getting a Gig: A Guide": "https://github.com/cassidoo/getting-a-gig"
	}

	Books = {
	"Cracking the coding interview": "http://www.amazon.com/Cracking-Coding-Interview-6th-Edition/dp/0984782850/ref=dp_ob_title_bk",
	"Data Structure and Algorithmic Thinking with Python": "http://www.amazon.com/Data-Structure-Algorithmic-Thinking-Python/dp/8192107590"
	}

	return render_template("resources.html", coding_question_sites = coding_question_sites, Books = Books,
	Tutorials=Tutorials, Readings = Readings, Other = Other)

@app.route('/interview-questions/')
def interview_questions():
	return render_template("interviewQuestions.html")

@app.route('/interview-questions/<question_type>')
def interview_question_section_main(question_type):
	if question_type == "Strings-And-Arrays":
		section_title = "Strings And Arrays"
		questions = ["Reverse a String", "String to Int", "Word Frequency", "Find Missing Element"]

	elif question_type == "Recursion-and-Dynamic-Programming":
		section_title = "Recursion and Dynamic Programming"
		questions = ["Fibonacci Sequence", "N Step Problem", "Tower of Hanoi", "Max Path Grid", "Pot of Gold"]
	elif question_type == "Graphs":
		section_title = "Graphs"
		questions = ["Insert into Binary Search Tree", "Delete from Binary Search Tree", "Level Order Traversal"]
	elif question_type == "Linked-Lists":
		section_title = "Linked Lists"
		questions = ["Reverse a Linked List", "Detect a Cycle"]
	elif question_type == "Sorting":
		section_title = "Sorting"
		questions = ["Sort a Linked List", "Merge Sort", "Quick Sort", "Radix Sort" ]

	elif question_type == "Search":
		section_title = "Search"
		questions = ["Binary Search"]

	num_questions = len(questions)
	url_question_titles = [question.replace(" ", "-") for question in questions]
	return render_template("interviewQuestionTypeTemplate.html",url_question_titles = url_question_titles,
	question_type = question_type, section_title = section_title, num_questions = num_questions,questions = questions)

@app.route('/interview-questions/<question_type>/<question>')
def question(question_type, question):
	"""
	Specific interview question pages genereted here
	This will create the question title and path to the html page for a specific question that will be 
	inserted into question.html

	"""
	question_title = question.replace("-", " ")
	question_path = "questions/{}/{}.html".format(question_type, question)
	return render_template("question.html", question_title = question_title, question_path = question_path)

@app.route('/grad-school/')
def grad_school():
	return render_template("gradSchool.html")

@app.route('/senior-advice/')
def senior_advice():
	return render_template("seniorAdvice.html")



if __name__ == "__main__":
	app.run(debug=True)
