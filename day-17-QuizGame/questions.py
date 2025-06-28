import requests
import html

class Questions:
    """
    Class to fetch trivia questions from the Open Trivia Database API.

    Parameters:
    - num_of_questions (int): The number of questions to fetch. Default is 10.
    - category (str or int, optional): The category of questions. Can be a category name or its corresponding ID.
    - Difficulty (str, optional): The difficulty level of questions. Options: 'easy', 'medium', 'hard'.

    Category options:
    - "General Knowledge"
    - "Books"
    - "Film"
    - "Music"
    - "Musicals"
    - "Television"
    - "Video Games"
    """

    CATEGORY_DICT = {
        "General Knowledge": 9,
        "Books": 10,
        "Film": 11,
        "Music": 12,
        "Musicals": 13,
        "Television": 14,
        "Video Games": 15
    }

    def __init__(self, num_of_questions: int, category: str, difficulty: str):
        # TODO: Have to handle scenario where there are not enough questions
        url = f"https://opentdb.com/api.php?amount={num_of_questions}&type=boolean"
        if category: url +=  f"&category={Questions.CATEGORY_DICT[category.capitalize()]}"
        if difficulty: url += f"&difficulty={difficulty.lower()}"
        self.__response = requests.get(url)
        self.__question_list = self.__get_questions()
        self.__current_question = None
        self.__correct_answer = 0
        self.__num_of_questions = 0

    def __get_questions(self):
        questions = []
        for question in self.__response.json()['results']:
            questions.append(question)
        return questions

    def get_question(self) -> str or None:
        """
        Retrieves the next trivia question from the internal list.

        Returns:
            str: The text of the next trivia question.
                 Returns None if no questions remain.
        """
        if self.__question_list:
            self.__current_question = self.__question_list.pop()
            self.__num_of_questions += 1
            return html.unescape(self.__current_question['question'])
        return None

    def check_answer(self, answer: str):
        """
        Compares the user's answer to the correct answer and prints the result.
        Also updates the internal score counter.

        Parameters:
            answer (str): The user's answer as 'True' or 'False' (case-insensitive).
        """
        if answer.capitalize() == self.__current_question['correct_answer']:
            print("You got it right!")
            self.__correct_answer += 1
        else:
            print("That's wrong.")

        print(f"The correct answer was: {self.__current_question['correct_answer']}.")
        print(f"Your current score is: {self.__correct_answer}/{self.__num_of_questions}")