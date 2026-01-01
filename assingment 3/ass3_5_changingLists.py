#ERIC genuinly entering flow btw

guests = ["Albert Einstein", "Marie Curie", "Nikola Tesla"]

print(f"\nUnfortunately, {guests[1]} can’t make it to dinner.")

# Replace guest who can't make it
guests[1] = "Ada Lovelace"

for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")
