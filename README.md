COVID-19 Chart Demonstration using Python

Overview

This project visualizes the trends of COVID-19 cases across multiple countries using Python's Matplotlib library. The script plots the number of cases over time for different countries and presents them in a multi-plot format.

Features

Uses Matplotlib for data visualization.

Displays trends for multiple countries in a 3x3 grid layout.

Plots include grid lines and data markers for better readability.

Provides clear titles and date labels for each subplot.

Installation

To run this script, ensure you have Python installed along with the required dependencies.

pip install numpy matplotlib

Usage

Clone this repository or copy the script.

Run the script using:

python covid_chart.py

The chart will be displayed with multiple subplots, each representing a different country.

Code Explanation

The script initializes data arrays for dates (x) and corresponding COVID-19 cases (y).

plt.subplot(3,3,i) is used to create a 3x3 grid for different countries.

plt.plot(x, y, color, marker='o') plots the data points with markers.

plt.xticks() ensures proper date labeling.

plt.grid() enhances readability with dashed grid lines.

plt.suptitle() provides an overall title for the visualization.

Output

The script generates a grid of plots showing the COVID-19 case trends for the following countries:

Russian Federation

Greece

New Zealand

Italy

United Kingdom

Poland

France

Czechia

Contribution

Feel free to fork this repository, make improvements, and submit a pull request. Any contributions to improve data accuracy or visualization are welcome!

License

This project is licensed under the MIT License. See the LICENSE file for details.

Author

[Chathura Hasanga][https://github.com/ChathuraHasanga][chathurahasanga074@gmail.com]

![Figure_1](https://github.com/user-attachments/assets/e39178ab-c1b2-432a-a38b-81849808bd95)


