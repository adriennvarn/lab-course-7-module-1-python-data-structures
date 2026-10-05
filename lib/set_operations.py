# This module contains operations related to sets.

def unique_majors(student_list):
    """
    Uses set comprehension to return a set of unique majors from the list of students.
    """
    return {student[2] for student in student_list}