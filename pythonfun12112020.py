#class name():
    #def __init__(self, s):
        #self.letters = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,
                        #"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26,"A":27,"B":28,"C":29,
                        #"D":30,"E":31,"F":32,"G":33,"H":34,"I":35,"J":36,"K":37,"L":38,"M":39,"N":40,"O":41,"P":42,"Q":43,
                        #"R":44,"S":45,"T":46,"U":47,"V":48,"W":49,"X":50,"Y":51,"Z":52}
        #self.string = s
        #self.num = 0
        
    #def __mul__(self, other):
        #power = 0
        #for i in self.string:
            #for j in other.string:
                #power = power + (self.letters[i] * other.letters[j])
        #print(self.string + " and " + other.string + "'s relationship power is:", end = " ")
        #print(power)
        #return power
        
    #def calc_name_value(self):
        #for i in self.string:
            #self.num = self.num + self.letters[i]
        #print(self.string + "'s value is:", end = " ")
        #print(self.num)
        

#Cassidy = name("Cassidy")
#Cassidy.calc_name_value()

#Chase = name("Chase")
#Chase.calc_name_value()

#love = Chase * Cassidy

#Patunia = name("Patunia")
#Patunia.calc_name_value()

#Skylar = name("Skylar")
#Skylar.calc_name_value()

#hope = Patunia * Skylar

import turtle as t

t.speed(0)

t.circle(5,90)

for i in range(0,30):
    t.forward(5)
    t.left(12)

#t.left(60)

#for i in range(0,12):
    #for j in range(0,30):
        #t.forward(1)
        #t.left(6)
    #t.right(150 + i)
    
#for i in range(0,30):
    #t.forward(4)
    #t.left(8)

#t.hideturtle()
t.exitonclick()
    