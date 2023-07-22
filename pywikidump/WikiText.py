# coding: utf-8

import regex

class WikiText():
    def __init__(self, wikitext=''):
        # wikitext
        self.wikitext = wikitext

        self.re_bblock = regex.compile(r'{{((?>[^{{}}]+|(?R))*)}}')
        self.re_infobox_title = regex.compile(r'^Infobox')
        self.re_infobox_attribute = regex.compile(r'^\s*\|\s*(.*?)\s*=\s*(.*)\s*$')
        self.re_categories = regex.compile(r'\[\[[C|c]ategory\s*:\s*(.+)?\]\]')
    
    def set(self, wikitext=''):
        self.wikitext = wikitext

    def getInfoboxTextArray(self):
        '''
        @return InfoboxTextArray.
        
        Get Array of InfoboxText from Wikitext.
        (I don't know its only one or not.)

        self.wikitextから{{ }}で囲まれたブロックのリストを作成し、
        そのうち「Infobox」で文章が開始するもののリストを返す。
        リストで返すのは、複数のinfoboxが記載されているケースがあるもしれないため。
        # https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Infoboxes
        '''

        infobox_array = [t for t in self.re_bblock.findall(self.wikitext) if self.re_infobox_title.match(t)]

        if len(infobox_array) > 0:
            return infobox_array
        else:
            return None

    def getInfobox(self, target=-9999):
        '''
        @param target Index of InfoboxArray(default: All)
        @return infobox Dictionary Object

        Get Infobox Dictionary Object from self.wikitext.
        Target num is index num of infobox array in wikitext.
        '''

        infobox_array = self.getInfoboxTextArray()

        if infobox_array == None:
            return {"infobox": {}}

        infobox_data = {}
        infobox_data["infobox"] = []
        for i, infobox_text in enumerate(infobox_array):
            infobox_data["infobox"].append({"name": "", "attributes": []})
            for j, info_field in enumerate(infobox_text.splitlines()):
                if j == 0:
                    infobox_data["infobox"][i]["name"] = info_field
                    infobox_data["infobox"][i]["attributes"] = {}
                else:
                    m = self.re_infobox_attribute.match(info_field)
                    if m:
                        # infobox_data["infobox"][i]["attributes"].append({m.group(1): m.group(2)})
                        infobox_data["infobox"][i]["attributes"][m.group(1)] = m.group(2)

        if target == -9999:
            return infobox_data
        else:
            return {"infobox": infobox_data["infobox"][target]}

    def getCategories(self):
        '''
        @return Array of category text
        '''

        categories = []
        for each_text in self.re_categories.findall(self.wikitext):
            if len(each_text) > 0:
                categories.append(each_text)

        return categories
