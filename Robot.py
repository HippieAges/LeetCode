def isRobotBounded(instructions: str) -> bool:
    robot_pos = [0, 0]
    direction = "north" # initial direction is north

    bounds = {
        'G': 
            {
                "north": [0, 1],
                "south": [0, -1],
                "west": [-1, 0],
                "east": [1, 0]
            },
        'L':
            {
                "north": "west",
                "south": "east",
                "west": "south",
                "east": "north"
            },
        'R':
            {
                "north": "east",
                "south": "west",
                "west": "north",
                "east": "south"
            }
    }

    # easy case: if only G then return False
    if instructions.count('G') == len(instructions):
        return False
    
    for instruction in instructions:
        if instruction == 'G':
            robot_pos = [sum(index) for index in list(zip(bounds['G'][direction], robot_pos))]
        elif instruction == 'L':
            direction = bounds['L'][direction]
        else: # instruction == 'R'
            direction = bounds['R'][direction]

    return True if robot_pos == [0, 0] or direction != "north" else False