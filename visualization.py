import matplotlib.pyplot as plt

def plot_alignment(align1, align2):
    plt.figure(figsize=(10, 5))
    plt.plot(list(align1), label='Sequence 1')
    plt.plot(list(align2), label='Sequence 2')
    plt.legend()
    plt.show()
