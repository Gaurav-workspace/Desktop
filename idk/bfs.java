import java.util.*;
public class bfs {
    static void BFS(int[][] graph,int start){
        int[] visited = new int[graph.length];
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        visited[start]=1;
        while (!q.isEmpty()) {
            int value = q.poll();
            System.out.print(value+" ");
            for (int i = 0; i < visited.length; i++) {
                if (graph[value][i]==1
                    &&
                    visited[i]==0) {

                    visited[i]=1;
                    q.add(i);
                }
            }
        }
        System.out.println();
    }
    public static void main(String[] args) {
        int[][] graph = {
            {0,1,0,0,1},
            {1,0,1,0,0},
            {0,1,0,1,1},
            {0,0,1,0,0},
            {1,0,1,0,0}
        };
        BFS(graph, 0);
        BFS(graph, 1);
        BFS(graph, 2);
        BFS(graph, 3);
    }
}
