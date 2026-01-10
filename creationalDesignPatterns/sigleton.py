class JudgeAnalytics:
    submitCount = 0
    def __init__(self):
        self.runCount = 0
    def runCountt(self):
        self.runCount+=1
    def submitCount(self):
        submitCount+=1
    def getRunCount(self):
        return self.runCount
    def submitCount(self):
        return submitCount
    
analytics = JudgeAnalytics()
analytics.runCountt()
# print(analytics.getRunCount())

analytics2 = JudgeAnalytics()
analytics2.runCountt()
# print(analytics2.getRunCount())

#from the above function we can see that the runCount is not shared between the two instances of the class JudgeAnalytics.
#this is why singleton pattern is used to make sure that only one instance of the class is created and shared between all the instances of the class.


#Sigleton Pattern means that only one instance of a class is created and shared between all the instances of the class.

#Singleton implementation

#Eager loading

# Class implementing Eager Loading
class EagerSingleton:
    # Static instance created eagerly

    __instance = None #by using __instance we are making it private, internally the name will be changed to _EagerSingleton__instance this makes it difficult to access from outside the class.

    # Private constructor simulation
    def __init__(self):
        if EagerSingleton.__instance is not None:# Prevents creation of multiple instances
            raise Exception("This class is a singleton!")
        # Declaring it private prevents creation of its object using the new keyword
        EagerSingleton.__instance = self #Assigning the instance to the static variable for first time

    # Method to get the instance of class
    @staticmethod
    def getInstance():
        return EagerSingleton.__instance  # Always returns the same instance

# Eager initialization (happens at load time)
EagerSingleton._EagerSingleton__instance = EagerSingleton()
# obj = EagerSingleton()
# obj.getInstance()
# print("Eager Singleton Instance:", EagerSingleton.getInstance())