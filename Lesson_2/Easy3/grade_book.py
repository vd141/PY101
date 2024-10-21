# Grade Book

def get_grade(score1, score2, score3):
    average = (score1 + score2 + score3) / 3
    match average:
        case average if average >= 90 and average <= 100:
            return 'A'
        case average if average >= 80 and average < 90:
            return 'B'
        case average if average >= 70 and average < 80:
            return 'C'
        case average if average >= 60 and average < 70:
            return 'D'
        case average if average >= 0 and average < 60:
            return 'F'
        case _:
            return 'Scores must be between 0 and 100 inclusive.'

print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True