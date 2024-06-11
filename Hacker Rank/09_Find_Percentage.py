if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
       name, *line = input().split()
       score = list(map(float, line))
       student_marks[name] = score
    input_query = input()
    _sum = sum(student_marks[input_query])
    _len = len(student_marks[input_query])
    _avg = round(_sum / _len, 2)
    print(f"{_avg:.2f}")