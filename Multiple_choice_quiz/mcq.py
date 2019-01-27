from Question import Question

question_prompt = [
    "What colour are Apples?\n(a)Red(b)Green\n",
    "What colour are Bananas?\n(a)Purple(b)Yellow\n",
    "What colour are Oranges?\n(a)Blue(b)Orange\n"
]

questions = [
    Question(question_prompt[0],"a"),
    Question(question_prompt[1],"b"),
    Question(question_prompt[2],"b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got "+str(score)+"/"+str(len(questions))+" correct")


run_test(questions)
