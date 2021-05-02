from Odin import Odin
from Loki import Loki
from Thor import Thor
from counter import Counter

counter_thor=Counter(2)
counter_odin=Counter(2)
odin_dodge=Counter(2)
thor_dodge=Counter(2)
loki=Loki()
odin=Odin()
thor=Thor()
choice1=input("Which character if you want to choice Odin you can type Odin,you want to choice Loki youcan type Loki,you want to Thor,you can type Thor")
choice2 = input("Which character if you want to choice Odin you can type Odin,you want to choice Loki youcan type Loki,you want to Thor,you can type Thor")

if(choice1.upper()=="ODIN" and choice2.upper()=="THOR" or choice1.upper()=="THOR" and choice2.upper()=="ODIN"):
    while True:
        print("Moves on Odin")
        attackchoice = input(" press Pyhsical attack for P,press glory attack for G,Ultimate attack for U")

        if (attackchoice == "P"):
            thor.HP=thor.HP-odin.First_attack
        elif (attackchoice == "G"):
            thor.HP=thor.HP-odin.Second_attack
        elif(attackchoice=="U"):
            thor.HP=thor.HP-odin.Ultimate
            counter_odin.increase_count(1)
            if (counter_odin.count <= 0):
                continue

        defencechoice = input("press F for Defence,press D for Dodge")
        if(defencechoice=="F"):
            print("You are defencing moves")
            thor.HP+=thor.Defence
        elif(defencechoice=="D"):
            print("You are dodging moves")
            thor.HP+=thor.Dodge
            thor_dodge.increase_count(1)
            if(thor_dodge.count<=0):
                print("you are defencing ")
                thor.HP += thor.Defence

        print("Moves on  Thor")
        attackchoice = input(" press Pyhsical attack for P,press glory attack for G,Ultimate attack for U")
        if (attackchoice == "P"):
            odin.HP = odin.HP - thor.First_attack
        elif (attackchoice == "G"):
            odin.HP = odin.HP - thor.Second_attack
        elif (attackchoice == "U"):
              odin.HP-=thor.Ultimate
              counter_thor.increase_count(1)
              if(counter_thor.count<=0):
                  odin.HP = odin.HP - thor.Second_attack







        defencechoice = input("press F for Defence,press D for Dodge")
        if (defencechoice == "F"):
            print("You are defencing moves")
            odin.HP += odin.Defence
        elif (defencechoice == "D"):
            print("You are dodging moves")
            odin.HP += odin.Dodge
            odin_dodge.increase_count(1)
            if (odin_dodge.count <= 0):
                odin.HP += odin.Defence




        if(odin.HP<=0):
            print("Odin is dead")
            break
        elif(thor.HP<=0):
            print("Thor is dead")
            break




elif(choice1.upper()=="ODIN" and choice2.upper()=="lOKI" or choice1.upper()=="LOKI" and choice2.upper()=="ODIN"):
    while True:

        attackchoice=input(" press Pyhsical attack for P,press glory attack for G,Ultimate attack for U")
        defencechoice=input(",press F for Defence,press D for Dodge")
        if(attackchoice=="P"):
            pass
        elif(attackchoice=="G"):
            pass
        else:
            pass


elif(choice1.upper()=="THOR" and choice2.upper()=="LOKI" or choice1.upper()== "LOKI" and choice2.upper()== "THOR"):
    while True:
        attackchoice = input("press Pyhsical attack for P,press glory attack for G,Ultimate attack for U")
        defencechoice = input("press F for Defence,press D for Dodge")
        if (attackchoice == "P"):
            pass
        elif (attackchoice == "G"):
            pass
        else:
            pass




