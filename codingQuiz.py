CODE = """
def loop(n):
    for i in range(n):
        n += 1
        
    return n
"""

questions = [f"""What does the code below return if n = 50? 
      {CODE}""",f"""What does the code below return if n = 25?
      {CODE}""",f"""What does the code below return if n = 1?
      {CODE}""",f"""What does the code below return if n = 2?
      {CODE}""",f"""What does the code below return if n = 555?
      {CODE}""",f"""What does the code below return if n = 106?
      {CODE}""",f"""What does the code below return if n = 55?
      {CODE}""",f"""What does the code below return if n = 9?
      {CODE}""",f"""What does the code below return if n = 99?
      {CODE}""",f"""What does the code below return if n = 82?
      {CODE}"""]


answers = [100,
           50,
           2,
           4,
           1110,
           212,
           110,
           18,
           198,
           164]



count = 0
correct = 0
total = len(answers)


while count < total:
    
    print(questions[count])
    user_answer = int(input("ENTER HERE: "))
    if answers[count] == user_answer:
        print("CORRECT ANSWER")
        correct += 1
    elif answers[count] != user_answer and user_answer != 9999:
        print("INCORRECT ANSWER")
    if user_answer == 9999:
        print("OKAY BYE")
        break
    count += 1
score = correct / total
def score_checker(your_score):
    your_score *= 100
    if your_score > 90 and your_score <= 100:
        print("GREAT JOB! YOU GOT AN A")
    if your_score > 80 and your_score <= 90:
        print("GOOD JOB! YOU GOT A B")
    if your_score > 70 and your_score <= 80:
        print("SATISFACTORY. YOU GOT A C")
    if your_score > 60 and your_score <= 70:
        print("YOU BARELY PASSED THIS TIME... YOU GOT A D")
    if your_score <= 50:
        print("STUDY AND YOU'll IMPROVE.. YOU FALIED")
    if your_score == 0:
        print("TRY AGAIN LATER... COME ON BUDDY...")
    

print(f"{score * 100}%")
score_checker(score)
