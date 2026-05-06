#include <bits/stdc++.h>
#include <omp.h>
#include <chrono>

using namespace std;

// ============================
// Tree Node
// ============================
class TreeNode
{
public:
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int x)
    {
        val = x;
        left = NULL;
        right = NULL;
    }
};

// ============================
// Sequential BFS
// ============================
void bfs(TreeNode *root)
{
    if (!root)
        return;

    queue<TreeNode *> q;
    q.push(root);

    while (!q.empty())
    {
        TreeNode *node = q.front();
        q.pop();

        if (node->left)
            q.push(node->left);

        if (node->right)
            q.push(node->right);
    }
}

// ============================
// Optimized Parallel BFS
// ============================
void parallel_bfs(TreeNode *root)
{
    if (!root)
        return;

    vector<TreeNode *> currentLevel;
    currentLevel.push_back(root);

    while (!currentLevel.empty())
    {
        vector<TreeNode *> nextLevel;

        #pragma omp parallel
        {
            vector<TreeNode *> localNext;

            #pragma omp for nowait
            for (int i = 0; i < currentLevel.size(); i++)
            {
                TreeNode *node = currentLevel[i];

                if (node->left)
                    localNext.push_back(node->left);

                if (node->right)
                    localNext.push_back(node->right);
            }

            #pragma omp critical
            nextLevel.insert(nextLevel.end(),
                             localNext.begin(),
                             localNext.end());
        }

        currentLevel.swap(nextLevel);
    }
}

// ============================
// Sequential DFS
// ============================
void dfs(TreeNode *root)
{
    if (!root)
        return;

    dfs(root->left);
    dfs(root->right);
}

// ============================
// Optimized Parallel DFS
// ============================
void parallel_dfs(TreeNode *root, int depth = 0)
{
    if (!root)
        return;

    // Limit thread creation depth
    if (depth > 4)
    {
        dfs(root);
        return;
    }

    #pragma omp task shared(root)
    parallel_dfs(root->left, depth + 1);

    #pragma omp task shared(root)
    parallel_dfs(root->right, depth + 1);

    #pragma omp taskwait
}

// ============================
// Build Large Binary Tree
// ============================
TreeNode* buildTree(int levels)
{
    if (levels <= 0)
        return NULL;

    int totalNodes = (1 << levels) - 1;

    vector<TreeNode*> nodes(totalNodes + 1);

    for (int i = 1; i <= totalNodes; i++)
    {
        nodes[i] = new TreeNode(i);
    }

    for (int i = 1; i <= totalNodes / 2; i++)
    {
        if (2 * i <= totalNodes)
            nodes[i]->left = nodes[2 * i];

        if (2 * i + 1 <= totalNodes)
            nodes[i]->right = nodes[2 * i + 1];
    }

    return nodes[1];
}

// ============================
// Main
// ============================
int main()
{
    int levels;

    cout << "Enter number of tree levels: ";
    cin >> levels;

    TreeNode *root = buildTree(levels);

    cout << "\nTotal Nodes: "
         << ((1LL << levels) - 1) << endl;

    // ---------------- Sequential BFS ----------------
    auto start = chrono::high_resolution_clock::now();

    bfs(root);

    auto end = chrono::high_resolution_clock::now();

    cout << "\nSequential BFS Time: "
         << chrono::duration_cast<chrono::milliseconds>(end - start).count()
         << " ms\n";

    // ---------------- Parallel BFS ----------------
    start = chrono::high_resolution_clock::now();

    parallel_bfs(root);

    end = chrono::high_resolution_clock::now();

    cout << "Parallel BFS Time: "
         << chrono::duration_cast<chrono::milliseconds>(end - start).count()
         << " ms\n";

    cout << "----------------------------------------\n";

    // ---------------- Sequential DFS ----------------
    start = chrono::high_resolution_clock::now();

    dfs(root);

    end = chrono::high_resolution_clock::now();

    cout << "Sequential DFS Time: "
         << chrono::duration_cast<chrono::milliseconds>(end - start).count()
         << " ms\n";

    // ---------------- Parallel DFS ----------------
    start = chrono::high_resolution_clock::now();

    #pragma omp parallel
    {
        #pragma omp single
        parallel_dfs(root);
    }

    end = chrono::high_resolution_clock::now();

    cout << "Parallel DFS Time: "
         << chrono::duration_cast<chrono::milliseconds>(end - start).count()
         << " ms\n";

    return 0;
}
