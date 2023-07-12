import tkinter as tk
from tkinter import StringVar
from tkinter import *

window = Tk()
window.geometry("500x500")

questions = ["Attraper-les tous,il s agit du slogan de: ","L'histoire satache à lenfance et à l'adolescence de goku ","Au contacte de l'eau froide, ce garcon se transforme en une ravissante jeune fille","Nicky larson","Jeune garcon voulan devenir le meilleur footballeur","Deux frere a la recherche de la piere philosophale"]
option = [["dragon ball super","Beelzebub","pokemon","GTO","pokemon"],["Radiant","dragon ball","Blue exorcist","Goblin slayer","dragon ball"],["Dragon ball","Bleach","One piece","ranma 1/2","ranma 1/2"],["city hunter","One punch man","Blue lock","MMH","city hunter"],["Kuruko no baket","SNK","olive et tom","full metal alchimiste","olive et tom"],["full metal alchimiste","SNK","Bleach","Norigami","full metal alchimiste"]]


frame = Frame(window,padx=10, pady=10,bg="#fff")
questions_label = Label(frame,height=5, width=28,bg="grey",fg='#fff',font=("verdana",20),wraplength=500)

v1 = StringVar(frame)
v2 = StringVar(frame)
v3 = StringVar(frame)
v4 = StringVar(frame)

option1 = Radiobutton(frame,bg="#fff",font=("verdata",20),variable=v1,command= lambda : checkanswer(option1))
option2 = Radiobutton(frame,bg="#fff",font=("verdata",20),variable=v2,command= lambda : checkanswer(option2))
option3 = Radiobutton(frame,bg="#fff",font=("verdata",20),variable=v3,command= lambda : checkanswer(option3))
option4 = Radiobutton(frame,bg="#fff",font=("verdata",20),variable=v4,command= lambda : checkanswer(option4))

button_next = Button(frame,text="Next",bg="orange", font=("verdana",20), command= lambda : displaynextquestion())

frame.grid(row=1, column=0)
questions_label.grid(row=0, column=0)

option1.grid(sticky='w',row=1, column=0)
option2.grid(sticky='w',row=3, column=0)
option3.grid(sticky='w',row=5, column=0)
option4.grid(sticky='w',row=6, column=0)

button_next.grid(row=10, column=0)

index = 0
correct = 0

# creation de fonction pour desactiver les radiobouton

def disablebuttons(state):
    option1["state"] = state
    option2["state"] = state
    option3["state"] = state
    option4["state"] = state

# cretion dune fonction qui verifie si les radiobuttons sont cocher

def checkanswer(radio):
    global correct,index
    # le 4eme emplacement contien la bonne reponce
    # on vas verifer la reponse choisie par lutilisateur
    if radio['text'] == option[index][4]:
        correct += 1
    index += 1
    disablebuttons("disable")


# creation d'une donction qui evois la prochaine question
def displaynextquestion():
    global index,correct
    if (button_next["text"]  == "Restart the Quiz"):
        correct = 0
        index = 0
        questions_label["bg"] = "grey"
        button_next["text"] = "Next"

    if index == len(option):
        questions_label["text"] = str(correct) + "/" + str(len(option))
        button_next["text"] = "Restart the Quiz"
        if correct >= len(option)/2:
            questions_label["bg"] = "green"
        else:
            questions_label["bg"] = "red"

    else:

        questions_label["text"] = questions[index]

        disablebuttons("normal")
        opts = option[index]
        option1['text'] = opts[0]
        option2['text'] = opts[1]
        option3['text'] = opts[2]
        option4['text'] = opts[3]
        v1.set(opts[0])
        v2.set(opts[1])
        v3.set(opts[2])
        v4.set(opts[3])

    if index == len(option)-1:
        button_next["text"] = "check the result"

displaynextquestion()

window.mainloop()