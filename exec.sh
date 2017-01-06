#!/bin/sh
python test_formatter.py static/crf/to_seg.txt static/crf/crf_tag.txt
crf_test -m train1.model static/crf/crf_tag.txt > static/crf/tagfile.txt
python label_2_seg.py static/crf/tagfile.txt static/crf/segfile.txt
#rm -f model
