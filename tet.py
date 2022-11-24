
class Guessing_game:
    correct_number=15
    def __init__(self, number):
        self.number=number
    def is_correct(self,guess):
        if guess==15:
            return True 
    def is_too_high(self,guess):
        if guess > 15:
            return True
    def is_too_low(self, guess):
        if guess<15:
            return True
#GuessingGame=[]
game = Guessing_game(15)
guess = 1 
while not game.is_correct(guess): 
    guess = int(input("Enter guess:"))     
    if game.is_too_low(guess):        
        print("That is too low!")     
    elif game.is_too_high(guess):         
        print("That is too high!") 
print("That is correct!") 
##################################################################
class Counte_sum:
    sum_of_the_number=18
    def __init__(self, count_the_value):
        self.count_the_value=count_the_value
    def is_corrects(self,Counte):
        if Counte==18:
            return True
    def is_too_lows(self, Counte):
        if Counte<18:
            return True
    def is_too_highs(self, Counte):
        if Counte > 15:
            return True
sum=Counte_sum(18)
Counte=1
while not sum.is_corrects(Counte):
    Counte=int(input("enter the number ="))
    if sum.is_too_lows(Counte):
        print ("it is too low ")
    elif sum.is_too_highs(Counte):
        print("the number is too high")
print ("it is correct")
###########################################################
class Add_sum:
    sum_of_the_integer=20
    def __init__(self, Add):
        self.Add = Add
    def is_right(self,numbers):
        if numbers==20:
            return True
    def is_higher(self, numbers):
        if numbers > 20:
            return True
    def is_lower(self, nmbers):
        if numbers < 20:
            return True
Add=Add_sum(20)
numbers=1
while not Add.is_right(numbers):
    numbers=int(input("inter the number you want to add! ="))
    if Add.is_lower(numbers):
        print("The number is too llow ")
    elif Add.is_higher(numbers):
        print("The number is too high try agien ")
print("the number you enterd is true")
##############################################################
class Andoms_age:
    guess_the_age_of_andom=34
    def __init__(self,age):
        self.age=age
    def is_tikkl(self,kuser):
        if kuser==34:
            return True
    def is_whidu(self,kuser):
        if kuser < 34:
            return True
    def is_bezihu(self,kuser):
        if kuser > 34:
            return True 
age= Andoms_age(34)
kuser=1
while not age.is_tikkl(kuser):
    kuser=int(input("Eti tikilna kusri atu! = "))
    if age.is_whidu(kuser):
        print("Eizi zetekayo kusry wihidu degimka fetin ")
    elif age.is_bezihu(kuser):
        print("Ezi zetekayo kusri bezihu degmka fetn")
print ("Tikil tigmit wedi_haram")
##################################################
class Xeweta_gemt:
    etitikikilna = 13
def __init__(self,xu):
    self.xu=xu
def iti_gmiot_haki(self,xubuq):
    if xubuq==13:
        return True
def iti_gimt_entewiwidu(self,xubuq):
    if xubuq < 13:
        return True
def iti_gimt_entebezihu(self,xubuq):
    if xubuq > 13:
        return True
xu=Xeweta_gemt(13)
xubuq = 1
while not xu.iti_gmiot_haki(xubuq):
    xubuq=int(input("eti zidelekayo kusiri aetu: "))
    if xu.iti_gimt_entewiwidu(xubuq):
        print("bkibretka weskelu ")
    elif xu.iti_gimt_entebezihu(xubuq):
        print("bkibretka kenselu")
print ("teawet xbuk gimt")
