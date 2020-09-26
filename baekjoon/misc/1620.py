from .. import util

example = """
26 5
Bulbasaur
Ivysaur
Venusaur
Charmander
Charmeleon
Charizard
Squirtle
Wartortle
Blastoise
Caterpie
Metapod
Butterfree
Weedle
Kakuna
Beedrill
Pidgey
Pidgeotto
Pidgeot
Rattata
Raticate
Spearow
Fearow
Ekans
Arbok
Pikachu
Raichu
25
Raichu
3
Pidgey
Kakuna
"""
util.setinput(example)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pocketmon = {}
pocketmon_num = {}
for idx in range(N):
    name = input().strip()
    pocketmon[idx + 1] = name
    pocketmon_num[name] = idx + 1

for _ in range(M):
    question = input().strip()
    if question.isnumeric():
        num = int(question)
        print(pocketmon[num])
    else:
        print(pocketmon_num[question])
