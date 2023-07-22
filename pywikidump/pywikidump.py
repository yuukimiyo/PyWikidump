# coding: utf-8

import regex

def getArticlesMultistreamIndexArray(indexText, articlesSize):
    '''
    @param indexText whole text of pages-articles-multistream-index.txt
    @param articlesSize Size of whole of pages-articles-multistream.xml.bz2
    @return List of [blockOffset, blockSize, index] for the multistream block.
    '''

    indexArray = []
    last_offset = 0
    for i, l in enumerate(indexText.splitlines()):
        ll = l.split(':', 2)
        ll[0] = int(ll[0])

        if ll[0] != last_offset:
            indexArray.append([last_offset, ll[0] - last_offset, i])

        last_offset = ll[0]

    # 先頭要素（[0, n, i]）を削除
    indexArray = indexArray[1:]

    # リストの最終行を追加
    indexArray.append([last_offset, int(articlesSize) - last_offset, i])

    return indexArray
