class Job:
    def __init__(self, job_code, job_name, field, salary):
        self.job_code = job_code
        self.job_name = job_name
        self.field = field
        self.salary = salary

    def evaluate(self):
        avg_score = (self.python_skill + self.ml_skill + self.deep_skill + self.math_skill) / 4
        if avg_score > 9.0:
            return "Rất phù hợp"
        elif avg_score > 7.0:
            return "Phù hợp"
        elif avg_score > 5.0:
            return "Tạm được"
        elif avg_score > 3.0:
            lacking_skills = [skill for skill, score in self.get_skills().items() if score < 4.0]
            return f"Cần bổ sung kiến thức: {', '.join(lacking_skills)}"
        else:
            return "Cần học lại kiến thức base"

    def get_skills(self):
        return {
            "Python Skill": self.python_skill,
            "ML Skill": self.ml_skill,
            "Deep Skill": self.deep_skill,
            "Math Skill": self.math_skill
        }


class AI(Job):
    def __init__(self, python_skill, ml_skill, deep_skill, math_skill):
        super().__init__("AI001", "AI Engineer", "Artificial Intelligence", 0)
        self.python_skill = python_skill
        self.ml_skill = ml_skill
        self.deep_skill = deep_skill
        self.math_skill = math_skill


class Backend(Job):
    def __init__(self, sql_skill, oop_skill, api_skill, java_skill):
        super().__init__("BE001", "Backend Developer", "Software Development", 0)
        self.sql_skill = sql_skill
        self.oop_skill = oop_skill
        self.api_skill = api_skill
        self.java_skill = java_skill

    def get_skills(self):
        return {
            "SQL Skill": self.sql_skill,
            "OOP Skill": self.oop_skill,
            "API Skill": self.api_skill,
            "Java Skill": self.java_skill
        }


class Frontend(Job):
    def __init__(self, html_skill, css_skill, nodejs_skill, ux, ui):
        super().__init__("FE001", "Frontend Developer", "Web Development", 0)
        self.html_skill = html_skill
        self.css_skill = css_skill
        self.nodejs_skill = nodejs_skill
        self.ux = ux
        self.ui = ui

    def get_skills(self):
        return {
            "Html Skill": self.html_skill,
            "Css Skill": self.css_skill,
            "Nodejs Skill": self.nodejs_skill,
            "UX": self.ux,
            "UI": self.ui
        }


class Fullstack(Backend, Frontend):
    def __init__(self, python_skill, ml_skill, deep_skill, math_skill, sql_skill, oop_skill, api_skill, java_skill,
                 html_skill, css_skill, nodejs_skill, ux, ui):
        Backend.__init__(self, sql_skill, oop_skill, api_skill, java_skill)
        Frontend.__init__(self, html_skill, css_skill, nodejs_skill, ux, ui)
        self.python_skill = python_skill
        self.ml_skill = ml_skill
        self.deep_skill = deep_skill
        self.math_skill = math_skill

ai_engineer = AI(9.5, 8.0, 7.5, 9.0)
backend_dev = Backend(8.0, 9.0, 7.0, 8.5)
frontend_dev = Frontend(8.0, 9.0, 8.5, 7.5, 8.0, 9.0)
fullstack_dev = Fullstack(9.0, 8.5, 8.0, 9.0, 8.5, 9.0, 7.5, 8.0, 8.0, 9.0, 8.5, 8.0, 9.0)

print("Thông tin và đánh giá của AI Engineer:")
print(ai_engineer.__dict__)
print(f"Đánh giá: {ai_engineer.evaluate()}\n")

print("Thông tin và đánh giá của Backend Developer:")
print(backend_dev.__dict__)
print(f"Đánh giá: {backend_dev.evaluate()}\n")

print("Thông tin và đánh giá của Frontend Developer:")
print(frontend_dev.__dict__)
print(f"Đánh giá: {frontend_dev.evaluate()}\n")

print("Thông tin và đánh giá của Fullstack Developer:")
print(fullstack_dev.__dict__)
print(f"Đánh giá: {fullstack_dev.evaluate()}")
