WikiParser

1. The above parser is aimed for extracting the visible text from the xml dumps of wikipedia .

2. The output would be in .txt format with different .txt for different pages with the name being the id and the revision id of the page. 

3. Usage is very simple : transfer the two .py files to the location of the xml file , rename the xml file as b.xml and then run parser.py using python3 . The output would be various .txt files generated in the same folder with there names as the id and the revision id of the respective page in the xml document .

4. The library is simple and readable , all the filtering has been done in wikiparser.py hence one can change/add code to it in order to tailor it to one's use .

Note: The above library aims to keep the text which we see on the wikipedia pages as they are rendered on the web browser . All the tables/infobox within the wikipedia pages have been removed . Only the text part of the wikipedia articles/pages is given as the output .


Refer to the syntax of the WikiText Markup for more details .
Following are the details of what the library does as of now on the xml dumps .

Processed :

1.) Templates

Removed Content Text :

1.) Infobox

2.) Files (Images,audio,etc)

3.) Comments

4.) References

5.) Sections :

5.a.) See Also Content
		
5.b) Notes

5.c) External Links

5.d) References

5.e) Bibliography

6) Templates :

6.a) Quote

6.b) About

6.c) Switch-Case

6.d) Expression

6.e) Main-Article 

7) Convertions

8) Dates

