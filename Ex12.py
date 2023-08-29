def tax_calculate(income):
    if income <= 10000:
        tax_total = 0
    elif income <= 20000:
        amount = income - 10000
        tax_total = amount * 0.1
    else:
        #for income <= 20000
        tax_total = 10000 * 0.1

        #for income > 20000
        tax_above20k = (income - 20000) * 0.2
        tax_total = tax_total + tax_above20k

    print(f"Total tax to pay is ${tax_total}")

tax_calculate(45000)

