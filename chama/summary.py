def calculate_summary(chama):
    return {
        "total_members": len(chama['members']),
        "total_transactions": len(chama['transactions']),
    }
