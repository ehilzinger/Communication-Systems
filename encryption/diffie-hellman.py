import random


def generate_prime():
    # Generate a large prime number
    return 23


def generate_primitive_root(prime):
    # Find a primitive root modulo prime
    primitive_roots = []
    for i in range(2, prime):
        if all(pow(i, powers, prime) != 1 for powers in range(1, prime)):
            primitive_roots.append(i)
    return random.choice(primitive_roots)


def generate_private_key(prime):
    # Generate a private key (a random number less than prime)
    return random.randint(2, prime - 1)


def generate_public_key(prime, primitive_root, private_key):
    # Generate a public key using the private key, prime, and primitive root
    return pow(primitive_root, private_key, prime)


def generate_shared_secret(prime, public_key, private_key):
    # Generate a shared secret using the other party's public key and our private key
    return pow(public_key, private_key, prime)


if __name__ == "__main__":
    prime = generate_prime()
    primitive_root = generate_primitive_root(prime)

    # Alice's side
    alice_private_key = generate_private_key(prime)
    alice_public_key = generate_public_key(
        prime, primitive_root, alice_private_key)

    # Bob's side
    bob_private_key = generate_private_key(prime)
    bob_public_key = generate_public_key(
        prime, primitive_root, bob_private_key)

    # Exchange public keys
    shared_secret_alice = generate_shared_secret(
        prime, bob_public_key, alice_private_key)
    shared_secret_bob = generate_shared_secret(
        prime, alice_public_key, bob_private_key)

    # Both parties should have the same shared secret
    print("Shared secret calculated by Alice:", shared_secret_alice)
    print("Shared secret calculated by Bob:", shared_secret_bob)
