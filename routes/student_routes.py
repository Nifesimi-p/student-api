import logging
from flask import Blueprint, request, jsonify
from models.student import Student
from app import db

# Configure logging for this module
logger = logging.getLogger(__name__)

student_bp = Blueprint('students', __name__)

# Create a new student
@student_bp.route('/', methods=['POST'])
def add_student():
    data = request.get_json()
    logger.info(f"Received data to add student: {data}")
    try:
        new_student = Student(**data)
        db.session.add(new_student)
        db.session.commit()
        logger.info("Student added successfully")
        return jsonify({"message": "Student added"}), 201
    except Exception as e:
        logger.error(f"Error adding student: {e}")
        return jsonify({"error": "Failed to add student"}), 500

# Get all students
@student_bp.route('/', methods=['GET'])
def get_students():
    logger.info("Fetching all students")
    students = Student.query.all()
    result = [
        {"id": s.id, "name": s.name, "age": s.age, "grade": s.grade}
        for s in students
    ]
    return jsonify(result), 200

# Get a specific student by ID
@student_bp.route('/<int:id>', methods=['GET'])
def get_student(id):
    logger.info(f"Fetching student with ID: {id}")
    student = Student.query.get_or_404(id)
    return jsonify({"id": student.id, "name": student.name, "age": student.age, "grade": student.grade}), 200

# Update a student
@student_bp.route('/<int:id>', methods=['PUT'])
def update_student(id):
    logger.info(f"Updating student with ID: {id}")
    student = Student.query.get_or_404(id)
    data = request.get_json()
    try:
        for key, value in data.items():
            if hasattr(student, key):
                setattr(student, key, value)
                logger.info(f"Updated {key} to {value}")
        db.session.commit()
        logger.info(f"Student with ID {id} updated successfully.")
        return jsonify({"message": "Student updated"}), 200
    except Exception as e:
        logger.error(f"Error updating student with ID {id}: {e}")
        return jsonify({"error": "Failed to update student"}), 500

# Delete a student
@student_bp.route('/<int:id>', methods=['DELETE'])
def delete_student(id):
    logger.info(f"Deleting student with ID: {id}")
    student = Student.query.get_or_404(id)
    try:
        db.session.delete(student)
        db.session.commit()
        logger.info(f"Student with ID {id} deleted successfully.")
        return jsonify({"message": "Student deleted"}), 200
    except Exception as e:
        logger.error(f"Error deleting student with ID {id}: {e}")
        return jsonify({"error": "Failed to delete student"}), 500
