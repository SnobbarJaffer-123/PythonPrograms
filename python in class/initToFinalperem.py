def initial_permutation(plaintext):
   
    ip_table = [ 2,3,1,4,0,5]
    
    # Perform initial permutation
    permuted_text = ['']*5
    for index in range(5):
        permuted_text[index]=plaintext[ip_table[index] ]
    return permuted_text

def final_permutation(plaintext):
   
    fp_table = [ 4,2,0,3,1,5]
    
    # Perform initial permutation
    permuted_text = ['']*5
    for index in range(5):
        permuted_text[index]=plaintext[fp_table[index]]
    return permuted_text
   

plaintext = ['a','b','c','d','e','f']
permuted_plaintext = initial_permutation(plaintext)
print("Permuted plaintext :", permuted_plaintext)
permuted_plaintext = final_permutation(plaintext)
print("Permuted plaintext :", permuted_plaintext)


"""def print_text(pt,ip):
    ct=['']
    for i in ip:
        ct.append(pt[i])
    return ct    
pt=['a','b','c','d','e','f']
ip=[5,3,2,0,1,4]
ct=print_text(pt,ip)
print(ct)
fp=[3,2,4,5,1,0]
ct=print_text(pt,ip)
print(ct)"""















