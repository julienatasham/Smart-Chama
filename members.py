def add_member(chama_members):
    name = input("Enter member name: ")
    try:
        amount = float(input(f"Enter {name}'s contribution amount (KES): "))
    except ValueError:
        print("❌ Invalid amount. Please enter a number.")
        return

    chama_members.append({
        'name': name,
        'contribution': amount
    })
    print(f"✅ Added {name} with KES {amount} contribution.\n")
