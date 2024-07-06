from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(Or(Not(AKnight),And(AKnight,AKnave)),
                And(Or(AKnave,AKnight),Not(And(AKnave,AKnight))),
                
    # TODO
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(Or(Not(AKnight),And(AKnave,BKnave)),
                Or(Not(AKnave), Or(Or(And(AKnight,BKnave),And(AKnave,BKnight),
                                    And(AKnight,BKnight)))),
                                    And(Or(AKnave,AKnight),Not(And(AKnave,AKnight)))
                
    # TODO
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(Or(Not(AKnight),Or(And(AKnight,BKnight),And(AKnave,BKnave))),
                Or(Not(AKnave),Or(And(AKnight,BKnave),And(AKnave,BKnight))),
                Or(Not(BKnight),Or(And(AKnight,BKnave),And(AKnave,BKnight))),
                Or(Not(BKnave),Or(And(AKnight,BKnight),And(AKnave,BKnave))),
                And(Or(AKnave,AKnight),Not(And(AKnave,AKnight))),
                And(Or(BKnave,BKnight),Not(And(BKnave,BKnight)))
                
    # TODO
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
                And(Or(Not(AKnight),AKnight),Not(And(Or(Not(AKnight),AKnave)))),
                Or(Not(BKnight),Or(Not(AKnight),AKnave)),
                
                And(Or(AKnave,AKnight),Not(And(AKnave,AKnight))),
                Or(Not(BKnight),CKnave),
                Or(Not(BKnave),CKnight),
                Or(Not(CKnight),AKnight),
                Or(Not(CKnave),AKnave),
                
                And(Or(BKnave,BKnight),Not(And(BKnave,BKnight))),
                And(Or(CKnave,CKnight),Not(And(CKnave,CKnight)))
    # TODO
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
