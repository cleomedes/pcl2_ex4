# !/usr/bin/env python3
# -*- coding: utf8 -*-
# PCL II 
# Übung 04
# Aufgabe 1.2
# Olivier Fischer

import random
import gzip
import lxml.etree as ET
from typing import BinaryIO

def split_corpus(infile: BinaryIO, targetdir: str, n: int=1000):
    counter = 0
    reservoir = []
    # Note: we will create one reservoir which contains both our test and development set.
    # Let n be the number of elements in each the test and the development set.
    # Hence our reservoir will contain 2*n elements, which we will later divide into test and development set.
    with gzip.open(targetdir+'/abstracts.txt.training.gz', 'wt', encoding='utf8') as training:
        ## if deduplication is necessary
        # hashes = set()
        for _, article in ET.iterparse(infile, tag='document'): 
            counter += 1
            sentences = ' '.join(name.text for name in article.iterfind('.//section/sentence'))
            ## if deduplication is necessary
            # if hash(sentences) in hashes:
              #  continue
            # hashes.add(hash(sentences)
            if counter <= 2*n:
                reservoir.append(sentences)
            else: 
                m = random.randint(0,counter)
                if m < n: 
                    training.write(reservoir[m])
                    reservoir[m] = sentences
                else: 
                    training.write(sentences)
            article.clear()
    # now we will shuffle our reservoir to randomize a bit more before dividing the reservoir into development and test set
    with gzip.open(targetdir+'/abstracts.txt.development.gz', 'wt', encoding='utf8') as development, gzip.open(targetdir+'/abstracts.txt.test.gz', 'wt', encoding='utf8') as test:
        random.shuffle(reservoir)
        development.write('\n'.join(reservoir[:n]))
        test.write('\n'.join(reservoir[n:]))

def main():
    with gzip.open('Korpusdaten/abstracts.xml.gz', 'rb') as infile:
        split_corpus(infile, 'Aufgabe1.2')

if __name__ == "__main__":
    main()