"""Lager plugin/.claude-plugin/icon.png: hvit «Ø» (Arial Bold) sentrert på #1F3A5F, 1024×1024 PNG uten metadata."""
from PIL import Image, ImageDraw, ImageFont
S=1024; img=Image.new("RGB",(S,S),(0x1F,0x3A,0x5F)); d=ImageDraw.Draw(img)
f=ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 760)
x0,y0,x1,y1=d.textbbox((0,0),"Ø",font=f)
d.text(((S-(x1-x0))/2-x0,(S-(y1-y0))/2-y0),"Ø",font=f,fill=(255,255,255))
img.save("plugin/.claude-plugin/icon.png", format="PNG", optimize=True)
