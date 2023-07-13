import pandas as pd
import re

class CardCodesSpreadsheet:
    def __init__(self, spreadsheetFile, keywordsFile):
        self.keywords = _initializeDataframe(keywordsFile)
        self.spreadsheet = _findAndReplaceKeywords(
            _initializeDataframe(spreadsheetFile), self.keywords)
        
    def convertCardCodesToMarkdown(self):
        # Search through each row of the card data
        md = ""
        returnMarkdown = ""
        with open(file="www\\tools\markdownTemplate.md") as f:
            md = f.read()
        for i in range(len(self.spreadsheet.index)):
            cardMarkdown = md
            cardMarkdown = cardMarkdown.replace("{{Name}}", self.spreadsheet.loc[i, "Name"])
            cardMarkdown = cardMarkdown.replace("{{Class}}", self.spreadsheet.loc[i, "Class"])
            cardMarkdown = cardMarkdown.replace("{{Type}}", self.spreadsheet.loc[i, "Type"])
            cardMarkdown = cardMarkdown.replace("{{Attribute}}", self.spreadsheet.loc[i, "Attribute"])
            cardMarkdown = cardMarkdown.replace("{{Code}}", self.spreadsheet.loc[i, "Code"])
            
            text = self.spreadsheet.loc[i, "Text"].replace("\r\n", "  \r\n")
            cardMarkdown = cardMarkdown.replace("{{Text}}", text)
            
            rank = ""
            if self.spreadsheet.loc[i, "Rank"]:
                try:
                    rank = f' - Rank: {int(self.spreadsheet.loc[i, "Rank"])}\n'
                except:
                    # Doesn't have to be an int
                    rank = f' - Rank: {self.spreadsheet.loc[i, "Rank"]}\n'
            cardMarkdown = cardMarkdown.replace("{{Rank}}", rank)
            
            cost = ""
            if self.spreadsheet.loc[i, "Cost"]:
                try:
                    cost = f' - Cost: {int(self.spreadsheet.loc[i, "Cost"])}\n'
                except:
                    # Doesn't have to be an int
                    cost = f' - Cost: {self.spreadsheet.loc[i, "Cost"]}\n'
            cardMarkdown = cardMarkdown.replace("{{Cost}}", cost)
            
            power = ""
            if self.spreadsheet.loc[i, "Power"]:
                try:
                    power = f' - Power: {int(self.spreadsheet.loc[i, "Power"])}\n'
                except:
                    # Doesn't have to be an int
                    power = f' - Power: {self.spreadsheet.loc[i, "Power"]}\n'
            cardMarkdown = cardMarkdown.replace("{{Power}}", power)
            
            life = ""
            if self.spreadsheet.loc[i, "Life"]:
                try:
                    life = f' - Life: {int(self.spreadsheet.loc[i, "Life"])}\n'
                except:
                    # Doesn't have to be an int
                    life = f' - Life: {self.spreadsheet.loc[i, "Life"]}\n'
            cardMarkdown = cardMarkdown.replace("{{Life}}", life)
            
            hand = ""
            if self.spreadsheet.loc[i, "Hand"]:
                try:
                    hand = f' - Hand: {int(self.spreadsheet.loc[i, "Hand"])}\n'
                except:
                    # Doesn't have to be an int
                    hand = f' - Hand: {self.spreadsheet.loc[i, "Hand"]}\n'
            cardMarkdown = cardMarkdown.replace("{{Hand}}", hand)
            
            returnMarkdown += f"{cardMarkdown}\r\n"
        # Make it human readable
        returnMarkdown = returnMarkdown.replace("{l}", "Life")
        returnMarkdown = returnMarkdown.replace("{h}", "Hand")
        returnMarkdown = returnMarkdown.replace("{c}", "Cost")
        returnMarkdown = returnMarkdown.replace("{p}", "Power")
        return returnMarkdown

    def convertCardCodesToCardCreatorCSV(self):
        return


def _initializeDataframe(file):
    return pd.read_csv(file).fillna("")

def _findAndReplaceKeywords(spreadsheetDataframe, keywordsDataframe):
    # Search through each row of the card data
    for i in range(len(spreadsheetDataframe.index)):
        cardText = spreadsheetDataframe.loc[i, "Text"]
        if cardText:
            # Search for any {{keywords}}
            keywordSearch = re.compile("{{.*}}")
            keywords = keywordSearch.findall(cardText)
            if keywords:
                # If there are 1 or more keywords
                for keyword in keywords:
                    k = keyword
                    x = ""
                    y = ""
                    z = ""
                    # Determine if it is a dynamic keyword
                    if len(k.split(",")) > 1:
                        # Dyanmic keyword, this needs a substitution
                        kw = k[2:-2].split(",")
                        # Use a loop to avoid disgusting if statements
                        for j in range(len(kw)):
                            if j == 1:
                                x = kw[j]
                                kw[j] = "x"
                            if j == 2:
                                y = kw[j]
                                kw[j] = "y"
                            if j == 3:
                                z = kw[j]
                                kw[j] = "z"
                        k = "{{" + ",".join(kw) + "}}"
                    keywordCell = keywordsDataframe.loc[keywordsDataframe["Keyword"] == k]
                    keywordReplacement = keywordCell["Replacement"].item()
                    # Replace any dynamic elements
                    keywordReplacement = keywordReplacement.replace("{{x}}", x)
                    keywordReplacement = keywordReplacement.replace("{{y}}", y)
                    keywordReplacement = keywordReplacement.replace("{{z}}", z)
                    cardText = cardText.replace(keyword, keywordReplacement)
        # Update the original text in the spreadsheet
        spreadsheetDataframe.loc[i, "Text"] = cardText
    return spreadsheetDataframe

ss = CardCodesSpreadsheet("www\data\cardcodes.csv", "www\data\keywords.csv")
with open(file="www\data\cards.md", mode="w") as f:
    f.write(ss.convertCardCodesToMarkdown())