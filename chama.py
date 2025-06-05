def add_member(name, amount, chama_members):
    if not name or amount <= 0:
        return
    chama_members.append({'name': name, 'contribution': amount})

