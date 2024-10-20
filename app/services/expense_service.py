def split_expenses(expense, users):
    if expense.split_method == 'equal':
        share = expense.amount / len(users)
        return {user.id: share for user in users}
    elif expense.split_method == 'exact':
        return expense.exact_splits
    elif expense.split_method == 'percentage':
        return {user.id: (user.percentage * expense.amount) / 100 for user in users}
