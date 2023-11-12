from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Signup(db.Model):
    """
    A class to store and structure the data.
    """
    id = db.Column(db.Integer, primary_key=True, unique=True)
    student_name = db.Column(db.String(200), nullable=False)
    course_name = db.Column(db.String(200), nullable=False)
    date_signed_up = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f"<Signup {self.id} - {self.student_name} for {self.course_name}>"


with app.app_context():
    db.create_all()


@app.route('/', methods=['POST', 'GET'])
def index():
    """
    For adding new items into the database.
    Inputs: from the user through the form with student name and course name
    Outputs: added into the database
    """
    if request.method == 'POST':
        student_name = request.form['student_name']
        course_name = request.form['course_name']
        new_signup = Signup(student_name=student_name,
                            course_name=course_name, date_signed_up=datetime.now())
        # The datetime.now() has to be stated, otherwise it will stay as default
        try:
            db.session.add(new_signup)
            db.session.commit()
            return redirect('/') # rerun the index function to have the new added item presented
        except:
            return 'There was an issue with your sign-up' # Handle errors
    else:
        # Handle when a new item is added, the request.method is no long post, will render the html file again
        signups = Signup.query.order_by(Signup.date_signed_up).all()
        # The list is ordered by the timestamp
        return render_template('index.html', signups=signups)


@app.route('/cancel/<int:id>', methods=['GET', 'POST'])
def cancel(id):
    """
    Method to delete the items in the database
    Inputs: id of the going to delete item
    Outputs: Rerender the last function for rerendering/throw an error
    """
    signup_to_cancel = Signup.query.get_or_404(id)

    if request.method == 'POST':
        try:
            db.session.delete(signup_to_cancel)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was a problem canceling your sign-up'


def main():
    # this is the main function, which is the entry point for the program
    # you should write your code in methods and/or functions and have the
    # main function call those functions
    app.run(debug=True)


if __name__ == "__main__":
    main()
