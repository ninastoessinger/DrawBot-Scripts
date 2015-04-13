"""
ColorCombinations.py

Simple DrawBot script to show all possible combinations of color swatches for a given list of colors.
"""

# set a color space to finetune display of colors
# requires DrawBot version 3.55 and up
# use listColorSpaces() to see what's available
colorspace = "sRGB"

# define colors as r,g,b values
colorsRGB = [
    (0,0,0),
    (71,88,56),
    (159,184,173),
    (255,236,68),
    (255,185,32),
    (206,208,206),
    (232,232,230),
    (161,135,120),
    (50,26,20),
    ]
colors = [(r/255, g/255, b/255) for (r,g,b) in colorsRGB]

# dimensions of color double-swatches
swatchHeight = 40
swatchWidth  = 40

# space between color swatches
padding = 10

# end of editable parameters


spaceX = swatchWidth + padding
spaceY = swatchHeight + padding*1.025
startX = (595 - ((len(colors)+1)*spaceX + swatchWidth))/2 # center horizontally
startY = 750


newPage('A4')
colorSpace(colorspace)
translate(startX,startY)
for c1 in colors:
    r1, g1, b1 = c1
    for c2 in colors:
        translate(spaceX,0)
        if c1 != c2:
            r2, g2, b2 = c2
            stroke(None)
            fill(r1,g1,b1)
            rect(0, 0, swatchWidth/2, swatchHeight)
            fill(r2,g2,b2)
            rect(swatchWidth/2, 0, swatchWidth/2, swatchHeight)
        else:
            stroke(0)
            strokeWidth(3)
            fill(r1,g1,b1)
            rect(0, 0, swatchWidth, swatchHeight)
    translate(-(len(colors) * spaceX),-spaceY)
