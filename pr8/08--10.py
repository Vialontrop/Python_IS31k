class Exam:
    def score(self):
        return 0


class MathExam(Exam):
    def score(self):
        return 95


class EnglishExam(Exam):
    def score(self):
        return 88


exams = [MathExam(), EnglishExam(), Exam()]
total = sum(e.score() for e in exams)
print(total)
