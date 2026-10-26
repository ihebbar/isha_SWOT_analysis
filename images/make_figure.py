import matplotlib.pyplot as plt

features = ["Login system", "Admin page to list sign-ups", "Form handling", "Database layer", "CSRF protection"]
frameworks = ["Django", "Flask", "FastAPI"]
# True = ships with the framework; False = add an extension/library yourself
built_in = [
    [True, False, False],
    [True, False, False],
    [True, False, False],
    [True, False, False],
    [True, False, False],
]

fig, ax = plt.subplots(figsize=(6, 3))
ax.set_xlim(0, 3); ax.set_ylim(0, len(features))
for r, row in enumerate(built_in):
    for c, ok in enumerate(row):
        ax.add_patch(plt.Rectangle((c, len(features) - 1 - r), 1, 1,
                                   color="#8fd19e" if ok else "#f3c1c1", ec="white", lw=2))
        ax.text(c + .5, len(features) - 1 - r + .5, "built in" if ok else "add-on",
                ha="center", va="center", fontsize=9)
ax.set_xticks([.5, 1.5, 2.5]); ax.set_xticklabels(frameworks)
ax.set_yticks([i + .5 for i in range(len(features))]); ax.set_yticklabels(features[::-1])
ax.xaxis.tick_top(); ax.tick_params(length=0)
for s in ax.spines.values(): s.set_visible(False)
plt.tight_layout()
plt.savefig("images/built-in-features.png", dpi=200)
