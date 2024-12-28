Ranges = [[1,10], [21,22], [30, 36], [41, 48], [52,53], [90, 97], [100, 108]]
Style_names = [
    "bold", "dim", "italics", "underline", 
]

for r in Ranges:
    for i in range(r[0], r[1]):
        print(f"\033[{i}m"+ "\\"+f"033[{i}m" + "\033[0m")

print(f"\033[{0}m"+ "\\"+f"033[{0}m"+"--> RESEST")