#Test Case for maths pyq

#Only for maths just as a test case!
import random
import TestMathsModule

#Main menu automatically gives u mcq options and answer for the test case!!
def main():
    random.seed(0)
    q=TestMathsModule.maths_mcq[0]
#will print all 3 menus without input from user and also give correct answer!!
    print("Q:",q["question"])
    print("Options:",q["options"])
    answer_text=q["answer"]
    options=q["options"]
    answer_index=1

    for i in range(len(options)):
        if options[i].lower()==answer_text.lower():
            answer_index=i+1
            break
#Kept it simple for test case just to show all the three types of selections
    print("Correct option number:",answer_index)
    print("-----Here you go!^-^-----")

if __name__=="__main__":
    main()
