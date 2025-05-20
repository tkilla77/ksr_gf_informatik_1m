def binary_to_decimal(b):
    """Wandelt Binärzahl b in Dezimalzahl um."""
    d = 0
    for digit in b:
        d = d*2
        d = d + int(digit)
    return d

def decimal_to_binary(d):
    """Wandelt Dezimalzahl mit dem Restwertalgorithmus in Binärzahl um."""
    b = ""
    while d > 0:
        r = d % 2
        d = d // 2
        b = str(r) + b
    return b

def fill_zeros(b, digits):
    while len(b) < digits:
        b = "0" + b
    return b

def binary_add(a,b):
    """Addiert zwei Binärzahlen beliebiger Länge."""
    n = max(len(a), len(b))
    a = fill_zeros(a, n)
    b = fill_zeros(b, n)
    
    out = ""
    carry = 0
    index = n - 1
    while index >= 0:
        digit_a = int(a[index])
        digit_b = int(b[index])
        sum = digit_a + digit_b + carry
        if sum == 0:
            out = "0" + out
            carry = 0
        elif sum == 1:
            out = "1" + out
            carry = 0
        elif sum == 2:
            out = "0" + out
            carry = 1
        elif sum == 1:
            out = "1" + out
            carry = 1
        index = index - 1
    if carry != 0:
        out = str(carry) + out
    return out

def invert(b):
    # Erstellt einen neuen String, wobei 0en und 1en vertauscht sind.
    result = ""
    for digit in b:
        if digit == "0":
            result = result + "1"
        else:
            result = result + "0"
    return result
 
def zweierkomplement(b, stellen=8):
    # 1) Auffüllen auf stellen bits
    b = fill_zeros(b, stellen)
    # 2) Invertieren (1->0, 0->1)
    b = invert(b)
    # 3) Addiere 1
    return binary_add(b, "1")
 
def binary_subtraction(a, b, stellen=8):
    complement = zweierkomplement(b, stellen)
    result = binary_add(a, complement)
    if len(result) > stellen:
        result = result[1:]  # Vorderstes Bit auslassen
    return result

a_dec = 42
b_dec = 19
a_bin = decimal_to_binary(a_dec)
b_bin = decimal_to_binary(b_dec)
difference_bin = binary_subtraction(a_bin, b_bin, 8)
difference_dec = binary_to_decimal(difference_bin)
print(f"{a_dec} - {b_dec} = {a_bin} - {b_bin} = {difference_bin} = {difference_dec}")