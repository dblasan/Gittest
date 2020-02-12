import math
import re
import matplotlib.pyplot as plt
with open("/home/developer/Downloads/FußDaten.txt","r") as data:
    plaintext=data.read()
    plaintext1=plaintext.split('\n')
    X=[]
    Y=[]
    i=0
    for line in plaintext1:
            #print(line)
            line1=line.replace(']','')
            line2=line1.replace('[','')
            k=line2.split(' ')
            for l in k :
                    try:
                            inNumberfloat = float(l)


                            if (i % 2 == 0):

                                    X.append(l)
                                    i=i+1

                                    continue


                            if(i % 2 != 0):
                                    Y.append(l)

                                    i=i+1



                    except ValueError:
                            pass
AA=len(X)
AA=AA-1

# Berechnungen der Distanz der Schrittlänge für jedes Frame
DIS=[]
for cont in range(0,AA):

    disabo= math.sqrt(
        math.pow((float(X[cont]) - float(X[cont+1])), 2) + math.pow((float(Y[cont]) - float(Y[cont+1])), 2))
    DIS.append(disabo)
    #if (Distanz <= DIS[cont]):
     #  Distanz=DIS[cont]

Schrittelänge=[]
DistanzGros=DIS[0]
Schritte=0
#der Abrechnungen  der Schrittlänge
#for test in range(0,len(DIS)):
#    if(DistanzGros <= DIS[test]):
#        DistanzGros = DIS[test]
#        if(DIS[test]<=20):
#            print("BOBo")
#            test=test+3
#            Schritte=Schritte+1
#            Schrittelänge.append(DistanzGros)
#            DistanzGros=0






#der abrechnung von den Zahlen der Schritte
Distanzklein=DIS[0]
#for test in range(0,len(DIS)):
#    print(test)
#    if (DIS[test] <= 20):
#        print("BOBo")
#        Schritte = Schritte + 1
#        Schrittelänge.append(DistanzGros)
#        test=test+3
#        DistanzGros = 0
 #       continue
#Schrittlänge rechnen
i=0
PositionG=[]
#for i in range(0,len(DIS)):
#    print(DIS[i])

#exit()
while i<len(DIS):
    if (DistanzGros <= DIS[i]):
        DistanzGros = DIS[i]

        Position = i

    if (DIS[i] <= 37):

        Schritte = Schritte + 1
        Schrittelänge.append(DistanzGros)
        DistanzGros=0
        PositionG.append(Position)
        i = i + 3
        if (DIS[i]<37):
            i= i + 5


    i=i+1
Schrittelänge.append(DistanzGros)
PositionG.append(Position)

#print(DIS)
#print(DistanzGros)
################################################## Arme Abrechnungen
with open("/home/developer/Downloads/armeDaten.txt","r") as data:
    plaintext=data.read()
    plaintext1=plaintext.split('\n')
    X=[]
    Y=[]
    i=0
    for line in plaintext1:
            #print(line)
            line1=line.replace(']','')
            line2=line1.replace('[','')
            k=line2.split(' ')
            for l in k :
                    try:
                            inNumberfloat = float(l)


                            if (i % 2 == 0):

                                    X.append(l)
                                    i=i+1

                                    continue


                            if(i % 2 != 0):
                                    Y.append(l)

                                    i=i+1



                    except ValueError:
                            pass
#AA=len(X)
#AA=AA-1
#print(AA)#muss etwas hier machen
#print(float(X[16])-float(Y[15]))
#print(X[15],Y[16])
#total= math.sqrt(math.pow((float(X[15])-float(X[16])),2)+math.pow((float(Y[15])-float(Y[16])),2))
#print(total)


#print(AA)
#for h in range (0,len(X)):
 #   print(X[h])
#print(Y[0])
#Distanz initialisieren
#print("Arme Abrechnung")
#Distanz1= math.sqrt(math.pow((float(X[0])-float(X[1])),2)+math.pow((float(Y[0])-float(Y[1])),2))
#print(Distanz)
# Berechnungen der Distanz der Schrittlänge für jedes Frame
DIS1=[]
for cont in range(0,AA):

    disabo1= math.sqrt(math.pow((float(X[cont]) - float(X[cont+1])), 2) + math.pow((float(Y[cont]) - float(Y[cont+1])), 2))
    DIS1.append(disabo1)
    #if (Distanz <= DIS[cont]):
     #  Distanz=DIS[cont]







#der abrechnung von den Zahlen der Schritte
#Distanzklein=DIS1[0]
#for test in range(0,len(DIS)):
#    print(test)
#    if (DIS[test] <= 20):
#        print("BOBo")
#        Schritte = Schritte + 1
#        Schrittelänge.append(DistanzGros)
#        test=test+3
#        DistanzGros = 0
 #       continue
#Schrittlänge rechnen

#print(DIS1)

################################################################################################



# DIS euclodian Fußdaten    DIS1 euclodian armdaten
dist_in_pixel = DIS1[PositionG[0]]
#print("disin pixel")
#print(dist_in_pixel)

dist_in_cm = 30
#pixel_per_cm = dist_in_pixel/dist_in_cm
#print(pixel_per_cm)


#print(PositionG)

#print(koko)
#print(PositionG)
#print(len(Schrittelänge),Schrittelänge)
F=0
for i in range(0,len(Schrittelänge)):
    dist_in_pixel = DIS1[PositionG[i]]
    #print("disin pixel")
    #print(dist_in_pixel)
    #initializierung von arme Größe
    #dist_in_cm = 25
    pixel_per_cm = dist_in_pixel / dist_in_cm
    #print(pixel_per_cm)

    Schrittelänge_per_cm=float(Schrittelänge[i])/pixel_per_cm
    #Kleine Schritte zu vermeiden
    if(Schrittelänge_per_cm <= 10):
        F=F+1
        i=i+1
        continue
    print("schritte  :")
    print(Schrittelänge_per_cm,"cm")
Total_schitte=len(Schrittelänge)-F
print("der zahle der Schitten :",Total_schitte)
