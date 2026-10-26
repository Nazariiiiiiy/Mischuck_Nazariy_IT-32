
import math
import random
import sys
from datetime import datetime
from pathlib import Path


NAME = "Nazar"
SURNAME = "Mischuck "
GROUP = "IT-32"
YEAR = 2009  


HISTORY = Path(__file__).parent / "results" / "history.csv"

print(f"{NAME} {SURNAME}, {GROUP}")

random.seed(YEAR) 


root = random.randint(5, 30)
text1 = f"sqrt({root * root})"
answer1 = math.isqrt(root * root)

n = random.randint(3, 7)
text2 = f"{n}!"
answer2 = math.factorial(n)

a = random.randint(10, 99)
b = random.randint(10, 99)
text3 = f"gcd({a}, {b})"
answer3 = math.gcd(a, b)

m = random.randint(5, 9)
k = random.randint(2, 4)
text4 = f"comb({m}, {k})"
answer4 = math.comb(m, k)

percent = random.choice([5, 10, 15, 20, 25])
number = random.randint(5, 30) * 20
text5 = f"{percent}% of {number}"
answer5 = percent * number // 100

tasks = [(text1, answer1), (text2, answer2), (text3, answer3),
         (text4, answer4), (text5, answer5)]


start = datetime.now()
score = 0
for i, (text, answer) in enumerate(tasks, start=1):
    try:
        reply = input(f"{i}) {text} = ")
    except EOFError:
        reply = ""
    try:
        value = int(reply.strip())
    except ValueError:
        value = None  # нечислова відповідь - неправильна
    if value == answer:
        print("   correct")
        score += 1
    else:
        print(f"   wrong, answer: {answer}")
end = datetime.now()
seconds = round((end - start).total_seconds(), 1)
print(f"score: {score}/5, time: {seconds} s")


HISTORY.parent.mkdir(exist_ok=True)
is_new = not HISTORY.exists()
with HISTORY.open("a", encoding="utf-8") as f:
    if is_new:
        f.write("# datetime;score;seconds\n")
    f.write(f"{start:%Y-%m-%d %H:%M};{score};{seconds}\n")


attempts = []
with HISTORY.open(encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line == "" or line.startswith("#"):
            continue
        parts = line.split(";")
        try:
            attempts.append((parts[0], int(parts[1]), float(parts[2])))
        except (ValueError, IndexError):
            print(f"warning: bad line in history: {line}", file=sys.stderr)


best = max(attempts, key=lambda x: (x[1], -x[2]))
print(f"attempts: {len(attempts)}, best: {best[1]}/5 in {best[2]} s ({best[0]})")
