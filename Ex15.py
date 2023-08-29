def exponent(base, exp):
    print(f"base = {base}")
    print(f"exponent = {exp}")

    if base > 0:
        pow_ = pow(base, exp)
        asterisk_ = "*"; display = ( f"{base}{asterisk_}" *(exp) )

        print(f"{base} raises to the power of {exp}: "
              f"{pow_} i.e. ({display} = {pow_})")
    else:
        return base == 0

base = 5
exponent_ = 4
exponent(base, exponent_)

