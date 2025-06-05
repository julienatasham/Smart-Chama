def add_member(chama, member_name):
    if member_name not in chama['members']:
        chama['members'].append(member_name)
