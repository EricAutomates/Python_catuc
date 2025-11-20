guests = ["Albert", "Maya", "Eric"]

for person in guests:
    print(f"Hi {person}, you're invited to dinner!")

for person in guests:
    print(f"Hi {person}, you're invited to dinner!")

# One guest cannot make it
print(f"\nUnfortunately, {guests[1]} can't make it.\n")

# Replace the unavailable guest
guests[1] = "Epstein"

# New invitations
for person in guests:
    print(f"Hi {person}, you're still invited to dinner!")
