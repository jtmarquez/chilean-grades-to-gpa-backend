def calculateSingleGpaFromGrade(grade):
    if (grade >= 6.5):
        return 4.0
    if (grade >= 6.0):
        return 3.7
    if (grade >= 5.5):
        return 3.3
    if (grade >= 5):
        return 3.0
    if (grade >= 4.5):
        return 2.7
    if (grade >= 4):
        return 2.0
    return 0.0

def calculateGpaFromGrades(chilean_grades):
    gpas = [calculateSingleGpaFromGrade(grade) for grade in chilean_grades]
    return gpas
    
def calculateAvgGpaFromGpas(gpas):
    avg_gpa = sum(gpas) / len(gpas)
    return avg_gpa