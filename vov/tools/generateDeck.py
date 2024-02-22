#!/usr/bin/python

from PIL import Image
import pandas as pd

# Start by getting the decklist in a usable format
rawDeck = pd.read_csv("vov/data/decklist.csv").fillna("")
cardlist = []
for i in range(rawDeck.shape[0]):
    for j in range(rawDeck.shape[1]):
        if rawDeck.iloc[i, j] and rawDeck.iloc[i, j].split("@")[0]:
            id, amount = rawDeck.iloc[i, j].split("@")
            for k in range(int(amount)):
                cardlist.append(f"vov/img/{id.replace('.', '')}.jpg")

base = Image.open( cardlist[0] )
width, height = base.size
# 10 wide by 6 tall
totalWidth = width * 10
totalHeight = height * 6
output = Image.new(size=(totalWidth, totalHeight), mode="RGB")
for h in range(6):
    for w in range(10):
        if len(cardlist) == 0:
            break
        im = Image.open( cardlist.pop(0) )
        output.paste(im, (w*width, h*height))
output.save("vov/img/!output.jpg")