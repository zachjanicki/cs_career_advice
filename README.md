# CS Career Advice

Website for career advice in computer science

**Building Locally:**

Make sure you have Flask installed on your machine
<pre>
$ pip install Flask 
$ python main.py
</pre>
You should get a message saying debugger is active 
The site can be accessed in your browser at http://localhost:5000/

Or run it in the background so that your terminal isn't peppered with GET request messages.
Just don't forget to kill it when you're done!


#Guide to contributing

We want as many people as possible to contribute to this site. Thus, we've layed out some steps to the various ways in which you can contribute to the site. Please note that we will review all contributions to make sure that the information is appropriate, informative, and substantive. We may ask for clarification or further explanation for edits and answers. 

#####  Interview questions/answer

1) Add an interview question:
-    First, go into main.py and scroll down to the function interview_question_section_main. Find your question category and add the question title to the question list. The question title should be descriptive, short, can contain spaces, and should be formated with title capitalization. 
-    Second, go templates/questions and find the directory that marks your question category (Strings-and-Arrays, Graphs, etc). Navigate into the correct category and create your question html page. This page should be named exactly what you named your question in main, except insert dashes (-) where spaces were in your question title. 
-    If you would like to answer the interview question as well as add it, scroll down for information.

2) Add an interview answer:
-   Too add an interview answer, navigate to templates/questions and choose the directory that matches the category of the question you'd like to answer. Then, edit the html document for your question. 

3) Add advice to freshman/sophomores/juniors/seniors:
-   Simply submit a pull request with the edits to the appropriate html document. 

####  Design

It's probably pretty clear that Pierce and I are not design experts...
It would be very helpful if someone wanted to help out and make the site prettier or easier to navigate. The current standard page design can be found in ./templates/layout.html
We would prefer to stick with Bootstrap and keep the general layout idea pretty similar to what currently exists, but we would certainly appreciate any and all suggestions for design improvements.

**General Layout:**

Flask is a python web framework that lets you essentially build the back end of a website and 
use Jinja templating in your HTML files (essentially variables in HTML, see any of the pages as an example. They're hard to miss)

The file system of the project is very simple:
It's state as of 3/30/16 is below

<pre>
.
├── README.md
├── main.py
├── statics
│   └── css
│       └── main.css
└── templates
    ├── firstInternship.html
    ├── freshmanAdvice.html
    ├── gradSchool.html
    ├── index.html
    ├── interviewQuestionTypeTemplate.html
    ├── interviewQuestions.html
    ├── juniorAdvice.html
    ├── layout.html
    ├── question.html
    ├── questions
    │   ├── Graphs
    │   │   ├── Delete-from-Binary-Search-Tree.html
    │   │   ├── Insert-into-Binary-Search-Tree.html
    │   │   └── Level-Order-Traversal.html
    │   ├── Linked-Lists
    │   │   ├── Detect-a-Cycle.html
    │   │   └── Reverse-a-Linked-List.html
    │   ├── Recursion-And-Dynamic-Programming
    │   │   ├── Fibonacci-Sequence.html
    │   │   ├── Max-Path-Grid.html
    │   │   ├── N-Step-Problem.html
    │   │   ├── Pot-of-Gold.html
    │   │   └── Tower-of-Hanoi.html
    │   ├── Search
    │   │   └── Binary-Search.html
    │   ├── Sorting
    │   │   ├── Merge-Sort.html
    │   │   ├── Quick-Sort.html
    │   │   ├── Radix-Sort.html
    │   │   └── Sort-a-Linked-List.html
    │   └── Strings-And-Arrays
    │       ├── Find-Missing-Element.html
    │       ├── Reverse-a-String.html
    │       ├── String-to-Int.html
    │       └── Word-Frequency.html
    ├── resources.html
    ├── seniorAdvice.html
    └── sophomoreAdvice.html
    </pre>
