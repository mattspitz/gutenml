#!/bin/bash

# create directory storage structure
mkdir -p data/catalog
mkdir -p data/books/raw

# download project gutenberg's catalog
wget http://www.gutenberg.org/feeds/catalog.rdf.bz2

# unzip the archive
bunzip2 catalog.rdf.bz2

# move catalog to proper directory
mv catalog.rdf data/catalog

# convert the RDF catalog to TSV, generate counts by author
python 00catalog2csv.py data/catalog/catalog.rdf data/catalog/catalog.tsv data/catalog/author_count.tsv

# pick some authors based on author_count, add them to 01generate_wget_urls.py
python 01generate_wget_urls.py data/catalog/catalog.tsv data/books/urls.txt

# download books with trick to bypass bot deterrent
cd data/books/raw
wget --referer="http://www.google.com" \
    --user-agent="Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6" \
    --header="Accept: text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5" \
    --header="Accept-Language: en-us,en;q=0.5" \
    --header="Accept-Encoding: gzip,deflate" \
    --header="Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7" \
    --header="Keep-Alive: 300" \
    --wait 30 \
    --input-file ../urls.txt
