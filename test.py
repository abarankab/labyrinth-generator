import random
from labyrinth import Labyrinth

print("Started tests")

for i in range(1000):
    w = random.randint(1, 40)
    h = random.randint(1, 40)
    seed = random.randint(1, 10 ** 10)
    random.seed(seed)

    try:
        labyrinth = Labyrinth(w, h)
    except Exception as e:
        print(w, h, seed)
        raise e

print("OK!")
