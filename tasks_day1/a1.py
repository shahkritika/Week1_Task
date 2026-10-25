"""Task A1"""

def main():
    print("=" * 60)
    print("Task A1: 5 Variables of Different Types & Their Types")
    print("=" * 60)

    student_id = 101

    gpa = 3.85
    
    course_name = "Full-Stack Developer"
    
    is_active = True
    
    tech_stack = ["Python", "Git", "Linux", "SQL", "FastAPI", "React"]

    # Displaying each varaibles
    print(f"1. Variable 'student_id'   : Value = {student_id:<30} | Type = {type(student_id)}")
    print(f"2. Variable 'gpa'          : Value = {gpa:<30} | Type = {type(gpa)}")
    print(f"3. Variable 'course_name'  : Value = {course_name:<30} | Type = {type(course_name)}")
    print(f"4. Variable 'is_active'    : Value = {str(is_active):<30} | Type = {type(is_active)}")
    print(f"5. Variable 'tech_stack'   : Value = {str(tech_stack):<30} | Type = {type(tech_stack)}")
    print("=" * 60)

if __name__ == "__main__":
    main()
