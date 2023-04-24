from helpers.complexity import *
from helpers.raw import *

filename = 'sample.py'

with open(filename) as f:
    source = f.read()

def findComplexity():
    results = analyze(source)
    blocks = cc_visit(source)

    print("""
==================================================================
    1 - 5        A (low risk - simple block)
    6 - 10       B (low risk - well structured and stable block)
    11 - 20      C (moderate risk - slightly complex block)
    21 - 30      D (more than moderate risk - more complex block)
    31 - 40      E (high risk - complex block, alarming)
    41+          F (very high risk - error-prone, unstable block)
==================================================================
""")

    for block in blocks:
        rank = cc_rank(block.complexity)
        print(f'{block.letter} {block.name}: {block.lineno} [{block.complexity} {rank}]')

def raw_stats():
    results = analyze(source)
    print(f"LOC: {results.loc}\n"
          f"LLOC: {results.lloc}\n"
          f"SLOC: {results.sloc}\n"
          f"Comments: {results.comments}\n"
          f"Single comments: {results.single_comments}\n"
          f"Multi: {results.multi}\n"
          f"Blank: {results.blank}\n"
          f"- Comment Stats\n")
    
    if results.lloc != 0:
        print(f"    (C % L): {results.comments / results.lloc:.0%}\n"
              f"    (C + M % L): {(results.comments + results.multi) / results.lloc:.0%}")
    else:
        print("LLOC is zero, cannot calculate comment stats.")
    
    if results.sloc != 0:
        print(f"    (C % S): {results.comments / results.sloc:.0%}\n")
    else:
        print("SLOC is zero, cannot calculate comment stats.")



print("File: ", filename)
print("Type c for complexity analysis, r for raw stats and q to quit")
choice = input("Enter your choice: ")

while choice != 'q':
    if choice == 'c':
        findComplexity()
    elif choice == 'r':
        raw_stats()
    else:
        print("Invalid choice")

    print("Type c for complexity analysis, r for raw stats and q to quit")
    choice = input("Enter your choice: ")