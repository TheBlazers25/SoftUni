targets = [int(x) for x in input().split()]
shoot = input()
targets_len = len(targets)


while shoot != "End":
    shoot = int(shoot)

    if 0 <= shoot < targets_len:
        target = targets[shoot]
        targets[shoot] = -1
        for i in range(targets_len):

            if targets[i] == -1:
                continue

            if targets[i] > target:
                targets[i] -= target
            else:
                targets[i] += target

    shoot = input()

print(f"Shot targets: {sum(1 for x in targets if x == -1)} ->", *targets)
