
from flask import Flask, jsonify
from dotenv import load_dotenv

import database
from auth import require_api_key
from routes import students_bp

load_dotenv()

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Student Management REST API",
        "status": "Running"
    })


# Register student routes
app.register_blueprint(
    students_bp,
    url_prefix="/api"
)


# Protect all student API routes
for endpoint in list(app.view_functions):
    if endpoint.startswith("students."):
        app.view_functions[endpoint] = require_api_key(
            app.view_functions[endpoint]
        )


if __name__ == "__main__":
    database.create_table()
    print("Student Management REST API is running!")
    app.run(debug=True)
