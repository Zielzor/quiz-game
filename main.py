from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_list = []

for q in question_data:
    question_list.append(Question(q["text"], q["answer"]))


quiz = QuizBrain(question_list)

while quiz.still_has_questions():
    quiz.next_question()

print("You completed the quiz")
print(f"Final score was: {quiz.score}/{quiz.question_number}")

