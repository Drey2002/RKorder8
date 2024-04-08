# For file manipulation
import csv

# For graphing
import pandas
import matplotlib.pyplot as plt

# Differential equation used
def differentialEquation(x, y):
    return (2 * (x * y))

# 8th order formula fucntion
def runge_kutta_8(x0, y0, h, yn):
    k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    counter = 0

    with open("Iteration_results.csv", "w", newline='') as csvFile:
        csv_writer = csv.writer(csvFile)
        csv_writer.writerow(["n", "x", "y", "k1", "k2", "k3", "k4", "k5", "k6", "k7", "k8", "k9", "k10", "k11", "k12", "k13"])

        while counter < 101:
            k1 = differentialEquation(x0, y0)
            k2 = differentialEquation(x0 + (0.0741 * h), y0 + (0.0741 * (h * k1)))

            k3 = differentialEquation(x0 + (0.1111 * h), y0 + (0.0278 * (h * (k1 + (3 * k2)))))

            k4 = differentialEquation(x0 + (0.1667 * h), y0 + (0.0417 * (h * (k1 + (3 * k3)))))

            k5 = differentialEquation(x0 + (0.417 * h), y0 + (0.0208 * (h * ((20 * k1) - (75 * k3) + (75 * k4)))))

            k6 = differentialEquation(x0 + (0.5 * h), y0 + (0.05 * (h * (k1 + (5 * k4) + (4 * k5)))))

            k7 = differentialEquation(x0 + (0.8333 * h), y0 + (0.0093 * (h * ((-25 * k1) + (125 * k4) + (-260 * k5) + (250 * k6)))))

            k8 = differentialEquation(x0 + (0.1667 * h), y0 + (h * ((0.1033 * k1) + (0.2711 * k5) + (-0.2222 * k6) + (0.0144 * k7))))

            k9 = differentialEquation(x0 + (0.6667 * h), y0 + (h * ((2 * k1) + (-8.3333 * k4) + (15.6444 * k5) + (-11.8888 * k6) + (0.7444 * k7) + (3 * k8))))

            k10 = differentialEquation(x0 + (0.3333 * h), y0 + (h * ((-0.8426 * k1) + (0.21296 * k4) + (-7.2296 * k5) + (5.7592 * k6) + (-0.3167 * k7) + (2.8333 * k8) + (-0.0833 * k9))))

            k11 = differentialEquation(x0 + h, y0 + (h * ((0.5812 * k1) + (-2.0793 * k4) + (4.3863 * k5) + (-3.6707 * k6) + (0.5202 * k7) + (0.5488 * k8) + (0.2744 * k9) + (0.4390 * k10))))

            k12 = differentialEquation(x0 + h, y0 + (h * ((0.0146 * k1) + (-0.1463 * k6) + (-0.0146 * k7) + (-0.0732 * k8) + (-0.0732 * k9) + (0.1463 * k10))))

            k13 = differentialEquation(x0 + h, y0 + (h * ((-0.4334 * k1) + (-2.0793 * k4) + (4.3863 * k5) + (-3.5244 * k6) + (0.5349 * k7) + (0.62195 * k8) + (0.2012 * k9) + (0.2927 * k10) + k12)))
        
            yn = y0 + (h * ((0.3238 * k6) + (0.2571 * k7) + (0.2571 * k8) + (0.0321 * k9) + (0.0321 * k10) + (0.0488 * k12) + (0.0488 * 13)))

            csv_writer.writerow([
                counter,
                round(x0, 5),
                round(y0, 5),
                round(k1, 5),
                round(k2, 5),
                round(k3, 5),
                round(k4, 5),
                round(k5, 5),
                round(k6, 5),
                round(k7, 5),
                round(k8, 5),
                round(k9, 5),
                round(k10, 5),
                round(k11, 5),
                round(k12, 5),
                round(k13, 5)
            ])

            x0 += h
            y0 = yn
            counter += 1

# Get user inputs
if __name__ == "__main__":
    x0 = float(input("Enter initial value for x: "))
    y0 = float(input("Enter initial value for y: "))
    h = float(input("Enter step size: "))
    yn = 0.0

    runge_kutta_8(x0, y0, h, yn)


    # Read data from the result file
    data = pandas.read_csv("Iteration_results.csv")

    # Select variables for axes
    selected_data = data.iloc[0:10]

    x_values = selected_data["x"]
    y_values = selected_data["y"]

    # yellow lines for 8th order
    plt.plot(x_values, y_values, linestyle="-", color="yellow", label="eighth order", marker="o", markerfacecolor="green")

    plt.legend()
    plt.grid(True, axis="y")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Graph of first 10 iterations of 8th order Runge Kutta")
    plt.show()
