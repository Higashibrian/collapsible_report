# collapsible_report
Provides some functions in order to create an HTML document with a series of collapsible buttons. 
Useful for any application where you want to programmatically create an html document with sections that can be hidden or shown.

The insert_single_dropdown function in this class takes a tuple in the format (collapsed_text,html) and it can be nested infinitely.
This allows you to give the person who views the document an option to start with a high level view of the results and click through as deep as they want into a series of granular results including html tables and images if desired.

It was built to provide a report on a test which was run daily.
The test compared between 2000-6500 pairs of XML files with at least 126 distinct fields that needed to be compared in each file.
excel was not a viable option.
