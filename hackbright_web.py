"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/")
def start_here():
    """Homepage"""

    return """<html>
                <head>
                    <title>Project Tracker</title>
                </head>
                <body> <h1> Homepage</h1>
                <br>
                <a href= "/student-search"> Search for a student</a>
                <br>
                <a href= "/student-create"> Create a student</a>
                </body>
                </html>"""


#@app.route("/student/<github>")
#def get_student(github):
@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    rows = hackbright.get_grades_by_github(github)

    html = render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github,
                            grades_list=rows)

    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")




@app.route("/student-create")
def student_create():
    """Create a new student"""

    return render_template("student_create.html")




@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a new student."""

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    github = request.form.get('github')

    first, last, github = hackbright.make_new_student(first_name, last_name, github)


    html = render_template("student_confirmation.html",
                            first=first,
                            last=last,
                            github=github)

    return html







if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
