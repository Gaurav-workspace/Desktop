
public class dfs {
    static void DFS(int[][] graph,
                    int[] visited,
                    int index){
        visited[index]=1;
        System.out.print(index+" ");
        for (int i = 0; i < graph.length; i++) {
            if(graph[index][i]==1
                &&
                visited[i]==0){
                DFS(graph,visited,i);
            }
        }
    }
    public static void main(String[] args) {
        
        int[] visited = new int[5];
        int[][] graph = {
            {0,1,0,0,1},
            {1,0,1,0,0},
            {0,1,0,1,1},
            {0,0,1,0,0},
            {1,0,1,0,0}
        };
        DFS(graph, visited, 0);
    }
}
