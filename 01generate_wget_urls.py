import sys

handpicked_authors = [
    "Twain, Mark, 1835-1911",
    "Dickens, Charles, 1812-1870",
    "Doyle, Arthur Conan, Sir, 1859-1930",
    "Wells, H. G. (Herbert George), 1866-1946",
    "Churchill, Winston, 1871-1947",
    "Baum, L. Frank (Lyman Frank), 1856-1919",
    "Verne, Jules, 1828-1905",
    "London, Jack, 1876-1916",
    "Kipling, Rudyard, 1865-1936",
    "Dumas, Alexandre, 1802-1870",
    "Plato, 427? BC-347? BC",
    "Sinclair, Upton, 1878-1968",
"Melville, Herman, 1819-1891",
    "Carroll, Lewis, 1832-1898",
    "Poe, Edgar Allan, 1809-1849",
    "Lincoln, Abraham, 1809-1865",
    "United States. Central Intelligence Agency",
    "Austen, Jane, 1775-1817",
    "Aesop, 620 BC-563 BC",
    "Voltaire, 1694-1778",
    "Rousseau, Jean-Jacques, 1712-1778",
    "Homer, 750? BC-650? BC",
    "United States",
    "Thoreau, Henry David, 1817-1862",
    "Longfellow, Henry Wadsworth, 1807-1882",
    "Dick, Philip K., 1928-1982",
    "Muir, John, 1838-1914",
    "Kafka, Franz, 1883-1924"
]

def main():
    catalog_fn = sys.argv[1]
    urls_fn = sys.argv[2]

    urls_f = open(urls_fn, 'w')
    for line in open(catalog_fn):
        ebook_id, author, title = line.split("\t")
        if author in handpicked_authors:
            url = "http://www.gutenberg.org/files/%s/%s.txt" % (ebook_id, ebook_id)
            urls_f.write("%s\n" % url)

    # use urls_f as a --input-file to wget
    urls_f.close()

if __name__ == "__main__":
    main()
