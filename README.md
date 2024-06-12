# Matplotlib Visualization Project

## Overview

This project demonstrates how to use Matplotlib, a powerful plotting library in Python, to create various types of data visualizations. Matplotlib is widely used for generating plots, histograms, bar charts, scatter plots, and more.

## Features

- Line plots
- Bar charts
- Histograms
- Scatter plots
- Pie charts
- Customizing plots with titles, labels, and legends
- Saving plots to files

## Prerequisites

Before you begin, ensure you have the following installed on your local machine:

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/PhoniciaAnne/matplotlib-visualization-project.git
    cd matplotlib-visualization-project
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

You can run the example scripts to generate various plots. Each script demonstrates different features of Matplotlib.

### Example 1: Line Plot

```python
import matplotlib.pyplot as plt
  
# Data
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 17, 20]

# Create a line plot
plt.plot(x, y, marker='o')

# Add title and labels
plt.title('Line Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show plot
plt.show()
```
## Example 2: Bar Chart
```python
import matplotlib.pyplot as plt

# Data
categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]

# Create a bar chart
plt.bar(categories, values, color='skyblue')

# Add title and labels
plt.title('Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('Values')

# Show plot
plt.show()
```
## Example 3: Histogram
```python
import matplotlib.pyplot as plt
import numpy as np

# Data
data = np.random.randn(1000)

# Create a histogram
plt.hist(data, bins=30, color='purple', alpha=0.7)

# Add title and labels
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Show plot
plt.show()
```
## Example 4 :Scatter Plot
```python
import matplotlib.pyplot as plt

# Data
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]

# Create a scatter plot
plt.scatter(x, y, color='red', marker='x')

# Add title and labels
plt.title('Scatter Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show plot
plt.show()
```
## Example 5 : Pie chart
```python
import matplotlib.pyplot as plt

# Data
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice

# Create a pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

# Add title
plt.title('Pie Chart Example')

# Show plot
plt.show()
```
## Saving Plot
```python
plt.plot(x, y)
plt.title('Line Plot Example')
plt.savefig('line_plot.png')
```
## Contributing
** Contributions are welcome! Please fork the repository and submit a pull request.**

