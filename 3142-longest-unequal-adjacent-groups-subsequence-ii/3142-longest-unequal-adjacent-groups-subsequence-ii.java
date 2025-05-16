import java.util.*;

public class Solution {
    public List<String> getWordsInLongestSubsequence(String[] words, int[] groups) {
        int n = words.length;
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());

        // Build graph: only forward edges (i < j)
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (groups[i] != groups[j] &&
                    words[i].length() == words[j].length() &&
                    hammingDistance(words[i], words[j]) == 1) {
                    graph.get(i).add(j);  // i → j
                }
            }
        }

        // Memoization
        List<Integer>[] memo = new List[n];
        List<Integer> bestPath = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            List<Integer> path = dfs(i, graph, memo);
            if (path.size() > bestPath.size()) {
                bestPath = path;
            }
        }

        List<String> result = new ArrayList<>();
        for (int idx : bestPath) {
            result.add(words[idx]);
        }
        return result;
    }

    private List<Integer> dfs(int curr, List<List<Integer>> graph, List<Integer>[] memo) {
        if (memo[curr] != null) return memo[curr];

        List<Integer> maxPath = new ArrayList<>();
        for (int next : graph.get(curr)) {
            List<Integer> subPath = dfs(next, graph, memo);
            if (subPath.size() > maxPath.size()) {
                maxPath = subPath;
            }
        }

        List<Integer> result = new ArrayList<>();
        result.add(curr);
        result.addAll(maxPath);
        memo[curr] = result;
        return result;
    }

    private int hammingDistance(String a, String b) {
        int dist = 0;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != b.charAt(i)) dist++;
        }
        return dist;
    }
}
