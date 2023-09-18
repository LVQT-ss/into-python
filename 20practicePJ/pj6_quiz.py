quiz = { 
    "question1":{
        "question": " what is the capital of france",
        "answer":"paris"
    },
    "question2":{
        "question": " what is the capital of germany",
        "answer":"berlin"
    },
    "question3":{
        "question": " what is the capital of italy",
        "answer":"rome"
    },
    "question4":{
        "question": " what is the capital of spain",
        "answer":"mandrid"
    },
    "question5":{
        "question": " what is the capital of vietnam",
        "answer":"hanoi"
    },
}
score = 0 
for key, value in quiz.items():
    print(value["question"])
    answer = input("answer?")

    if answer.lower() == value['answer'].lower():
        score = score +1 
        print("your score is : "+ str(score))
    
    else:
        print("wrong!")
        print("the answer is : "+ value['answer'])
        print("your score is : "+ str(score))


print("you got " + str(score) + " out of 78 questions correctly ")
print("your percentage is " + str(int(score/7 * 100) ) + "%")