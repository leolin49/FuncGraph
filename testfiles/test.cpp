/*
 * @Author: leolin49@foxmail.com
 * @Date: 2023-11-08 15:46:35
 * @Last Modified by: leolin49
 * @Last Modified time: 2023-11-08 16:36:19
 */
#include <bits/stdc++.h>
using namespace std;

bool over = false;
int n, a, b;
int dir[8][2] = {{-1,-2}, {-2,-1}, {-2,1}, {-1, 2}, {1,2}, {2,1}, {2,-1}, {1,-2}};

struct Node {
    int x, y;
    int c;  // 方向策略：机会少的方向优先   Warnsdorff's algorithm
    int d;  // 离心策略：偏离中心位置的方向优先
};

struct cmp {
    bool operator()(Node& a, Node& b) {
        if (a.c == b.c) {
            return a.d < b.d;
        }
        return a.c > b.c;
    }
};

bool ok(int x, int y) {
    return !(x < 0 || x >= n || y < 0 || y >= n);
}

void print(vector<vector<int>>& g) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << g[i][j] << " ";
        }
        cout << endl;
    }
}

//void function_test_1()
//{
//    cout << "test" << endl;
//}

// 计算每个位置的下一步的位置数量
int cntNext(vector<vector<int>>& g, int x, int y) {
    int cnt = 0;
    for (int i = 0; i < 8; i++) {
        int next_x = x + dir[i][0];
        int next_y = y + dir[i][1];
        if (ok(next_x, next_y) && g[next_x][next_y] == 0) {
            cnt++;
        }
    }
    return cnt;
}

// (x,y)到中心点的曼哈顿距离
int getDis(int x, int y) {
    return abs(x - n / 2) + abs(y - n / 2);
}

// 表示当前位于（x,y）上，且已经走了step步
void backtrack(vector<vector<int>>& g, int x, int y, int step) {
    if (step == n * n) {
        if ((abs(x-((n/2)))==1&&abs(y-((n/2)))==2) || (abs(x-((n/2)))==2&&abs(y-((n/2)))==1)) { // 能否回到起点
            // print(g);
            over = true;
        }
        return;
    }
    priority_queue<Node, vector<Node>, cmp> q;
    for (int i = 0; i < 8; i++) {
        int next_x = x + dir[i][0];
        int next_y = y + dir[i][1];
        if (ok(next_x, next_y) && g[next_x][next_y] == 0) {
            Node node;
            int cnt = cntNext(g, next_x, next_y);
            int dis = getDis(next_x, next_y);
            node.x = next_x, node.y = next_y, node.c = cnt, node.d = dis;
            q.push(node);
        }
    }
    while (q.size()) {
        Node node = q.top();
        q.pop();
        g[node.x][node.y] = step + 1;
        backtrack(g, node.x, node.y, step + 1);
        if (over) return;
        g[node.x][node.y] = 0;
    }
}

int main() {
    cin >> n >> a >> b;
    vector<vector<int>> g(n, vector<int>(n, 0));
    // 无论起点是多少，都从(n/2, n/2)开始出发，后面再进行平移
    g[n/2][n/2] = 1;
    backtrack(g, n/2, n/2, 1);
    // 平移
    int s_val = g[a-1][b-1];  // 真实的起点值
    int offset = s_val - 1;   // 偏移量
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (g[i][j] > offset) {
                g[i][j] -= offset;
            } else {
                g[i][j] += (n * n - offset);
            }
        }
    }
    print(g);
    system("pause");
    return 0;
}
