from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    q_bank = Question(data["question"], data["correct_answer"])
    question_bank.append(q_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the Quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
