

import time

def generate_random_marks(count, seed=123):
    a = 1103515245
    c = 12345
    m = 2**31
    
    marks = []
    current_val = seed
    
    for _ in range(count):
        current_val = (a * current_val + c) % m
      
        score = current_val % 101
        marks.append(score)
        
    return marks


def compare_search_speeds(size=15000):
    list_data = [(f"STU_{i}", f"Student_{i}", i % 100) for i in range(size)]
    dict_data = {f"STU_{i}": (f"Student_{i}", i % 100) for i in range(size)}
    
    search_target = f"STU_{size - 1}"  
    
  
    t0 = time.perf_counter()
    _ = [record for record in list_data if record[0] == search_target]
    t1 = time.perf_counter()
    list_duration = t1 - t0
    
    
    t0 = time.perf_counter()
    _ = dict_data.get(search_target)
    t1 = time.perf_counter()
    dict_duration = t1 - t0
    
    return list_duration, dict_duration
