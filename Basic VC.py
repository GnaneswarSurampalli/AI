def vacuum_cleaner(location, status):
    if status == 'Dirty':
        return 'Suck'
    elif location == 'A':
        return 'Right'
    elif location == 'B':
        return 'Left'

environments = [
    ['A','Dirty','Dirty'],
    ['A','Clean','Dirty'],
    ['B','Dirty','Clean'],
    ['A','Clean','Clean'],
    ['B','Clean','Clean']
]

total_A = total_B = 0
clean_A = clean_B = 0
step = 1

for env in environments:
    loc, roomA, roomB = env
    current_room_status = roomA if loc == 'A' else roomB
    action = vacuum_cleaner(loc, current_room_status)

    if action == 'Suck':
        if loc == 'A':
            roomA = 'Clean'
        else:
            roomB = 'Clean'

    if loc == 'A':
        total_A += 1
        if roomA == 'Clean':
            clean_A += 1
    else:
        total_B += 1
        if roomB == 'Clean':
            clean_B += 1

    overall_status = "Cleaned" if roomA == 'Clean' and roomB == 'Clean' else "Pending"

    percent_A = (clean_A / total_A) * 100 if total_A > 0 else 0
    percent_B = (clean_B / total_B) * 100 if total_B > 0 else 0

    print(f"Step {step}: Location {loc}, Perceived {current_room_status}")
    print(f"Action Taken: {action}")
    print(f"Room A Status: {roomA}")
    print(f"Room B Status: {roomB}")
    print(f"Overall Status: {overall_status}")
    print(f"Cleaning Percentages -> Room A: {percent_A:.0f}%, Room B: {percent_B:.0f}%\n")

    env[1] = roomA
    env[2] = roomB
    step += 1

print("Final Cleaning Percentages:")
print(f"Room A: {percent_A:.0f}%")
print(f"Room B: {percent_B:.0f}%")
