#Test Case for maths pyq

#Only for maths
import random
import TestMathsModule

#Main menu automatically gives u mcq options and answer for the test case!
def main():
    random.seed(0)
    q= TestMathsModule.maths_mcq[0]

    print("Q:", q["question"])
    print("Options:", q["options"])
    answer_text = q["answer"]
    options = q["options"]
    answer_index = 1

    for i in range(len(options)):
        if options[i].lower() == answer_text.lower():
            answer_index = i + 1
            break

    print("Correct option number:", answer_index)
    print("-----Here you go! ^-^-----")

if __name__ == "__main__":
    main()
