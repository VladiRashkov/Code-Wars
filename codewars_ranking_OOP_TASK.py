class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0

    @staticmethod
    def rank_to_int(rank):
       
        if rank < 0:
            return rank + 8
        else:
            return rank + 7

    @staticmethod
    def int_to_rank(value):
        
        if value < 8:
            return value - 8
        else:
            return value - 7

    def inc_progress(self, activity_rank):
        if activity_rank < -8 or activity_rank == 0 or activity_rank > 8:
            raise ValueError("Invalid activity rank")

        if self.rank == 8:
            return "You have reached the sky"

        user_rank_int = self.rank_to_int(self.rank)
        activity_rank_int = self.rank_to_int(activity_rank)
        rank_diff = activity_rank_int - user_rank_int

        if rank_diff == 0:
            self.progress += 3
        elif rank_diff == -1:
            self.progress += 1
        elif rank_diff > 0:
            self.progress += 10 * rank_diff * rank_diff

        while self.progress >= 100:
            self.progress -= 100
            next_rank_int = self.rank_to_int(self.rank) + 1
            self.rank = self.int_to_rank(next_rank_int)

            if self.rank == 8:
                self.progress = 0
                return "You have reached the sky"

        if self.rank == 0:
            self.rank = 1



user = User()
user.inc_progress(-7) 
print(user.rank)       
print(user.progress)  

user.inc_progress(-5)
print(user.rank)       
print(user.progress)   
