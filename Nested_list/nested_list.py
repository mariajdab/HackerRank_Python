if __name__ == '__main__':
    n = int(input())
    student_name_score = [[input(), float(input())] for _ in range(n)]
    # Orded by grade
    student_name_score.sort(key = lambda x : x[1])
     
    second_lowest_grade = []
    first_lowest_grade = student_name_score[0][1]

    for name, grade in student_name_score:
        if grade != first_lowest_grade:
            if len(second_lowest_grade) == 0:
                second_lowest_grade.append(name)
                g = grade
            else:
                if grade == g:
                    second_lowest_grade.append(name)
                else:
                    # Here break this avoid iterate over all students
                    break
    # Sort by name if the second_lowest_grade is shared with several students           
    print(*sorted(second_lowest_grade), sep ='\n')