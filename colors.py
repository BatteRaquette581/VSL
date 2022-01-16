def rgbtohex(rgb: tuple):
  if rgb[0] > 255 or rgb[1] > 255 or rgb[2] > 255 or rgb[0] < 0 or rgb[1] < 0 or rgb[2] < 0:
    print("Warning, you cannot put more than 255 or less than 0!")
    return "Error! Look in the console."
  return "#%02x%02x%02x" % rgb