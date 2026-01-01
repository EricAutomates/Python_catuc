guests = ["Albert Einstein", "Ada Lovelace", "Nikola Tesla"]

print("\nGood news! I found a bigger dinner table.")

# Add more guests
guests.insert(0, "Leonardo da Vinci")        # beginning
guests.insert(2, "Isaac Newton")              # middle
guests.append("Galileo Galilei")               # end

for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")
