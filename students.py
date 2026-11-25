
from flask import Blueprint, jsonify, request
import database
import sqlite3

students_bp = Blueprint("students", __name__)


@students_bp.route("/students", methods=["GET"])
def get_students():
    students = database.get_all_students()
    return jsonify({
        "message": "Students retrieved successfully",
        "students": students
    }), 200


@students_bp.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    student = database.get_student(student_id)

    if student is None:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(student), 200


@students_bp.route("/students", methods=["POST"])
def add_student():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Please provide JSON data"}), 400

    for field in ["name", "course", "email"]:
        if not isinstance(data.get(field), str) or not data[field].strip():
            return jsonify({"error": f"{field} is required"}), 400

    if "@" not in data["email"] or "." not in data["email"].split("@")[-1]:
        return jsonify({"error": "Invalid email address"}), 400

    try:
        student = database.add_student(
            data["name"].strip(),
            data["course"].strip(),
            data["email"].strip()
        )
        return jsonify({
            "message": "Student added successfully",
            "student": student
        }), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Email already exists"}), 409


@students_bp.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Please provide JSON data"}), 400

    for field in ["name", "course", "email"]:
        if not isinstance(data.get(field), str) or not data[field].strip():
            return jsonify({"error": f"{field} is required"}), 400

    if "@" not in data["email"] or "." not in data["email"].split("@")[-1]:
        return jsonify({"error": "Invalid email address"}), 400

    if database.get_student(student_id) is None:
        return jsonify({"error": "Student not found"}), 404

    try:
        student = database.update_student(
            student_id,
            data["name"].strip(),
            data["course"].strip(),
            data["email"].strip()
        )
        return jsonify({
            "message": "Student updated successfully",
            "student": student
        }), 200
    except sqlite3.IntegrityError:
        return jsonify({"error": "Email already exists"}), 409


@students_bp.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    deleted = database.delete_student(student_id)

    if not deleted:
        return jsonify({"error": "Student not found"}), 404

    return jsonify({"message": "Student deleted successfully"}), 200
