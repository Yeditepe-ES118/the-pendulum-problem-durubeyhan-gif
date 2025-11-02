import numpy as np

def find_period(L0, L1):
    g = 9.81
    
    for L in range(L0, L1 + 1):
        T = 2 * np.pi * np.sqrt(L / g)
        print(f"When L = {L:.1f} m, T = {T:.1f} s")
    
    T0 = 2 * np.pi * np.sqrt(L0 / g)
    T1 = 2 * np.pi * np.sqrt(L1 / g)
    
    return T0, T1


if __name__ == "__main__":
    L0 = 2
    L1 = 10
    T0, T1 = find_period(L0, L1)
    
    print("\nResults:")
    print(f"T0 (L0={L0} m) = {T0:.2f} s")
    print(f"T1 (L1={L1} m) = {T1:.2f} s")
    
