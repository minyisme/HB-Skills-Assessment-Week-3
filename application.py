from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("homepage.html")

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

@app.route("/application-form")
def application_page():
    """Show an application form page.

    Form includes input of first_name, last_name, salary, and job_title."""

    return render_template("application_form.html")

@app.route("/application", methods=["POST"])
def route_application():
    """Shows a results page based on form info from the application_form.

    Assigns each item of first_name, last_name, salary, and job_title from
    the application_form.html page to send to application_results.html 
    page."""

    app_first_name = request.form.get("first_name")
    app_last_name = request.form.get("last_name")
    app_salary = request.form.get("salary")
    app_job_title = request.form.get("select_job")

    return render_template("application_results.html",
                            first_name=app_first_name,
                            last_name=app_last_name,
                            salary=app_salary,
                            job_title=app_job_title)
    

if __name__ == "__main__":
    app.run(debug=True)
