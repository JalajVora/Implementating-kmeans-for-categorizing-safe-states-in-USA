from random import randint, choice
import matplotlib.pyplot as plt

def doPlot(array, color, symbol) :
	global figure
	x = [i[0] for i in array]
	y = [i[1] for i in array]
	plt.plot(x, y, color+symbol)
	plt.axis([-5,105,-5,105])
	plt.savefig(filePath+str(figure)+".png")
	# plt.close()
	print figure
	figure += 1
	

def doAdvancedPlot() :
	global figure
	plt.close()
	# doPlot(clusterHeads, "g", "o")
	for c in range(clusterNum) :
		x = [i[0] for i in clusters[c]]
		y = [i[1] for i in clusters[c]]
		plt.plot(x, y, colorType[c])
	plt.axis([-5,105,-5,105])
	plt.savefig(filePath+str(figure)+".png")
	# plt.close()
	print figure
	figure += 1
	

def assignClusterHead() :
	global clusters, figure
	clusters = []
	for i in range(clusterNum) :
		clusters.append([])

	for i in range(num) :
		temp = []
		# print nodes[i]
		for j in range(clusterNum) :
			d = calcDistance(nodes[i], clusterHeads[j])
			temp.append(d)
		# print temp
		c = temp.index(min(temp))
		clusters[c].append(nodes[i])
		print "assigning " + str(nodes[i]) + " to " + str(clusterHeads[c])
		plt.plot([nodes[i][0], clusterHeads[c][0]], [nodes[i][1], clusterHeads[c][1]], "y-")
		plt.savefig(filePath+str(figure)+".png")
		print figure
		figure += 1


def calcCentroid(array) :
	sumx = sum([i[0] for i in array])
	sumy = sum([i[1] for i in array])
	return ((sumx+0.0)/len(array), (sumy+0.0)/len(array))

def calcDistance(A, B) :
	x1, y1 = A
	x2, y2 = B
	dist = (((x1-x2)**2) + ((y1-y2)**2)) ** 0.5
	return dist


def printArray(array) :
	for i in range(len(array)) :
		print array[i],
		if (i+1) % 5 == 0 :
			print ""
	print ""
	print "====="


raw_input("Press Enter")

num = 100
maximum = 100
clusterNum = 3
colorType = ["ro", "ko", "mo"]
figure = 0
filePath = "images2/"
clusters = []
clusterHeads = []
prevClusterHeads = []
nodes = []

#===========================
#generating random 2D points
#===========================
for i in range(num) :
	i = randint(0, maximum)
	j = randint(0, maximum)
	nodes.append((i,j))
# print "nodes"
# printArray(nodes)
doPlot(nodes, "b", "o")
# plt.close()

#===============================
#Choosing cluster heads randomly
#===============================
while len(clusterHeads) < clusterNum :
	a = choice(nodes)
	if a not in clusterHeads :
		clusterHeads.append(a)

print clusterHeads

#==================
#Converge centroids
#==================
doPlot(clusterHeads, "g", "o")
# assignClusterHead()

while prevClusterHeads != clusterHeads :
	assignClusterHead()
	doAdvancedPlot()
	prevClusterHeads = list(clusterHeads)

	print "centroids"
	for i in range(clusterNum) :
		clusterHeads[i] = calcCentroid(clusters[i])

	doPlot(clusterHeads, "g", "o")

	print clusterHeads