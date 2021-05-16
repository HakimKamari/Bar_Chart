import string
import matplotlib.pyplot as plt
import mplcursors

# fig, ax = plt.subplots()
# ax.bar(range(9), range(1, 10), align="center")
# labels = string.ascii_uppercase[:9]
# ax.set(xticks=range(9), xticklabels=labels, title="Hover over a bar")

# # With HoverMode.Transient, the annotation is removed as soon as the mouse
# # leaves the artist.  Alternatively, one can use HoverMode.Persistent (or True)
# # which keeps the annotation until another artist gets selected.
# cursor = mplcursors.cursor(hover=mplcursors.HoverMode.Transient)
# @cursor.connect("add")
# def on_add(sel):
#     x, y, width, height = sel.artist[sel.target.index].get_bbox().bounds
#     sel.annotation.set(text=f"{x+width/2}: {height}",
#                        position=(0, 20), anncoords="offset points")
#     sel.annotation.xy = (x + width / 2, y + height)

# plt.show()

# annotations can be dragged -----------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
import mplcursors

fig, ax = plt.subplots()
ax.set_title("Click somewhere on a line.\nRight-click to deselect.\n"
             "Annotations can be dragged.")

mplcursors.cursor() # or just mplcursors.cursor()
lines = ax.plot(range(3), range(3), "o")
labels = ["a", "b", "c"]
cursor = mplcursors.cursor()
cursor.connect(
"add", lambda sel: sel.annotation.set_text(labels[sel.target.index]))
plt.show()

