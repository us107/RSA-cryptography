# Import necessary libraries
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# Step 1: Generate RSA Keys
def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# Step 2: Encrypt a message
def encrypt_message(plain_text, public_key):
    recipient_key = RSA.import_key(public_key)
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    encrypted_message = cipher_rsa.encrypt(plain_text.encode('utf-8'))
    return base64.b64encode(encrypted_message).decode('utf-8')

# Step 3: Decrypt a message
def decrypt_message(cipher_text, private_key):
    private_key = RSA.import_key(private_key)
    cipher_rsa = PKCS1_OAEP.new(private_key)
    decrypted_message = cipher_rsa.decrypt(base64.b64decode(cipher_text))
    return decrypted_message.decode('utf-8')

# Main function to demonstrate the process
def main():
    print("--- RSA Key Generation, Encryption, and Decryption ---")

    # Generate RSA keys
    private_key, public_key = generate_keys()
    print("\nGenerated Public Key:\n", public_key.decode('utf-8'))
    print("\nGenerated Private Key:\n", private_key.decode('utf-8'))

    # Encrypt a message
    plain_text = input("\nEnter the message to encrypt: ")
    cipher_text = encrypt_message(plain_text, public_key)
    print("\nEncrypted Message (Ciphertext):\n", cipher_text)

    # Decrypt the message
    decrypted_message = decrypt_message(cipher_text, private_key)
    print("\nDecrypted Message (Plaintext):\n", decrypted_message)

if __name__ == "__main__":
    main()
