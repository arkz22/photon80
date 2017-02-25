import numpy as np

'''For information on multiplying two polynomial in the Rijndael Field:
http://stackoverflow.com/questions/13202758/multiplying-two-polynomials'''


irreducible_poly = '100010'
degree_poly = len(irreducible_poly)-1

def multiply(a,b):
    # Convert to polymial or binary
    a_poly = bin(a)[2:]
    b_poly = bin(b)[2:]

    # Make sure that the highest degree is the one that been multiply
    if len(b_poly) > len(a_poly):
        a,b = b,a

    # Find the coefficient of x^n for polynomial b that is equal to one
    deg_b = len(b_poly)-1

    # Initialize the answer
    product = 0
    bitshift_left = deg_b
    for i in b_poly:
        if i == str(1):
            a_temp = a << bitshift_left
            product ^= a_temp
        bitshift_left -= 1

    return(product)

def modulo_reduction(a,irreducible_poly):

    # Photon irr poly = x^4 +x+1 = 10011
    degree_irreducible_poly = 0

    # Degree of input poly
    a_poly = bin(a)[2:]
    degree_a = len(a_poly)-1

    #Check for whether the input polynomial is inform of equation or binary
    if type(irreducible_poly) == str:
        degree_irreducible_poly = len(irreducible_poly)-1
        poly_decimal = int(irreducible_poly,2)
    elif type(irreducible_poly) == int:
        degree_irreducible_poly = len(bin(irreducible_poly)[2:])-1

    # Cases with the same degree drop the most left bit
    list_poly = list(irreducible_poly)
    list_poly[0] = '0'
    same_degree_output = str("".join(list_poly))


    # Low degree output
    degree_selected = degree_a - degree_irreducible_poly + 1
    print(degree_selected)
    low_degree_output = int(a_poly[degree_selected:],2)

    # High degree output
    high_degree_output = 0
    bitshift_left = 0
    same_degree_output_decimal = int(same_degree_output,2)
    for i in range(degree_selected,0,-1):
        high_degree_temp = same_degree_output_decimal << bitshift_left
        print(bin(high_degree_temp))
        bitshift_left += 1
        high_degree_output ^= high_degree_temp

    return high_degree_output ^ low_degree_output


print(modulo_reduction(252,irreducible_poly))
