def main():
    print("Welcome to the Quantum-Safe Algorithm Selector!")
    print("This tool will help you select the appropriate algorithm based on your needs.\n")

    # Step 1: Determine the purpose
    purpose = input("What do you need the algorithm for? (Type '1' for Encryption / Key Exchange, '2' for Digital Signatures): ").strip()

    if purpose == '1':
        print("\n### Encryption / Key Exchange ###")
        print("For key exchange and encryption, lattice-based key encapsulation mechanisms (ML-KEM) are recommended.\n")
        print("Recommended Options:")
        print("1. **Kyber**: Efficient, lattice-based, selected for standardization by NIST.")
        print("2. **NTRU**: Lattice-based and well-established, suitable for various applications.")
        print("3. **FrodoKEM**: Based on the Learning With Errors problem, providing a different security assumption.")
        print("4. **Saber**: Based on the Module-Learning With Rounding (MLWR) problem, good for key encapsulation.")
        print("5. **NTRUEncrypt**: Classic lattice-based encryption scheme, robust against quantum attacks.")
        
    elif purpose == '2':
        print("\n### Digital Signatures ###")
        print("For digital signatures, choose based on the structure and security requirements.\n")
        
        # Step 2: Determine preference between ML-DSA and SLH-DSA
        dsa_type = input("Do you prefer lattice-based (Type '1') or hash-based signatures (Type '2')? ").strip()

        if dsa_type == '1':
            print("\n### Lattice-Based Digital Signatures (ML-DSA) ###")
            print("Recommended Options:")
            print("1. **CRYSTALS-Dilithium**: Efficient, lattice-based, and selected for standardization by NIST.")
            print("2. **Falcon**: Another lattice-based option, known for its compact signatures and strong security.")
            print("3. **Rainbow**: Multivariate quadratic signature scheme, still under evaluation by NIST.")

        elif dsa_type == '2':
            # Step 3: Select between stateful or stateless hash-based signatures
            state_choice = input("Do you prefer a stateless (Type '1') or stateful (Type '2') signature scheme? ").strip()

            if state_choice == '1':
                print("\n### Stateless Hash-Based Digital Signatures (SLH-DSA) ###")
                print("Recommended Option:")
                print("1. **SPHINCS+**: Stateless, hash-based, selected for standardization, offering robust security for high-value applications.")
            elif state_choice == '2':
                print("\n### Stateful Hash-Based Digital Signatures ###")
                print("Recommended Options:")
                print("1. **XMSS (eXtended Merkle Signature Scheme)**: Stateful, hash-based, standardized in RFC 8391, suitable for certain use cases.")
                print("2. **LMS (Leighton-Micali Signature Scheme)**: Another stateful option, standardized and reliable for specific applications.")
            else:
                print("Invalid choice. Please restart the tool and select a valid option.")
        else:
            print("Invalid choice. Please restart the tool and select a valid option.")
    else:
        print("Invalid choice. Please restart the tool and select a valid option.")
    
    print("\nThank you for using the Quantum-Safe Algorithm Selector. Stay secure in the quantum era!")

# Run the tool
if __name__ == "__main__":
    main()
