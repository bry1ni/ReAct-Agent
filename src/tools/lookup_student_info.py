from langchain_core.tools import tool
import pandas as pd

@tool
def lookup_student_info(student_name: str, student_db_path="data/students.csv")-> str:
    """
    Lookup student information from the database.
    
    Args:
        student_name (str): Name of the student to lookup.
        
    Returns:
        str: Information about the student.
    """
    student_df = pd.read_csv(student_db_path)
    if student_name in student_df["student_name"].values:
        return student_df.loc[student_df["student_name"] == student_name].values[0]
    else:
        return "Student not found."