# Problem 2 Questions

## Which library did you choose?
Flask

## Did you encounter any difficulties while going through the tutorial/quickstart?  How did you resolve them?
Didn't find a specific way to store data, so I searched for other tutorials.

## Referencing the documentation, what is an important class that the library provides? Explain (in your own words) what it does.
Request: Handle the HTTP requests. For example, request.method can be used to differentiate the user's method (post, get, patch, delete, put), and request.form[''] can be used to store the data in dictionary.

## Referencing the documentation, what is an important function that the library provides? Explain (in your own words) what it does.
app = Flask(__name__) is the most important one. It enables the process know where to start running the Flask framework.