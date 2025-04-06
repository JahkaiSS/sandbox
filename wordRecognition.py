keywords = ["fight","battle","eat","feast","sleep","nap","rest"]
time = 0
user_answer = ""
units = "hours"
actionList = []
while user_answer != "exit":
    user_answer = input("What action will you choose?\n")
    if user_answer == "clear":
        time = 0
        actionList = []
        print("Actions cleared!")
    
    for i in keywords:
        if i in user_answer:
            if i in ["fight","battle"]:
                time += 60 * 2
                actionList.append(i)
            if i in ["sleep","nap","rest"]:
                time += 60 * 8
                actionList.append(i)
            if i in ["eat","feast"]:
                time += 15
                actionList.append(i)
    
    print(f"time used: {round(time / 60, 2)} {units} on these actions -> {actionList}")
    
    
