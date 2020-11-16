def Compute_interest(amount, persent):
    interest = (amount/100)*persent
    total = amount+interest
    return 'Amount: {}\nInterest: {}% = {}\nTotal: {}'.format(amount,
                                                              persent,
                                                              interest,
                                                              total)

print(Compute_interest(4310,20))
