from PIL import Image, ImageDraw, ImageFont
import textwrap

txt = """
Debut and early career (2014–2021)
Rahul made his Test debut in the 2014 Boxing Day Test at the Melbourne Cricket Ground.
He replaced Rohit Sharma and was presented with his Test cap by MS Dhoni.
He managed to score only 3 and 1 on his debut.
In the next test at Sydney where he opened the innings for the first time,
and made his maiden international century, scoring 110 runs.
KL Rahul, a right-handed batsman and wicketkeeper for the Indian cricket team,
has faced controversies in the past.
He was the first Indian and the sixth overall cricketer to score 7 consecutive Test fifties.
He also became the first Indian and 10th overall cricketer to be dismissed
by a hit-wicket in T20 internationals.
Rahul has also faced criticism for his social media posts and comments on sexist topics.
He has a net worth of approximately INR 90 crores and owns luxurious apartments
in Bangalore and Goa.
"""

# Image size
img = Image.new("RGB", (1000, 800), (255, 255, 255))
draw = ImageDraw.Draw(img)

# Handwriting font
font = ImageFont.truetype("HomemadeApple-Regular.ttf", 32)

# Text wrapping
lines = textwrap.wrap(txt, width=40)

y = 50
for line in lines:
    draw.text((50, y), line, fill=(0, 0, 138), font=font)
    y += 40

img.save("demo.png")

print("Handwritten assignment created!")