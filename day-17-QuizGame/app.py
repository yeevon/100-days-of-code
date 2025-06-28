def main():
    from questions import Questions
    question = ""
    q = None
    count = 1
    num_questions = 10  # default
    category = None  # default
    difficulty = None  # default

    while question is not None:
        if question == "":
            print("Welcome to the Quiz Game!")
            if "yes" == input("Do you want to customize the game? (Yes/No): ").lower():
                num_questions = int(input("How many questions do you want for this game: "))
                category = input(f"Select from list of categories: {list(Questions.CATEGORY_DICT.keys())}:\n")
                difficulty = input("Select level of difficulty? ['Easy', 'Medium', 'Hard']: ")


            q = Questions(num_questions, category, difficulty)
            question = q.get_question()

        answer = input(f"Q.{count}: {question} (True/False)?: ")
        q.check_answer(answer)
        question = q.get_question()
        count += 1

if __name__ == "__main__":
    main()