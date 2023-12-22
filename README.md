# gpea-tw-donation-records
This is a Python program designed to generate donation records for Taiwan.

 - **Input**: A csv file
 - **Output**: A pdf file
 - **Process**: Read the .csv file, and convert it to the HTML format to draw the table, and then save it as a .pdf file
 - **Note**: In this file, we use wkhtmltopdf, please download and install it: https://wkhtmltopdf.org/downloads.html


## Steps of using it

 1. Open the **csv2pdf.py** and edit the following four values
	 - csv_path = 'files/test.csv' # Give a .csv file as Input
	 - html_path = 'files/test.html' # Give a .html file as temporary file
	 - output_pdf_path = 'files/test.pdf' # Give a .pdf file as Output
	 - output_path = 'files/output.txt' # The log file of translated data
 2. In the command line, execute **`py csv2pdf.py`**
