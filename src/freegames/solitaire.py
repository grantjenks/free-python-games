import random

SUITS = ['♠', '♥', '♦', '♣']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
COLOR = {'♠': 'black', '♣': 'black', '♥': 'red', '♦': 'red'}


class Card:
    def __init__(self, suit, rank, up=False):
        self.suit = suit
        self.rank = rank
        self.up = up        # face-up flag

    def __str__(self):
        return f'{self.rank}{self.suit}' if self.up else '??'


class Solitaire:
    def __init__(self):
        self.stock = []
        self.waste = []
        self.found = {s: [] for s in SUITS}
        self.piles = [[] for _ in range(7)]
        self.deal()

    # deal opening layout
    def deal(self):
        deck = [Card(s, r) for s in SUITS for r in RANKS]
        random.shuffle(deck)
        for i in range(7):
            for j in range(i + 1):
                c = deck.pop()
                c.up = (j == i)
                self.piles[i].append(c)
        self.stock = deck

    # helpers
    def _rank(self, c): return RANKS.index(c.rank)
    def _diff_color(self, a, b): return COLOR[a.suit] != COLOR[b.suit]

    # draw from stock
    def draw(self):
        if self.stock:
            c = self.stock.pop()
            c.up = True
            self.waste.append(c)
        else:
            self.stock = list(reversed(self.waste))
            for c in self.stock:
                c.up = False
            self.waste = []

    # pile X → foundation
    def pile_to_found(self, idx):
        pile = self.piles[idx]
        if not pile or not pile[-1].up:
            return
        card = pile[-1]
        top = self.found[card.suit][-1] if self.found[card.suit] else None
        if (top is None and card.rank == 'A') or (top and self._rank(card) == self._rank(top) + 1):
            self.found[card.suit].append(pile.pop())
            if pile and not pile[-1].up:
                pile[-1].up = True

    # move pile A → pile B
    def pile_to_pile(self, frm, to):
        if frm == to:
            return
        src, dst = self.piles[frm], self.piles[to]
        if not src:
            return
        for cut, c in enumerate(src):
            if c.up:
                break       # first face-up
        else:
            return
        moving = src[cut:]
        if not dst:
            if moving[0].rank != 'K':
                return
            dst.extend(moving)
            del src[cut:]
        else:
            top = dst[-1]
            if self._diff_color(top, moving[0]) and self._rank(moving[0]) == self._rank(top) - 1:
                dst.extend(moving)
                del src[cut:]
        if src and not src[-1].up:
            src[-1].up = True

    # print board
    def show(self):
        print("\nStock:", len(self.stock), "cards | Waste:", self.waste[-1] if self.waste else 'Empty')
        print("Foundations:", {s: (str(p[-1]) if p else 'Empty') for s, p in self.found.items()})
        print("\nPiles:")
        for i, p in enumerate(self.piles):
            print(f"{i}: ", *p)

    # main loop
    def play(self):
        while True:
            self.show()
            print("\nCommands: d = draw   f X = pile X→foundation   p A B = pile A→pile B   q = quit")
            cmd = input("> ").split()
            if not cmd:
                continue
            if cmd[0] == 'q':
                break
            if cmd[0] == 'd':
                self.draw()
            elif cmd[0] == 'f' and len(cmd) == 2:
                self.pile_to_found(int(cmd[1]))
            elif cmd[0] == 'p' and len(cmd) == 3:
                self.pile_to_pile(int(cmd[1]), int(cmd[2]))


if __name__ == "__main__":
    Solitaire().play()
