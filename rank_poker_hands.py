class PokerHand:
    RESULT = ["Loss", "Tie", "Win"]
    RANKS = '23456789TJQKA'
    
    def __init__(self, hand):
        self.hand = hand.split()
        self.ranks = sorted([card[0] for card in self.hand], key=lambda x: PokerHand.RANKS.index(x))
        self.suits = [card[1] for card in self.hand]
        
    @staticmethod
    def all_elements_same(lst):
        return all(x == lst[0] for x in lst)
    
    def straight_check(self):
        """Check for straight and return the highest card in the straight."""
        idx_list = [PokerHand.RANKS.index(rank) for rank in self.ranks]
        idx_list.sort()
        for i in range(len(idx_list) - 4):
            if idx_list[i:i + 5] == list(range(idx_list[i], idx_list[i] + 5)):
                return PokerHand.RANKS[idx_list[i + 4]]
        return False

    def flush_check(self):
        """Check for flush."""
        if PokerHand.all_elements_same(self.suits):
            return True
        return False

    def kind(self, n):
        """Return the first rank that this hand has exactly n of."""
        for rank in self.ranks:
            if self.ranks.count(rank) == n:
                return rank
        return None

    def two_pair(self):
        """If there are two pairs, return the two ranks as a tuple."""
        pairs = [rank for rank in self.ranks if self.ranks.count(rank) == 2]
        if len(pairs) == 4:
            return tuple(sorted(set(pairs), key=lambda x: PokerHand.RANKS.index(x), reverse=True))
        return None
    
    def hand_rank(self):
        """Return a value indicating the ranking of the hand."""
        if self.flush_check() and self.straight_check():
            return (8, self.straight_check())
        elif self.kind(4):
            return (7, self.kind(4), self.kind(1))
        elif self.kind(3) and self.kind(2):
            return (6, self.kind(3), self.kind(2))
        elif self.flush_check():
            return (5, self.ranks)
        elif self.straight_check():
            return (4, self.straight_check())
        elif self.kind(3):
            return (3, self.kind(3), self.ranks)
        elif self.two_pair():
            return (2, self.two_pair(), self.kind(1))
        elif self.kind(2):
            return (1, self.kind(2), self.ranks)
        else:
            return (0, self.ranks)
    
    def compare_with(self, other):
        """Compare self hand with other hand."""
        other_hand = PokerHand(other)
        self_rank = self.hand_rank()
        other_rank = other_hand.hand_rank()
        
        if self_rank > other_rank:
            return PokerHand.RESULT[2]  # Win
        elif self_rank < other_rank:
            return PokerHand.RESULT[0]  # Loss
        else:
            return PokerHand.RESULT[1]  # Tie

# Example usage
poker_hand = PokerHand("KS 2H 5C JD TD")
print(poker_hand.compare_with("AS AH 2H AD AC")) 
