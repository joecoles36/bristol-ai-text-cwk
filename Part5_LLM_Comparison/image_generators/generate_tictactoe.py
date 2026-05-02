import matplotlib.pyplot as plt

sizes = {
    'small': 80,
    'medium': 150,
    'large': 250
}

def draw_number(number, colour, size, bg, filename):
    fig, ax = plt.subplots(figsize=(4,4))

    fig.patch.set_facecolor(bg)
    ax.set_facecolor(bg)

    ax.text(
        0.5, 0.5, str(number),
        fontsize=sizes[size],
        color=colour,
        ha='center', va='center',
        fontweight='bold'
    )

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    fig.savefig(filename, bbox_inches='tight', pad_inches=0)
    plt.close(fig)


# exact test set matching previous tests
test_cases = [
    (1173, 'orange', 'small', 'lightgrey'),
    (5567, 'pink', 'large', 'black'),
    (8582, 'yellow', 'small', 'darkblue'),
    (2, 'brown', 'medium', 'lightgrey'),
    (49, 'brown', 'small', 'darkblue'),
    (6, 'blue', 'medium', 'lightgrey'),
    (307, 'brown', 'medium', 'lightgrey'),
    (30, 'blue', 'large', 'black')
]

for i, (num, col, size, bg) in enumerate(test_cases):
    draw_number(num, col, size, bg, f"num_{i}.png")

print("Generated number images")
