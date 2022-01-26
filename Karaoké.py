class Player : 
    def __init__(self,scores,pseudo) :
        self.pseudo=pseudo
        self.__scores=scores
        self.__meilleurScore = 0
        self.__pireScore = 0
        self.__moyenne = 0
        self.__total = 0
        
    def getTotal(self):
        return self.__total

    def setTotal(self):
        self.__total = sum(self.__scores)
        

    def getMoyenne(self):
        return self.__moyenne

    def setMoyenne(self):
        self.__moyenne = self.__total/len(self.__scores)

    def getMeilleurScore(self):
        return self.__meilleurScore

    def setMeilleurScore(self):
        self.__meilleurScore= self.__scores.index(max(self.__scores))
    
    def getPireScore(self):
        return self.__pireScore

    def setPireScore(self):
        self.__pireScore= self.__scores.index(min(self.__scores))
    
    def getScore (self):
        return self.__scores

    def addScore (self, num, nvscore):
        if nvscore>=50 : 
            self.__scores[num]=nvscore

    def afficheScore (self):
        print ("Bonjour ",self.pseudo)
        print ("Votre score sur la chanson 1 est de " + str(self.__scores[0]) )
        print ("Votre score sur la chanson 2 est de " + str(self.__scores[1]) )
        print ("Votre score sur la chanson 3 est de " + str(self.__scores[2]) )
        print ("Votre score sur la chanson 4 est de " + str(self.__scores[3]) )
        print ("Votre score sur la chanson 5 est de " + str(self.__scores[4]) )
        print ("Votre moyenne est de " + str(self.__moyenne))
        print ("Votre total de points est de " + str(self.__total))
        print ("Votre meilleur score est sur la chanson numéro ",self.__meilleurScore)
        print ("Votre pire score est sur la chanson numéro ",self.__pireScore)

    
    

essai=Player([56,83,69,75,50], "test")
essai.afficheScore()
essai.getTotal()
essai.setTotal()
essai.getMoyenne()
essai.setMoyenne()
essai.getMeilleurScore()
essai.setMeilleurScore()
essai.getPireScore()
essai.setPireScore()
essai.getScore()
essai.addScore(2,37)
essai.afficheScore()
essai.addScore(4,66)
essai.afficheScore()

class Karaoke : 
    def __init__(self):
        self.players=[]
        self.__chansons={0: ["test",0],1:["truc",0],2:["machin",0],3:["bidule",0],4:["essai",0]}
        self.__msChanson= 0
    
    def getMSChanson (self):
        return self.__msChanson

    def addPlayer (self,scores,pseudo):
        pass
    