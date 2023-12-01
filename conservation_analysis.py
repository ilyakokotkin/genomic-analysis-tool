def analyze_conservation(align1, align2):
    conserved = sum(c1 == c2 for c1, c2 in zip(align1, align2))
    total = len(align1)
    conservation_rate = conserved / total
    return conservation_rate
