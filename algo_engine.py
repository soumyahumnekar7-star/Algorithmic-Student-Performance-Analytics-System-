

def remove_duplicate_students(student_list):
    seen_ids = set()
    clean_list = []
    
    for record in student_list:
        student_id, name, mark = record
        if student_id not in seen_ids:
            seen_ids.add(student_id)
            clean_list.append((student_id, name, mark))
            
    return clean_list


def assign_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 75:
        return 'B'
    elif score >= 60:
        return 'C'
    elif score >= 40:
        return 'D'
    else:
        return 'F'
