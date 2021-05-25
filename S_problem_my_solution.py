class Student:
    # 코드를 쓰세요
    def __init__(self, name, id, major):
        self.name = name
        self.id = id
        self.major = major
        self.grade = Grade(self.name, self.id, self.major)

    def change_student_info(self, new_name, new_id, new_major):
        self.name = new_name
        self.id = new_id
        self.major = new_major


# 작성한 클래스에 맞춰서 실행 코드도 바꿔보세요

class Grade:
    def __init__(self, name, id, major):
        self.name = name
        self.id = id
        self.major = major
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 4.3:
            self.grades.append(grade)
        else:
            print("수업 학점은 0과 4.3 사이여야 합니다!")

    def get_average_gpa(self):
        return sum(self.grades) / len(self.grades)

    def print_report_card(self):
        print("코드잇 대학 성적표\n\n학생 이름:{}\n학생 번호:{}\n소속 학과:{}\n평균 학점:{}" \
              .format(self.name, self.id, self.major, self.get_average_gpa()))


younghoon = Student("강영훈", 20120034, "통계학과")
younghoon.change_student_info("강영훈", 20130024, "컴퓨터 공학과")

younghoon.grade.add_grade(3.0)
younghoon.grade.add_grade(3.33)
younghoon.grade.add_grade(3.67)
younghoon.grade.add_grade(4.3)

younghoon.grade.print_report_card()
