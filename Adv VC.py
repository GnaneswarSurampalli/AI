rooms = ["Kitchen", "Hall", "Bedroom1", "Bedroom2", "Balcony", "Storeroom"]
parts = ["Left", "Center", "Right"]

env = {}
for r in rooms:
    env[r] = {"Left":1, "Center":1, "Right":1}

step = 1
cleaned = 0
total = len(rooms) * 3
percept_seq = []

print(f"{'Step':<5}{'Room':<12}{'Part':<10}{'Percept':<12}{'Action':<10}{'Performance'}")
print("-"*60)

for room in rooms:
    for part in parts:
        percept = [env[room]["Left"], env[room]["Center"], env[room]["Right"]]
        action = "Suck"
        env[room][part] = 0
        cleaned += 1
        performance = int((cleaned / total) * 100)

        print(f"{step:<5}{room:<12}{part:<10}{str(percept):<12}{action:<10}{performance}%")
        percept_seq.append((room.lower(), part.lower(), 1))
        step += 1

print("\nFinal Status:")
for r in rooms:
    print(f"{r:<12}: [{env[r]['Left']},{env[r]['Center']},{env[r]['Right']}]")

print("\nPercept Sequence:")
for i,p in enumerate(percept_seq,1):
    print(f"{i}: {p}")
