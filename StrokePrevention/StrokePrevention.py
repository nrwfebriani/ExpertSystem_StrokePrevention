from experta import *
import sys

class StrokePreventions(KnowledgeEngine):
    """Info about the person"""
    username = "",
    pass

    @DefFacts()
    def needed_data(self):
        """ 
        This is a method which is called everytime engine.reset() is called.
        It acts like a constructor to this class.
        """        
        yield Fact(findScore = 'true')
        print("Hello!\nThis is a program to find out whether you have risk factors for having stroke or not.\nThere will be several questions for you to answer.\n")

    @Rule(Fact(findScore = 'true'),NOT(Fact(name = W())),salience = 1000)
    def ask_name(self):
        self.username = input("What's your name?\n")
        self.declare(Fact(name = self.username))

    @Rule(Fact(findScore='true'), NOT (Fact(age = W())),salience = 995)
    def isOld(self):
        self.age = input("\nAre you 55 years old or older?\nPlease type y/n\n")
        self.age = self.age.lower()
        self.declare(Fact(age = self.age.strip().lower()))

    @Rule(Fact(findScore='true'), NOT (Fact(gender = W())),salience = 990)
    def isWoman(self):
        self.gender = input("\nAre you a woman?\nPlease type y/n\n")
        self.gender = self.gender.lower()
        self.declare(Fact(gender = self.gender.strip().lower()))

    @Rule(Fact(findScore='true'), NOT (Fact(stroke_history = W())),salience = 985)
    def hasStroke(self):
        self.stroke_history = input("\nWere you ever told by a physician that you had stroke and/or transient ischemic attack (TIA)?\nPlease type y/n\n")
        self.stroke_history = self.stroke_history.lower()
        self.declare(Fact(stroke_history = self.stroke_history.strip().lower()))

    @Rule(Fact(findScore='true'), NOT (Fact(family_history = W())),salience = 980)
    def isGenetic(self):
        self.family_history = input("\nHas any of your family member had stroke before?\nPlease type y/n\n")
        self.family_history = self.family_history.lower()
        self.declare(Fact(family_history = self.family_history.strip().lower()))

    @Rule(Fact(findScore='true'), NOT (Fact(hypertension = W())),salience = 975)
    def isHypertensive(self):
        self.hypertension = input("\nAre you considered to be hypertensive? (BP more than 130/80)\nPlease type y/n\n")
        self.hypertension = self.hypertension.lower()
        self.declare(Fact(hypertension = self.hypertension.strip().lower()))
        
    @Rule(Fact(findScore='true'), NOT (Fact(overweight = W())),salience = 970)
    def isOverweight(self):
        self.overweight = input("\nAre you considered to be overweight? (BMI more than 24.9)\nPlease type y/n\n")
        self.overweight = self.overweight.lower()
        self.declare(Fact(overweight = self.overweight.strip().lower()))
        
    @Rule(Fact(findScore='true'), NOT (Fact(smoking = W())),salience = 965)
    def isSmoker(self):
        self.smoking = input("\nDo you smoke more than 20 cigarettes per day?\nPlease type y/n\n")
        self.smoking = self.smoking.lower()
        self.declare(Fact(smoking = self.smoking.strip().lower()))
        
    @Rule(Fact(findScore='true'), NOT (Fact(lack_of_exercise = W())),salience = 960)
    def isInactive(self):
        self.lack_of_exercise = input("\nDo you do physical activity less than 3.5 hours/week?\nPlease type y/n\n")
        self.lack_of_exercise = self.lack_of_exercise.lower()
        self.declare(Fact(lack_of_exercise = self.lack_of_exercise.strip().lower()))
        
    @Rule(Fact(findScore='true'), NOT (Fact(high_cholesterol = W())),salience = 955)
    def isHyperlipidemia(self):
        self.high_cholesterol = input("\nDo you have high level of LDL Cholesterol? (LDL cholesterol level more than 130mg/dL)\nPlease type y/n\n")
        self.high_cholesterol = self.high_cholesterol.lower()
        self.declare(Fact(high_cholesterol = self.high_cholesterol.strip().lower()))

    @Rule(Fact(findScore = 'true'))
    def getScore(self):
            mapScore = []
            mapScore.append('hypertension')
            mapScore.append('overweight')
            mapScore.append('smoking')
            mapScore.append('lack_of_exercise')
            mapScore.append('high_cholesterol')
            mapScore.append('age')
            mapScore.append('gender')
            mapScore.append('stroke_history')
            mapScore.append('family_history')
            print("\n\nWe checked the following factors: ",mapScore)
            mapScore_val=[self.hypertension,self.overweight,self.smoking,self.lack_of_exercise,self.high_cholesterol,self.age,self.gender,self.stroke_history,self.family_history]
            print("\nAnswers from users are: ", mapScore_val)
            
            yes_factors = []
            for i in range(0,len(mapScore_val)):
                if mapScore_val[i] == 'y':
                    yes_factors.append(mapScore[i])
            score = len(yes_factors)
            if score > 0:
                print("\nYour risk factors noticed are : ", yes_factors)
                count = 0
                for x in yes_factors: 
                    if x == 'age':
                        yes_factors.remove('age')
                        count+=1
                for x in yes_factors: 
                    if x == 'stroke_history':
                        yes_factors.remove('stroke_history')
                        count+=1
                for x in yes_factors: 
                    if x == 'gender':
                        yes_factors.remove('gender')
                        count+=1
                for x in yes_factors: 
                    if x == 'family_history':
                        yes_factors.remove('family_history')
                        count+=1
                if count > 0:
                    yes_factors.append('general')

                print("\n\nNo need to worry, " + self.username + "!\nWe have several information and advices for you to lower your risk of having stroke in the future based on the data that you submitted:\n")

                for x in yes_factors:
                    file = open('factors/' + x + '.txt', 'r')
                    print(file.read())
                    file.close()
                    print("\n")
            else:
                print("\n\nCongratulations, "+ self.username + "!\nYou don't have any risk factors.")

            #print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
            print("Thank you for using our services.")
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")

if __name__ == "__main__":
    engine = StrokePreventions()
    engine.reset()
    engine.run()
    print('Printing engine facts after 1 run',engine.facts)