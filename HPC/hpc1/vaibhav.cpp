#include <bits/stdc++.h>

using namespace std;

class TreeNode
{
public:
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

TreeNode *buildCompleteBinaryTree(int nodeCount)
{
    if (nodeCount <= 0)
    {
        return nullptr;
    }

    vector<TreeNode *> nodes(nodeCount + 1, nullptr);
    for (int i = 1; i <= nodeCount; i++)
    {
        nodes[i] = new TreeNode(i);
    }

    for (int i = 1; i <= nodeCount; i++)
    {
        int leftIndex = 2 * i;
        int rightIndex = 2 * i + 1;
        if (leftIndex <= nodeCount)
        {
            nodes[i]->left = nodes[leftIndex];
        }
        if (rightIndex <= nodeCount)
        {
            nodes[i]->right = nodes[rightIndex];
        }
    }

    return nodes[1];
}

void bfs(TreeNode *root)
{
    queue<TreeNode *> q;
    q.push(root);
    while (!q.empty())
    {
        TreeNode *node = q.front();
        q.pop();
        cout << node->val << " ";
        if (node->left)
        {
            q.push(node->left);
        }
        if (node->right)
        {
            q.push(node->right);
        }
    }
}

void dfs(TreeNode *root)
{
    stack<TreeNode *> s;
    s.push(root);
    while (!s.empty())
    {
        TreeNode *node = s.top();
        s.pop();
        cout << node->val << " ";
        if (node->right)
        {
            s.push(node->right);
        }
        if (node->left)
        {
            s.push(node->left);
        }
    }
}

void parallel_bfs(TreeNode *root)
{
    queue<TreeNode *> q;
    q.push(root);
    long long visitedCount = 0;
    long long visitedSum = 0;
    while (!q.empty())
    {
        int qSize = q.size();
#pragma omp parallel
        {
            long long localCount = 0;
            long long localSum = 0;
#pragma omp for
            for (int i = 0; i < qSize; i++)
            {
                TreeNode *node;
#pragma omp critical
                {
                    node = q.front();
                    q.pop();
                }
                localCount++;
                localSum += node->val;
                if (node->left)
                {
#pragma omp critical
                    q.push(node->left);
                }
                if (node->right)
                {
#pragma omp critical
                    q.push(node->right);
                }
            }
#pragma omp atomic
            visitedCount += localCount;
#pragma omp atomic
            visitedSum += localSum;
        }
    }
    cout << "[visited=" << visitedCount << ", sum=" << visitedSum << "] ";
}

void parallel_dfs(TreeNode *root)
{
    stack<TreeNode *> s;
    s.push(root);
    long long visitedCount = 0;
    long long visitedSum = 0;
    while (!s.empty())
    {
        int sSize = s.size();
#pragma omp parallel
        {
            long long localCount = 0;
            long long localSum = 0;
#pragma omp for
            for (int i = 0; i < sSize; i++)
            {
                TreeNode *node;
#pragma omp critical
                {
                    node = s.top();
                    s.pop();
                }
                localCount++;
                localSum += node->val;
                if (node->right)
#pragma omp critical
                    s.push(node->right);
                if (node->left)
#pragma omp critical
                    s.push(node->left);
            }
#pragma omp atomic
            visitedCount += localCount;
#pragma omp atomic
            visitedSum += localSum;
        }
    }
    cout << "[visited=" << visitedCount << ", sum=" << visitedSum << "] ";
}

int main()
{
    // Increased node count so traversal output/timing is clearer.
    // Perfect binary tree nodes: 7, 15, 31, 63, 127, ...
    const int nodeCount = 100;
    TreeNode *root = buildCompleteBinaryTree(nodeCount);

    cout << "BFS traversal: ";
    auto start = chrono::high_resolution_clock::now();
    bfs(root);
    auto end = chrono::high_resolution_clock::now();
    cout << "\nBFS took " << chrono::duration_cast<chrono::microseconds>(end - start).count() << " microseconds." << endl;
    cout << endl;

    cout << "Parallel BFS traversal: ";
    start = chrono::high_resolution_clock::now();
    parallel_bfs(root);
    end = chrono::high_resolution_clock::now();
    cout << "\nParallel BFS took " << chrono::duration_cast<chrono::microseconds>(end - start).count() << " microseconds." << endl;

    cout << "---------------------------------------------------------" << endl;

    cout << "DFS traversal: ";
    start = chrono::high_resolution_clock::now();
    dfs(root);
    end = chrono::high_resolution_clock::now();
    cout << "\nDFS took " << chrono::duration_cast<chrono::microseconds>(end - start).count() << " microseconds." << endl;
    cout << endl;

    cout << "Parallel DFS traversal: ";
    start = chrono::high_resolution_clock::now();
    parallel_dfs(root);
    end = chrono::high_resolution_clock::now();
    cout << "\nParallel DFS took " << chrono::duration_cast<chrono::microseconds>(end - start).count() << " microseconds." << endl;

    return 0;
}
