def stitchy(filename="result", extension="png", imgpath="."):
    import glob
    import os
    from PIL import Image
    
    result_filename = "{0}.{1}".format(filename,extension)
    
    # Remove the result image if it exists.
    try:
        os.remove(result_filename)
    except OSError:
        pass
    
    # Get list of images in specified directory.
    included_extenstions = ["*.jpg","*.bmp","*.png","*.gif"]
    
    file_names = []
    for ext in included_extenstions:
        file_names.extend(glob.glob("{0}\{1}".format(imgpath,ext)))
    
    if len(file_names) == 0:
        raise IOError("No image files found in specified directory.")
    
    images = [Image.open(f) for f in file_names]
    
    # Get the maximum width and total height.
    result_width, result_height = 0, 0
    for image in images:
        width, height = image.size
        result_width = max(result_width, width)
        result_height += height
    
    # Create new image with those dimensions.
    result = Image.new("RGB", (result_width, result_height))
    
    # Set offset to top
    y_offset = 0
    
    for image in images:
        # Resize image to max width.
        image = image.resize((result_width, image.size[1]), Image.NEAREST)
        # Paste image into result at current y offset.
        result.paste(image, (0, y_offset))
        # Increase y offset.
        y_offset += image.size[1]
        
    # Done!
    result.save(result_filename)

if __name__ == "__main__":
    stitchy()
