from flask import Flask
from in_and_out import in_and_out_bp

app = Flask(__name__)
app.register_blueprint(in_and_out_bp)

if __name__ == "__main__":
    app.run(debug=True)
