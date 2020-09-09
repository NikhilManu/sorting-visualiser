import random
import algo
import matplotlib.pyplot as pyplot
import matplotlib.animation as animation


def generate_array():
    arr = []
    for i in range(101):
        arr.append(random.randint(1,100))
    return arr


i = 0


def update_fig(arr, bars, iter):
    for bar, val in zip(bars, arr):
        bar.set_height(val)
    iter += 1
    text.set_text("No of Operations: {}".format(iter))



arr = generate_array()
var = input("Merge Sort --> M or m \nQuick Sort --> q or Q \nInsertion Sort --> i or I\n")
if var == 'm' or var == 'M':
    Title = 'Merge Sort'
    generator = algo.merge_sort(arr, 0, 100)
elif var == 'q' or var == 'Q':
    Title = 'Quick Sort'
    generator = algo.quicksort(arr, 0, 100)
elif var == 'i' or var == 'I':
    Title = 'Insertion Sort'
    generator = algo.insertionsort(arr)
else:
    exit("Invalid Character")
fig, ax = pyplot.subplots()
ax.set_title(Title)

bar_graph = ax.bar(range(len(arr)), arr, align='edge')
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

text = ax.text(0, 1, "", transform = ax.transAxes)

anim = animation.FuncAnimation(fig, func=update_fig, fargs=(bar_graph, i), frames=generator, interval=1, repeat=False)
pyplot.show()











