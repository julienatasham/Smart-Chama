def show_summary(chama_members):
    print("\n📊 Chama Summary:")
    total = 0

    if not chama_members:
        print("No members added yet.")
        return

    for member in chama_members:
        print(f"- {member['name']}: KES {member['contribution']}")
        total += member['contribution']

    print(f"\n💰 Total Contributions: KES {total}")
