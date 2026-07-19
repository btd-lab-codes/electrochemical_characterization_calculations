# Hsu mansfeld
# Obtain the values of:
    # Rct ==> Charge transfer resistance
    # Y_0 ==> CPE
    # Y_0 ==> CPE deg of freedom

def hsu_mansfeld(Y_0, R_ct, alpha):
    return (Y_0 * R_ct)**(1 / alpha) / R_ct