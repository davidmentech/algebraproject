import number_theory_functions

class RSA():
    def __init__(self, public_key, private_key = None):
        self.public_key = public_key
        self.private_key = private_key

    @staticmethod
    def generate(digits = 10):
        """
        Creates an RSA encryption system object

        Parameters
        ----------
        digits : The number of digits N should have

        Returns
        -------
        RSA: The RSA system containing:
        * The public key (N,e)
        * The private key (N,d)
        """
        digit1=digits//2
        first_prime=number_theory_functions.generate_prime(digit1)
        while True:
            second_prime=number_theory_functions.generate_prime(digits-digit1)
            if second_prime!=first_prime:
                break
       
        N=first_prime*second_prime
        phiN=(first_prime-1)*(second_prime-1)    
        numofdigits=len(str(phiN))     
        while True:
            e=number_theory_functions.generate_prime(numofdigits//2)
            if(e!=second_prime and e!=first_prime):
                break
       
        d=number_theory_functions.modular_inverse(e,phiN) 
        key_public = (N, e)     
        key_private = (N, d)
        return RSA(key_public,key_private)
        

    def encrypt(self, m):
        """
        Encrypts the plaintext m using the RSA system

        Parameters
        ----------
        m : The plaintext to encrypt

        Returns
        -------
        c : The encrypted ciphertext
        """
        return number_theory_functions.modular_exponent(m,self.public_key[1],self.public_key[0])
        
    def decrypt(self, c):
        """
        Decrypts the ciphertext c using the RSA system

        Parameters
        ----------
        c : The ciphertext to decrypt

        Returns
        -------
        m : The decrypted plaintext
       """
        return number_theory_functions.modular_exponent(c,self.private_key[1],self.private_key[0])