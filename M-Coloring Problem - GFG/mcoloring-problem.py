#User function Template for python3


#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
def graphColoring(graph, m, n):
    
    #your code here
    def solve(node):
        def safe(nd,i):
            for k in range(n):
                if k!=nd and graph[k][nd]==1 and col[k]==i:
                    return False
            return True
        if node==n:
            return True
        for i in range(1,m+1):
            if safe(node,i):
                col[node]=i
                if solve(node+1):
                    return True
                col[node]=0
        return False
                
    col=[0]*n
    if solve(0):
        return 1
    return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        V = int(input())
        k = int(input())
        m = int(input())
        list = [int(x) for x in input().strip().split()]
        graph = [[0 for i in range(V)] for j in range(V)]
        cnt = 0
        for i in range(m):
            graph[list[cnt]-1][list[cnt+1]-1]=1
            graph[list[cnt+1]-1][list[cnt]-1]=1
            cnt+=2
        if(graphColoring(graph, k, V)==True):
            print(1)
        else:
            print(0)

        t = t-1

# } Driver Code Ends