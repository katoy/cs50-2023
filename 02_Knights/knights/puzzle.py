from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# character is either a knight or a knave.
# A knight will always tell the truth: if knight states a sentence, then that sentence is true.
# Conversely,
# a knave will always lie: if a knave states a sentence, then that sentence is false.

# Puzzle 0
# A says "I am both a knight and a knave."
sentence0 = And(AKnight, AKnave)

knowledge0 = And(
    # A is a knight or a knave, but not both:
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),

    Implication(AKnight, sentence0 ),
    Implication(AKnave, Not(sentence0 ))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
sentence1 = And(AKnave, BKnave)

knowledge1 = And(
    # A and B are knights or knaves, but not both:
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),

    Implication(AKnight, sentence1),
    Implication(AKnave, Not(sentence1))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
sentence2_A = Or(
    And(AKnight, BKnight),
    And(AKnave, BKnave)
)
sentence2_B = Or(
    And(AKnight, BKnave),
    And(AKnave, BKnight)
)

knowledge2 = And(
    # A and B are knights or knaves but not both:
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),

    Implication(AKnight, sentence2_A),
    Implication(AKnave, Not(sentence2_A)),

    Implication(BKnight, sentence2_B),
    Implication(BKnave, Not(sentence2_B))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
sentence3_A = Or(AKnight, AKnave)
sentence3_B = And(AKnight, CKnave)
sentence3_C = AKnight

knowledge3 = And(
    # A, B and C are knights or knaves but not both:
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    And(Or(CKnight, CKnave), Not(And(CKnight, CKnave))),

    Implication(AKnight, sentence3_A),
    Implication(AKnave, Not(sentence3_A)),

    Implication(BKnight, sentence3_B),
    Implication(BKnave, Not(sentence3_B)),

    Implication(CKnight, sentence3_C),
    Implication(CKnave, Not(sentence3_C)),
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
