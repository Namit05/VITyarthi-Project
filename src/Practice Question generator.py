#Practice Question Generator


#All modules used in the Program!

import random
import EnglishQuestions
import ChemistryQuestions
import PhysicsQuestions
import MathsQuestions

#Function to choose Subject!

def choose_a_subject():
    print("----Choose A Subject----")
    print("1.English")
    print("2.Chemistry")
    print("3.Physics")
    print("4.Maths")
    print("5.Exit")
    choice = input("Enter your choice :")

    if choice == "1":
        return "english"
    elif choice == "2":
        return "chemistry"
    elif choice == "3":
        return "physics"
    elif choice == "4":
        return "maths"
    elif choice == "5":
        return "exit"
    else:
        print("Invalid Input Detected!")
        return choose_a_subject()

#Function to choose the question type !

def choose_type():
    print("-----Choose question type-----")
    print("0. Exit")
    print("1. MCQ")
    print("2. Fill in the blanks")
    print("3. Short answer")
    print("4. Long answer")
    choice = input("Enter choice: ")

    if choice == "0":
        return "exit"
    elif choice == "1":
        return "mcq"
    elif choice == "2":
        return "fill"
    elif choice == "3":
        return "short"
    elif choice == "4":
        return "long"
    else:
        print("Invalid Input!")
        return choose_type()

#Function to get the questions depending on the choice of how many !

def get_questions(subject, question_type):
    if subject == "english":
        if question_type == "mcq":
            return EnglishQuestions.english_mcq
        if question_type == "fill":
            return EnglishQuestions.english_fill
        if question_type == "short":
            return EnglishQuestions.english_short
        if question_type == "long":
            return EnglishQuestions.english_long

    if subject == "chemistry":
        if question_type == "mcq":
            return ChemistryQuestions.chemistry_mcq
        if question_type == "fill":
            return ChemistryQuestions.chemistry_fill
        if question_type == "short":
            return ChemistryQuestions.chemistry_short
        if question_type == "long":
            return ChemistryQuestions.chemistry_long

    if subject == "physics":
        if question_type == "mcq":
            return PhysicsQuestions.physics_mcq
        if question_type == "fill":
            return PhysicsQuestions.physics_fill
        if question_type == "short":
            return PhysicsQuestions.physics_short
        if question_type == "long":
            return PhysicsQuestions.physics_long

    if subject == "maths":
        if question_type == "mcq":
            return MathsQuestions.maths_mcq
        if question_type == "fill":
            return MathsQuestions.maths_fill
        if question_type == "short":
            return MathsQuestions.maths_short
        if question_type == "long":
            return MathsQuestions.maths_long

    return []

#Function for MCQ !

def ask_mcq(question_item):
    print("Q:", question_item["question"])

    index = 1
    while index <= len(question_item["option"]):
        print(str(index) + ". " + question_item["option"][index - 1])
        index = index + 1

    attempts = 1
    while attempts <= 3:
        answer = input("Your answer (number): ")

        if answer.isdigit():
            number = int(answer)
            if number >= 1 and number <= len(question_item["option"]):
                chosen = question_item["option"][number - 1]
                if chosen.lower() == question_item["answer"].lower():
                    print("Correct!")
                    return
                else:
                    print("Wrong.")
            else:
                print("Enter a valid option number.")
        else:
            print("Please enter a number.")

        attempts = attempts + 1

    print("Correct answer:", question_item["answer"])

#Function for Fill in the blanks ! 

def ask_fill(question_item):
    print("Q:", question_item["question"])

    attempts = 1
    while attempts <= 3:
        answer = input("Your answer: ")

        if answer.lower().strip() == question_item["answer"].lower().strip():
            print("Correct!")
            return
        else:
            print("Wrong.")

        attempts = attempts + 1

    print("Correct answer:", question_item["answer"])

#Function for short questions !

def ask_short(question_item):
    print("Q:", question_item["question"])

#Function for long questions !

def ask_long(question_item):
    print("Q:", question_item["question"])

#Main Function and Main Menu of Program !

def main():
    print("---PRACTICE QUESTIONS----")

    subject = choose_a_subject()
    if subject == "exit":
        print("----EXITING----")
        return

    question_type = choose_type()
    if question_type == "exit":
        print("----EXITING----")
        return

    question_list = get_questions(subject, question_type)

    if len(question_list) == 0:
        print("No questions found for this selection.")
        return

    how_many = input("How many questions do you want? ")

    if how_many.isdigit():
        how_many = int(how_many)
    else:
        how_many = 1

    if how_many > len(question_list):
        how_many = len(question_list)

    selected_questions = random.sample(question_list, how_many)

    print("-- Starting Practice ---")

    for item in selected_questions:
        if question_type == "mcq":
            ask_mcq(item)
        elif question_type == "fill":
            ask_fill(item)
        elif question_type == "short":
            ask_short(item)
        elif question_type == "long":
            ask_long(item)

    print("----HOPE YOU ENJOYED ^~^----")

if __name__ == "__main__":
    main()
