import glob
from PIL import Image

def stitch_files(files):
    
    images = [Image.open(f) for f in files]
    
    # Get the maximum width and total height.
    result_width, result_height = 0, 0
    result_width = max(i.size[0] for i in images)
    
    # Resize images to max width.
    for i,image in enumerate(images):
        ratio = float(result_width) / image.size[0]
        newsize = (int(image.size[0]*ratio), int(image.size[1]*ratio))
        image = image.resize(newsize, Image.ANTIALIAS)
        result_height += newsize[1]
        images[i] = image
    
    # Create new image with those dimensions.
    result = Image.new("RGB", (result_width, result_height))
    
    # Set offset to top
    y_offset = 0
    
    for image in images:
        # Paste image into result at current y offset.
        result.paste(image, (0, y_offset))
        # Increase y offset.
        y_offset += image.size[1]
        
    # Done!
    return result

def stitchy(imgpath=".", filename="result.png"):
    
    # Get list of images in specified directory.
    included_extenstions = ["*.jpg","*.bmp","*.png","*.gif"]
    
    files = []
    for ext in included_extenstions:
        files.extend(glob.glob("{0}\{1}".format(imgpath,ext)))
    
    # Remove result from images to combine
    result_filepath = "{0}\{1}".format(imgpath,filename)
    
    if result_filepath in files:
        files.remove(result_filepath)
    
    if len(files) == 0:
        raise IOError("No image files found in specified directory.")
    
    result = stitch_files(files)
    result.save(result_filepath)

if __name__ == "__main__":
    stitchy()
