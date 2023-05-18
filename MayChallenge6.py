import heapq
from collections import Counter

def min_steps_to_delete_series(series):
    operations = 0
    
    while len(series) > 0:
        longest_sequence = ''
        longest_length = 0
        
        # Find the longest contiguous sequence of the same character
        current_sequence = ''
        current_length = 0
        
        for i in range(len(series)):
            if series[i] == current_sequence:
                current_length += 1
            else:
                if current_length > longest_length:
                    longest_sequence = current_sequence
                    longest_length = current_length
                current_sequence = series[i]
                current_length = 1
        
        if current_length > longest_length:
            longest_sequence = current_sequence
            longest_length = current_length
        
        # Remove the longest sequence from the series
        print(longest_sequence * longest_length)
        series = series.replace(longest_sequence * longest_length, '', 1)
        
        operations += 1
    
    return operations - 1

def min_steps_to_delete_series_heuristic(series):
    goal_state = ''

    open_list = []
    heapq.heappush(open_list, (0, series, 0))  # (f-score, state, g-score)
    closed_set = set()

    while open_list:
        _, state, g_score = heapq.heappop(open_list)

        if state == goal_state:
            return g_score

        if state in closed_set:
            continue

        closed_set.add(state)

        #counter = Counter(state)
        #unique_chars = set(counter.keys())
        #h_score = len(unique_chars)
        
        strList = []
        current_sequence = ''
        current_length = 0

        for i in range(len(state)):
            if state[i] == current_sequence:
                current_length += 1
            else:
                if not current_sequence == '':
                    strList.append(current_sequence * current_length)
                current_sequence = state[i]
                current_length = 1

        strList.append(current_sequence * current_length)
        
        #print(strList)
    
        for i in range(len(strList)):
            strListCp = strList.copy()
            strListCp[i] = ''
            new_state = "".join(strListCp)
            #print(new_state)
            score = calculate_score(new_state)
            #print(score)
            heapq.heappush(open_list, (score, new_state, g_score + 1))

        #for char in unique_chars:
        #    char_count = counter[char]
        #    for i in range(1, char_count + 1):
        #        new_state = state.replace(char * i, '')
        #       heapq.heappush(open_list, (g_score + 1 + h_score, new_state, g_score + 1))

    return None  # No solution found

def calculate_score(series):
    score = 0
    current_sequence = ''
    current_length = 0
    for i in range(len(series)):
        if series[i] == current_sequence:
            current_length += 1
        else:
            if not current_sequence == '':
                score += 1
            current_sequence = series[i]
            current_length = 1
    score += 1
    return score

series = "kjslaqpwoereeeeewwwefifjdksjdfhjdksdjfkdfdlddkjdjfjfjfjjjjfjffnefhkjgefkgjefkjgkefjekihutrieruhigtefhgbjkkkknbmssdsdsfdvneurghiueor"
min_steps = min_steps_to_delete_series_heuristic(series)
print(min_steps)