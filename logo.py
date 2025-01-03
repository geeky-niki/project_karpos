from PIL import Image

# Load the uploaded image
input_path = "image/logo.png"
output_path = "image/refined_logo.png"

# Open the image
image = Image.open(input_path)

# Remove white background by converting white to transparent
image = image.convert("RGBA")
data = image.getdata()

new_data = []
for item in data:
    # Replace white or near-white pixels with transparency
    if item[:3] == (255, 255, 255):  # Pure white
        new_data.append((255, 255, 255, 0))  # Transparent
    else:
        new_data.append(item)

image.putdata(new_data)

# Increase the resolution by scaling
scale_factor = 4  # Increase the resolution
new_size = (image.width * scale_factor, image.height * scale_factor)
refined_image = image.resize(new_size, Image.Resampling.LANCZOS)  # Use LANCZOS for high-quality resampling

# Save the refined image
refined_image.save(output_path, "PNG")  # Changed to PNG because SVG is not directly supported for images
print(output_path)
