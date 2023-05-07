runner = {'John': [10 * 6, 6 + 20, 10, 6, 20], 
          'James': [8 * 8, 8 + 25, 8, 8, 25],
          'Jenna': [12 * 5, 5 + 16, 12, 5, 16],
          'Josh': [7 * 7, 7 + 23, 7, 7, 23],
          'Jacob': [9 * 4, 4 + 32, 9, 4, 32],
          'Jerry': [5 * 9, 9 + 18, 5, 9, 18]}

secs = 1234
result = {}
for (k, v) in runner.items():
    distance = (secs // v[1]) * v[0]
    remaining = secs % v[1]
    while remaining > 0:
        if remaining >= v[3]:
            remaining = remaining - v[3]
            distance += v[2] * v[3] 
            remaining = remaining - v[4]
        else:
            remaining -= remaining
            distance += remaining * v[3]
    result[k] = distance
sorted_result = sorted(result.items(), key=lambda x: x[1], reverse = True)
#print(sorted_result)

print("Longest distance", sorted_result[0][1], "is achieved by", sorted_result[0][0])