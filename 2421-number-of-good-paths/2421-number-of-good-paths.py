class Solution(object):
	def numberOfGoodPaths(self, vals, edges):

		has_path = {}
		path = len(vals)
		V = set(vals)
		if len(V) == 1:

			s=[]
			for i in range(len(vals)):
				s.append(i+1)

			path = sum(s)
			return path
		for i,c in enumerate(vals):
			if c in has_path:
				has_path[c].append(i)
			else:
				has_path[c] = []
				has_path[c].append(i)

		nodes = {0:0}
		for c in edges:
			if c[0] > c[1]:
				nodes[c[0]] = c[1]
			else:
				nodes[c[1]] = c[0]
		
		path_pair = set()

		for num in has_path:
			for c,i in enumerate(has_path[num]):
				for j in has_path[num][c+1:]:
					current_node1 = i
					current_node2 = j
					
					if (current_node1, nodes[current_node2]) in path_pair:
						path += 1
						path_pair.add((i,j))
						continue
					found = False
					while not found:
						if current_node1< current_node2:
							current_node2 = nodes[current_node2]
							if vals[current_node2] > vals[i]:
								break
						elif current_node1 > current_node2:
							current_node1 = nodes[current_node1]
							if vals[current_node1] > vals[i]:
								break
						else:
							path += 1
							
							path_pair.add((i,j))
							found = True

		return path
