print("\n".join([str(["| ".join([str(a+b+c).rjust(2, '0') for a in range(1, 7)]) for b in range(1, 7)]) for c in range(1, 7)]))
