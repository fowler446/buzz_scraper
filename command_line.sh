wget -r http://www.buzzfeed.com/
find www.buzzfeed.com/ -maxdepth 2 -mindepth 2 -name '*[0-9][0-9]?*' ! -name *=mobile* ! -name *20xnx> buzz_posts.txt
