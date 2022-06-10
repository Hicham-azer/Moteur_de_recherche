from color_descriptor import ColorDescriptor
from searcher import Searcher
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
	help = r"C:\\Users\\hicha\Desktop\\moteur_de_recherche")
ap.add_argument("-q", "--query", required = True,
	help = "C:\\Users\\hicha\\Desktop\\moteur_de_recherche\\queries")
ap.add_argument("-r", "--result-path", required = True,
	help = "C:\\Users\\hicha\\Desktop\\moteur_de_recherche\\dataset")
args = vars(ap.parse_args())
# initialize the image descriptor
cd = ColorDescriptor((8, 12, 3))

# load the query image and describe it
query = cv2.imread(args["query"])
features = cd.describe(query)
# perform the search
searcher = Searcher(args["index"])
results = searcher.search(features)
# display the query
cv2.imshow("Query", query)
# loop over the results
for (score, resultID) in results:
	# load the result image and display it
	result = cv2.imread(resultID)
	cv2.imshow("Result", result)
	cv2.waitKey(0)


