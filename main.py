print("Welcome to Smart-Chama, saving made easier")
print("This tool will help Kenyan women manage and optimize Chama Groups.")
print()
# Smart-Chama Basic Structure`

from chama import create_chama
# A list to store chama members
chama_members = []
def add_member():
    name = input("Enter member name: ")
    amount = float(input(f"Enter {name}'s contribution amount: "))
    chama_members.append({'name': name, 'contribution': amount})
    print(f"✅ Added {name} with contribution of KES {amount}\n")

def show_summary():
    print("\n📊 Chama Summary:")
    total = 0
    for member in chama_members:
        print(f"- {member['name']}: KES {member['contribution']}")
        total += member['contribution']
    print(f"\n💰 Total Contributions: KES {total}")

# --- Start of program ---
group = create_chama()

while True:
    print("\nOptions:")
    print("1. Add member")
    print("2. Show summary")
    print("3. Exit")
    
    choice = input("Choose an option (1-3): ")

    if choice == '1':
        add_member()
    elif choice == '2':
        show_summary()
    elif choice == '3':
        print(f"\n👋 Thanks for using Smart-Chama, {group}!")
        break
    else:
        print("❌ Invalid choice, try again.")
