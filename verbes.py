from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

import sys
import random

if (len(sys.argv)) != 3:
	print "You need to specify level and number of reports"
	sys.exit (1)
	
level = int(sys.argv[1])
numberOfReports = int(sys.argv[2])
print "Using level " + str(level)
print "Generating " + str(numberOfReports) + " reports"

levelOneVerbs = set([
"A", 
"B", 
"C", 
"D", 
"E", 
"Nous Finissons",
"A1", 
"B1", 
"C1", 
"D1", 
"E1", 
"F1",
"A2", 
"B2", 
"C2", 
"D2", 
"E2", 
"F2"])

levelTwoVerbs = set([
"AX", 
"BX", 
"CX", 
"DX", 
"EX", 
"FX",
"A1X", 
"B1X", 
"C1X", 
"D1X", 
"E1X", 
"F1X",
"A2X", 
"B2X", 
"C2X", 
"D2X", 
"E2X", 
"F2X"])

for reportIndex in range(0, numberOfReports):
	# Page setup
	width, height = letter
	fileName = "report"+str(reportIndex)+".pdf"
	print "Generating report: " + fileName
	c = canvas.Canvas(fileName, pagesize=letter)
	c.setLineWidth(.3)
	c.setFont('Helvetica', 12)

	for pageIndex in range (2):
		if (pageIndex == 0):
			topPos = 750
		else:
			topPos = 350
		
		if (level == 1): 
			selectedVerbs = random.sample(levelOneVerbs, 12)
		else:
			selectedVerbs = random.sample(levelTwoVerbs, 12)
			
			
		# Name
		c.drawString(30, topPos, "Nom :")
		c.line(65,topPos,250,topPos)

		# Header
		c.drawString(250, topPos-50, "Judo verbes - Niveau " + str(level))

		for index, thisNoun in enumerate(selectedVerbs):
			lineLength = 125
			if index % 2 != 1:
				verticalPos = topPos-100-(index*20)
				horizPos = 30
				lineStart = horizPos+125
			else:
				verticalPos = topPos-100-((index-1)*20)
				horizPos = width/2
				lineStart = horizPos+125
				
			c.drawString(horizPos,verticalPos, str(index+1)+") "+thisNoun)
			c.line(lineStart,verticalPos,lineStart+lineLength, verticalPos)
		
	# Cleanup
	c.save()
	
print "Finished"