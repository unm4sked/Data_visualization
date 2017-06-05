import matplotlib.pyplot as plt

x_val = list(range(1, 1001))
y_val = [x**2 for x in x_val]

plt.scatter(x_val, y_val, c=(0, 0, 0.8), edgecolor='none', s=40)

plt.title("Kwadraty liczb", fontsize=24)
plt.xlabel("Wartosc: ", fontsize=14)
plt.ylabel("Kwadrat wartosci: ", fontsize=14)
#plt.tick_params(axis='both', whitch='major', labelsize=14)

plt.axis([0, 1100, 0, 1100000])

plt.show()
