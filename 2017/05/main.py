with open('input.txt', 'r') as f:
    lines = f.readlines()

instructions = [int(l.strip()) for l in lines]
# instructions = [0, 3, 0, 1, -3]

index = 0
numSteps = 0

while 0 <= index < len(instructions):
    moveDistance = instructions[index]
    # print(f"\tprocessing instruction {moveDistance} at {index}")
    instructions[index] = moveDistance + 1
    index += moveDistance
    numSteps += 1

print(f"Finished in {numSteps} steps")

print("-----------------")

instructions = [int(l.strip()) for l in lines]
# instructions = [0, 3, 0, 1, -3]

index = 0
numSteps = 0

while 0 <= index < len(instructions):
    moveDistance = instructions[index]
    # print(f"\tprocessing instruction {moveDistance} at {index}")
    if moveDistance > 2:
        instructions[index] = moveDistance - 1
    else:
        instructions[index] = moveDistance + 1
    index += moveDistance
    numSteps += 1

print(f"Finished in {numSteps} steps")