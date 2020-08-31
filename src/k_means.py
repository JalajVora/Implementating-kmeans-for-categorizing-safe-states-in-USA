from random import randint, choice

def assignClusterHead() :
	global clusters
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
assignClusterHead()

while prevClusterHeads != clusterHeads :
	assignClusterHead()

	prevClusterHeads = list(clusterHeads)

	print "centroids"
	for i in range(clusterNum) :
		clusterHeads[i] = calcCentroid(clusters[i])

	print clusterHeads