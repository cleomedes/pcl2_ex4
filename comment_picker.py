# !/usr/bin/env python3
# -*- coding: utf8 -*-
# Olivier Fischer

import bz2
import gzip
import json
from typing import BinaryIO

def mk_meme_corpus(infile: BinaryIO, outfile: str, min_score: int=100, min_len: int=1, max_len: int=50):
    with gzip.open(outfile+'.txt.gz', 'wt') as bestcomments:
        comment_hashes = set()
        # we will deduplicate identical comments, ignoring possible different authors, dates, etc. 
        for line in infile: 
            comment = line.decode('utf8')
            comment_dict = json.loads(comment)
            comment = comment_dict['body']
            if comment_dict['score'] >= 100 and len(comment) in range(min_len, max_len+1):
                comment_hash = hash(comment)
                if comment_hash not in comment_hashes: 
                    comment_hashes.add(comment_hash) 
                    bestcomments.write(comment + '\n')

def main():
    with bz2.open('RC_2012-06.bz2', 'rb') as infile:
        mk_meme_corpus(infile, 'bestcomments')

if __name__ == "__main__":
    main()