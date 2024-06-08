"""plainText="abcdef"
for i in plainText:
    print(plainText.index(i),i)
 
p="edabfc"  
print("\n")
for i in p:
    print(plainText.index(i) ,i)  
print("\n")    

"""
def initial_permutation(plaintext):
    # Initial Permutation Table (1-based index)
    ip_table = [ 2,3,1,4,,5]
    
    # Convert plaintext to binary string (assuming ASCII encoding)
    plaintext_bin = ''.join(format(ord(char), '08b') for char in plaintext)
    
    # Perform initial permutation
    permuted_text = []
    for index in ip_table:
        permuted_text.append(plaintext_bin[index - 1])  # -1 to convert to 0-based index
    
    # Join the list into a single string
    permuted_text = ''.join(permuted_text)
    
    return permuted_text

# Example usage
plaintext = ['a','b','c','d','e','f']
permuted_plaintext = initial_permutation(plaintext)
print("Permuted plaintext (binary):", permuted_plaintext)
