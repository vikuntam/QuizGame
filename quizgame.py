def run_quiz(questions):
    score = 0
    for question in questions:
        print("\n" + question["question"])
        for option in question["options"]:
            print(option)
        answer = input("Your answer (A/B/C/D): ").upper()
        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}")
    print(f"\nYour final score is {score} out of {len(questions)}")


# Question bank
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Paris", "C. Berlin", "D. Rome"],
        "answer": "B"
    },
    {
        "question": "Which language is used to write this quiz?",
        "options": ["A. Java", "B. Python", "C. C++", "D. JavaScript"],
        "answer": "B"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Process Unit", "B. Central Processing Unit", "C. Computer Personal Unit", "D. Central Power Unit"],
        "answer": "B"
    }
]

# Start the quiz
run_quiz(quiz_questions)