def add_member(name, amount, chama_members):
    """
    Adds a member dictionary to chama_members list.
    """
    if not name or amount <= 0:
        return False
    chama_members.append({'name': name, 'contribution': amount})
    return True


