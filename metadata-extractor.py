#!usr/bin/env python

import pyPdf

def main():
	
	filename = <LOCATION_OF_THE_PDF>
	
	pdfFile = pyPdf.PdfFileReader(file(filename,'rb'))
	data = pdfFile.getDocumentInfo()

	print "----Metadata of the file----"
	
	for metadata in data:
		print metadata+ ":" +data[metadata]

if __name__ == '__main__':
	main()
