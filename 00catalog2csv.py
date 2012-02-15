from operator import itemgetter
import re
import sys

def main():
    catalog_fn = sys.argv[1]
    catalog_csv_fn = sys.argv[2]
    author_count_fn = sys.argv[3]
    ebook_regex = re.compile(r'<pgterms:etext rdf:ID="etext(\d+)">(?:.*?)</pgterms:etext>', re.DOTALL)

    language_regex = re.compile(r'<dc:language><dcterms:ISO639-2><rdf:value>(.*?)</rdf:value></dcterms:ISO639-2></dc:language>', re.DOTALL)
    author_regex = re.compile(r'<dc:creator rdf:parseType="Literal">(.*?)</dc:creator>', re.DOTALL)
    title_regex = re.compile(r'<dc:title rdf:parseType="Literal">(.*?)</dc:title>', re.DOTALL)

    csv_out_f = open(catalog_csv_fn, 'w')
    author_count_f = open(author_count_fn, 'w')

    author_count = {}

    for match in ebook_regex.finditer(open(catalog_fn).read()):
        ebook_id = match.group(1)
        node_text = match.group(0)

        lang_match = language_regex.search(node_text)
        if not lang_match or lang_match.group(1) != "en":
            continue

        author_match = author_regex.search(node_text)
        title_match = title_regex.search(node_text)

        if author_match and title_match:
            author_txt = author_match.group(1).split("\n", 1)[0]
            title_txt = title_match.group(1).split("\n", 1)[0]

            author_count[author_txt] = author_count.get(author_txt, 0) + 1
            csv_out_f.write("%s\n" % "\t".join( (ebook_id, author_txt, title_txt) ) )

    for author, count in sorted(author_count.items(), key=itemgetter(1), reverse=True):
        author_count_f.write("%d\t%s\n" % (count, author))

    author_count_f.close()
    csv_out_f.close()

if __name__ == "__main__":
    main()
