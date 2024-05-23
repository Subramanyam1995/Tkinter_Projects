for i in range(26):
    print(f"windows.bind('<{chr(65+26+6+i)}>', lambda event: print('Press {chr(65+26+6+i)}'))")