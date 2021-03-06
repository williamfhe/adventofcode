programs = list("abcdefghijklmnop")

with open("input.txt") as f:
    dance = f.readline().split(',')

n = 1_000_000_000  # 1 billion

seen = list()

for _ in range(n):
    
    prog = "".join(programs)
    if prog in seen:
        break
    seen.append(prog)

    for move in dance:
        if move[0] == 's':
            dis = int(move[1:])
            programs = programs[-dis:] + programs[:-dis]
        else:
            a, b = move[1:].split('/')
            if move[0] == 'x':
                a, b = int(a), int(b)
            else:
                a, b = programs.index(a), programs.index(b)

            programs[a], programs[b] = programs[b], programs[a]

print(seen[n % len(seen)])
