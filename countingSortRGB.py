from PIL import Image
import matplotlib.pyplot as plt

def counting_sort_colors(arr):
    # We will sort the colors based on their RGB values
    min_val = min(arr)
    max_val = max(arr)
    
    # Create the counting array
    count = [0] * (max_val - min_val + 1)
    
    # Count the occurrences of each color
    for color in arr:
        count[color - min_val] += 1
    
    # Create the sorted list
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i + min_val] * count[i])
    
    return sorted_arr

def get_image_colors(image_path):
    try:
        # Let's open the image
        img = Image.open(image_path)
        
        # Open the image in RGB mode
        img = img.convert('RGB')
        
        # Get all the colors in the image
        colors = list(img.getdata())
        
        return colors
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def show_sorted_colors(sorted_colors):
    # Let's visualize the sorted colors
    plt.figure(figsize=(8, 2))
    plt.imshow([sorted_colors], aspect='auto')
    plt.axis('off')
    plt.show()

# Enter the image path
image_path = 'CountingSort.png'  # Görsel dosyanızın yolu

# Get the colors from the image
colors = get_image_colors(image_path)

if colors:
    # Get the sum of the RGB components
    color_values = [sum(color) for color in colors]

    # Sort the colors
    sorted_color_values = counting_sort_colors(color_values)

    # Get the corresponding RGB values for the sorted colors
    sorted_colors = [colors[color_values.index(val)] for val in sorted_color_values]

    # Visualize the sorted colors
    show_sorted_colors(sorted_colors)
else:
    print("The image could not be opened or another error occurred.")
