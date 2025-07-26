from enum import Enum
from typing import Optional
import requests


class Category(Enum):
    GENERAL_KNOWLEDGE = 9
    BOOKS = 10
    FILM = 11
    MUSIC = 12
    MUSICALS_THEATERS = 13
    TELEVISION = 14
    VIDEO_GAMES = 15

class Difficulty(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

class QuestionType(Enum):
    MULTIPLE_CHOICE = "multiple"
    TRUE_FALSE = "boolean"

class GenerateQuestions:

    def __init__(self,
                 num_of_questions: Optional[int]  = 10,
                 question_type: Optional[QuestionType] = QuestionType.TRUE_FALSE,
                 category: Optional[Category] = None,
                 difficulty: Optional[Difficulty] = None
                 ):

        self._params = {}
        self.update_question_params(
            num_of_questions=num_of_questions,
            question_type=question_type,
            category=category,
            difficulty=difficulty
        )

    def _call_question_api(self):
        response = requests.get("https://opentdb.com/api.php", self._params)
        response.raise_for_status()
        return response.json()

    def get_questions(self):
        return self._call_question_api()['results']

    def update_question_params(self,
               num_of_questions: Optional[int] = 10,
               category: Optional[Category] = None,
               difficulty: Optional[Difficulty] = None,
               question_type: Optional[QuestionType] = QuestionType.TRUE_FALSE):

        if num_of_questions < 1 or not isinstance(num_of_questions, int):
            raise ValueError("Invalid input in num_of_questions")

        if num_of_questions:
            self._params["amount"] = num_of_questions
        if category:
            self._params["category"] = category.value
        if difficulty:
            self._params["difficulty"] = difficulty.value
        if question_type:
            self._params["type"] = question_type.value



question_data = GenerateQuestions().get_questions()
