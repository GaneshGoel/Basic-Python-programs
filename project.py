"""
Created on Sat Mar 30 18:02:14 2019

@author: Ganesh Goel
"""

import random
import win32com.client as wincl
speak=wincl.Dispatch("SAPI.Spvoice")
import datetime
dt=datetime.datetime.now()



print("This is your personal assistant Zetmax.")
speak.Speak("This is your personal assistant Zetmax.")
greetings=['Hi','Hello','Hola','Yo','Hey','hi','hello']
greeting=['Hello! Please enter your name.',"Hi! Please enter your name."]
y=input(">>>")
if y in greetings:
    r_re=random.choice(greeting)
    print(r_re)
    speak.Speak(r_re)
sal=['Thanks','thanks','Thank you','Thank You','thank you','thank You']
resp=['Anytime','Your welcome','My pleasure']
rep=['Roll a die','roll a die']
res=["It's a one","It's a two","It's a three","It's a four","It's a five","It's a six"]
a=['Bye','bye']
b=["What's the time now","Can you tell me the time","Time","time","Current time"]
c=["Date","date","Today's date","What's the date today"]
d=["Reminder","reminder","Set a reminder","set a reminder"]
remind=[]
e=["What's the reminder","What to do now","todo","to do","To do"]
f=["Fact","tell me an amazing fact","amazing fact","fact"]
fact=["Banging your head against a wall for one hour burns 150 calories.","Snakes can help predict earthquakes.","Cherophobia is an irrational fear of fun or happiness.","If you lift a kangaroo’s tail off the ground it can’t hop.","Polar bears could eat as many as 86 penguins in a single sitting."]
g=["What's my name","My name","my name"]
name=[]
h=["Who created you"]
i=["toss a coin","Toss a coin"]
j=["It's a head.","It's a tail."]
x=input(">>>")
name.append(x)
print("Nice to meet you "+ x +". How can i help you?")
speak.Speak("Nice to meet you "+ x +". How can i help you?")
while True:
    userinput=input(">>>")
    if userinput in greetings:
        r_greeting=random.choice(greeting)
        print(r_greeting)
        speak.Speak(r_greeting)
    elif userinput in sal:
        r_response=random.choice(resp)
        print(r_response)
        speak.Speak(r_response)
    elif userinput in rep:
        r_resp=random.choice(res)
        print(r_resp)
        speak.Speak(r_resp)
    elif userinput in b:
        time=dt.strftime("%I %M %p")
        print(time)
        speak.Speak("It's"+time)
    elif userinput in c:
        date=dt.strftime("%a,%b %d ,%Y")
        print(date)
        speak.Speak("It's"+date)
    elif userinput in d:
        print("What do you want me to remember?")
        speak.Speak("What do you want me to remember?")
        rem=input("Enter text:")
        remind.append(rem)
        print("Ok! But what time should i remind you?")
        speak.Speak("Ok! But what time should i remind you?")
        input(">>>")
        print("Okay, I will remember that.")
        speak.Speak("Okay, I will remember that.")
    elif userinput in e:
        print("".join(remind))
    elif userinput in f:
        r_rsp=random.choice(fact)
        print(r_rsp)
        speak.Speak(r_rsp)
    elif userinput in g:
        print("Your name is "+x)
        speak.Speak("Your name is "+x)
    elif userinput in h:
        print("I have been created by Ganesh Goel.")
        speak.Speak("I have been created by Ganesh Goel.")
    elif userinput in i:
        r_rp=random.choice(j)
        print(r_rp)
        speak.Speak(r_rp)
    elif userinput in a:
        print("Bye, It was nice meeting you "+x+". Hope we will meet again.")
        speak.Speak("Bye, It was nice meeting you "+x+". Hope we will meet again.")
        break
    else:
        print("Sorry! I was not able to understand what you said, so can you please try again !")
        speak.Speak("Sorry! I was not able to understand what you said, so can you please try again !")
    
    