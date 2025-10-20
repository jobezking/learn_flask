from flask import Blueprint, request, render_template

# Define a blueprint so it can be imported into app.py
in_and_out_bp = Blueprint("in_and_out", __name__)

@in_and_out_bp.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            num3 = float(request.form["num3"])
            text = request.form["text"]

            avg = (num1 + num2 + num3) / 3
            result = f"{avg} {text}"
        except Exception as e:
            result = f"Error: {e}"

    # Render the template and pass the result (if any)
    return render_template("index.html", result=result)

