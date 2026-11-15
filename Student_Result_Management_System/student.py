from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Student:
    student_id: str
    full_name: str
    class_form: str
    gender: str
    date_of_birth: str
    scores: dict = field(default_factory=dict)
    result_date: str = ""

    def __post_init__(self):
        if not self.result_date:
            self.result_date = datetime.now().strftime("%Y-%m-%d %H:%M")

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "full_name": self.full_name,
            "class_form": self.class_form,
            "gender": self.gender,
            "date_of_birth": self.date_of_birth,
            "scores": self.scores,
            "result_date": self.result_date,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            student_id=data.get("student_id", ""),
            full_name=data.get("full_name", ""),
            class_form=data.get("class_form", ""),
            gender=data.get("gender", ""),
            date_of_birth=data.get("date_of_birth", ""),
            scores=data.get("scores", {}),
            result_date=data.get("result_date", ""),
        )
