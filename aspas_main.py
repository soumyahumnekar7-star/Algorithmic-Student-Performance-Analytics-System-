

def reverse_list_in_place(arr):
    work_list = list(arr)
    start = 0
    end = len(work_list) - 1
    
    while start < end:
        work_list[start], work_list[end] = work_list[end], work_list[start]
        start += 1
        end -= 1
        
    return work_list


def partition_students(student_data, cutoff_mark):
    passed = []
    needs_improvement = []
    
    for item in student_data:
        if item[2] >= cutoff_mark:
            passed.append(item)
        else:
            needs_improvement.append(item)
            
    return passed, needs_improvement


def get_kth_lowest_mark(marks_list, k):
    if k <= 0 or k > len(marks_list):
        return None
        
    temp = list(marks_list)
    n = len(temp)
    
    for i in range(k):
        min_pos = i
        for j in range(i + 1, n):
            if temp[j] < temp[min_pos]:
                min_pos = j
        temp[i], temp[min_pos] = temp[min_pos], temp[i]
        
    return temp[k - 1]
