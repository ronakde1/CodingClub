# Unique
# Loop through possible digits for each letter in SEND, MORE, and MONEY
for s in range(1, 10):   # Since S cannot be 0
    for e in range(10):
        for n in range(10):
            for d in range(10):
                for m in range(1, 10):  # Since M cannot be 0
                    for o in range(10):
                        for r in range(10):
                            for y in range(10):
                                # Calculate the numeric values for SEND, MORE, and MONEY
                                send = s * 1000 + e * 100 + n * 10 + d
                                more = m * 1000 + o * 100 + r * 10 + e
                                money = m * 10000 + o * 1000 + n * 100 + e * 10 + y

                                # Check if SEND + MORE equals MONEY
                                if send + more == money:
                                    # Print the found solution
                                    print(f"S: {s}, E: {e}, N: {n}, D: {d}")
                                    print(f"M: {m}, O: {o}, R: {r}, E: {e}")
                                    print(f"Y: {y}")
                                    print(f"SEND: {send}")
                                    print(f"MORE: {more}")
                                    print(f"MONEY: {money}")