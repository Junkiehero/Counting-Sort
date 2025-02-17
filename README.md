# Counting Sort with RGB Colors

This project is a Python application that extracts RGB color codes from an image and sorts these colors using the **Counting Sort** algorithm. The program retrieves the RGB values of each pixel from the image, sorts them, and visualizes the sorted colors.

## Contents

- **Counting Sort** algorithm for sorting colors.
- Extracting RGB values from an image.
- Visualizing the sorted colors.

## Requirements

- Python 3.x
- Pillow (Python Imaging Library)
- Matplotlib

## Installation

### 1. Install Python and Required Libraries

To run this project, ensure you have Python installed on your system. Additionally, you need to install the required libraries by running the following command in your terminal:

pip install pillow matplotlib


### 2. Running the Code

Before running the program, make sure to specify the correct path for the image file. You need to update the image path in the following line:

image_path = 'your_image.jpg'  # Path to your image file

Once you've updated the path, run the script using the following command:

python countingSortRGB.py


The program will process the image, sort the colors, and visualize the results.



### 3. Visualization
The program will visualize the sorted colors as a bar chart. This visualization allows you to easily observe how the colors are ordered.


### 4. Code Explanation

- Counting Sort: The Counting Sort algorithm sorts the colors based on the sum of their RGB components. A counting array is created to store the occurrences of colors, and the sorted colors are extracted.
- Opening the Image and Extracting Colors: The Pillow library is used to open the image and extract the RGB values of each pixel.
- Visualization: Matplotlib is used to display the sorted colors as a bar chart.


### 5. Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork this repo.
2. Create a new branch (git checkout -b feature-xyz).
3. Make your changes and commit them (git commit -am 'Add new feature').
4. Push your changes (git push origin feature-xyz).
5. Open a Pull Request.

### 6. License
This project is licensed under the MIT License - see the LICENSE file for details.
