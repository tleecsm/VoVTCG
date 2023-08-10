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
            
            text = self.spreadsheet.loc[i, "Text"].replace("\n", "  \n")
            cardMarkdown = cardMarkdown.replace("{{Text}}", text)
            
            rank = ""
            if self.spreadsheet.loc[i, "Rank"]:
                    rank = f' - Rank: { str(self.spreadsheet.loc[i, "Rank"]).replace(".0", "") }\n'
            cardMarkdown = cardMarkdown.replace("{{Rank}}", rank)
            
            cost = ""
            if self.spreadsheet.loc[i, "Cost"]:
                    cost = f' - Cost: { str(self.spreadsheet.loc[i, "Cost"]).replace(".0", "") }\n'
            cardMarkdown = cardMarkdown.replace("{{Cost}}", cost)
            
            power = ""
            if self.spreadsheet.loc[i, "Power"]:
                    power = f' - Power: { str(self.spreadsheet.loc[i, "Power"]).replace(".0", "") }\n'
            cardMarkdown = cardMarkdown.replace("{{Power}}", power)
            
            life = ""
            if self.spreadsheet.loc[i, "Life"]:
                    life = f' - Life: { str(self.spreadsheet.loc[i, "Life"]).replace(".0", "") }\n'
            cardMarkdown = cardMarkdown.replace("{{Life}}", life)
            
            hand = ""
            if self.spreadsheet.loc[i, "Hand"]:
                handSubString = str(self.spreadsheet.loc[i, "Hand"]).replace(".0", "")
                if self.spreadsheet.loc[i, "Hand"] >= 0:
                    handSubString = f'+{handSubString}'
                hand = f' - Hand: { handSubString }\n'
            cardMarkdown = cardMarkdown.replace("{{Hand}}", hand)
            
            returnMarkdown += f"{cardMarkdown}\r\n"
        # Make it human readable
        returnMarkdown = returnMarkdown.replace("{l}", "Life")
        returnMarkdown = returnMarkdown.replace("{h}", "Hand")
        returnMarkdown = returnMarkdown.replace("{c}", "Cost")
        returnMarkdown = returnMarkdown.replace("{p}", "Power")
        return returnMarkdown

    def convertCardCodesToCardCreatorCSV(self):
        # Create the columns we need for the new dataframe
        headers = {
            "TypeOverlay": [],
            "AttributeOverlay": [],
            "Art": [],
            "Text": [],
            "Name": [],
            "Id": [],
            "Rank": [],
            "Life": [],
            "Power": [],
            "Attribute": [],
            "Type": [],
            "Hand": [],
            "Cost": [],
        }
        returnSpreadsheet = pd.DataFrame(headers)
        
        for i in range(len(self.spreadsheet.index)):
            handSubstring = str(self.spreadsheet.loc[i, "Hand"]).replace('.0', "")
            if self.spreadsheet.loc[i, "Hand"] and self.spreadsheet.loc[i, "Hand"] >= 0:
                    handSubstring = f'+{handSubstring}'
            data = {
            "OverlayType": f'%PROJECT%/{self.spreadsheet.loc[i, "Attribute"]}.{self.spreadsheet.loc[i, "Type"]}.png',
            "TypeOverlay": f'%PROJECT%/{self.spreadsheet.loc[i, "Type"]}.png',
            "AttributeOverlay": f'%PROJECT%/{self.spreadsheet.loc[i, "Attribute"]}.png',
            "Art": f'%PROJECT%/{self.spreadsheet.loc[i, "Code"]}.png',
            "Text": self.spreadsheet.loc[i, "Text"],
            "Name": self.spreadsheet.loc[i, "Name"],
            "Id": self.spreadsheet.loc[i, "Code"],
            "Rank": "{r} " * int(self.spreadsheet.loc[i, "Rank"]) if self.spreadsheet.loc[i, "Rank"].isnumeric() else self.spreadsheet.loc[i, "Rank"],
            "Life": str(self.spreadsheet.loc[i, "Life"]).replace('.0', ""),
            "Power": str(self.spreadsheet.loc[i, "Power"]).replace('.0', ""),
            "Attribute": self.spreadsheet.loc[i, "Attribute"],
            "Type": f'{self.spreadsheet.loc[i, "Class"]} {self.spreadsheet.loc[i, "Type"]}' if self.spreadsheet.loc[i, "Class"] else self.spreadsheet.loc[i, "Type"],
            "Hand": handSubstring,
            "Cost": str(self.spreadsheet.loc[i, "Cost"]).replace('.0', ""),
            }
            returnSpreadsheet.loc[len(returnSpreadsheet)] = data
        return returnSpreadsheet


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
ss.convertCardCodesToCardCreatorCSV().to_csv("www\data\cardcreator.csv", index=False)
