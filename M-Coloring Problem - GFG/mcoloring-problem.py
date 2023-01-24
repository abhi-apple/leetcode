#User function Template for python3


#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
def graphColoring(graph, m, n):
    
    #your code here
    def safe(nd,col,graph,n,c):
        for k in range(n):
            if k!=nd and graph[k][nd]==1 and col[k]==c:
                return False
        return True
    def solve(nd,col,m,n,graph):
        if nd==n:
            return True
        for i in range(1,m+1):
            if safe(nd,col,graph,n,i):
                col[nd]=i
                if solve(nd+1,col,m,n,graph):
                    return True
                col[nd]=0
        return False
    col=[0]*n
    return solve(0,col,m,n,graph)
    


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