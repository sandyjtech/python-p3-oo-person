class Person:
    def __init__(self, first_name, bank_account=25, happiness=8, hygiene=8):
        self.first_name = first_name
        self.bank_account = bank_account
        self.happiness = happiness
        self.hygiene = hygiene

    def get_name(self):
        return self.first_name

    def is_clean(self):
        if self.hygiene > 7:
            return True
        else:
            return False
    
    def is_happy(self):
        if self.happiness > 7:
            return True
        else:
            return False
        
    def get_paid(self, amount):
        self.bank_account += amount
        print("all about the benjamins")

    def take_bath(self):
        self.hygiene += 4
        print("♪ Rub-a-dub just relaxing in the tub ♫")

    def work_out(self):
        self.happiness += 2
        self.hygiene -= 3
        return "♪ another one bites the dust ♫"
        
    def call_friend(self, friend):
        self.happiness += 3
        friend.happiness += 3
        
        return f"Hi {friend.name}! It's {self.name}. How are you?"
    
    def start_conversation(self, friend, topic):
        self.topic = topic
        self.friend = friend
        if topic == "politics":
            self.happiness -= 2
            friend.happiness -= 2
            return "blah blah partisan blah lobbyist"
        elif topic == "weather":
            self.happiness += 1
            friend.happiness += 1
            return "blah blah sun blah rain"
        else:
            return "blah blah blah blah blah"
    
    name = property(get_name)
    
    

    

      
