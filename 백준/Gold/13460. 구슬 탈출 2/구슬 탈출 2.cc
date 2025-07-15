#include <iostream>
#include <queue>
#include <tuple>
#include <cstring>

using namespace std;

const int MAX_N = 11;
const int MAX_M = 11;

int N, M;
char board[MAX_N][MAX_M];
bool visited[MAX_N][MAX_M][MAX_N][MAX_M];

struct Ball {
    int rx, ry; 
    int bx, by; 
    int depth;  
};

int dx[] = {-1, 1, 0, 0}; 
int dy[] = {0, 0, -1, 1};


pair<int, int> moveBall(int x, int y, int dir) {
    while (board[x + dx[dir]][y + dy[dir]] != '#' && board[x][y] != 'O') {
        x += dx[dir];
        y += dy[dir];
    }
    return {x, y};
}

int bfs(int rx, int ry, int bx, int by) {
    queue<Ball> q;
    memset(visited, false, sizeof(visited));

    q.push({rx, ry, bx, by, 0});
    visited[rx][ry][bx][by] = true;

    while (!q.empty()) {
        Ball cur = q.front();
        q.pop();

        if (board[cur.rx][cur.ry] == 'O' && board[cur.bx][cur.by] != 'O') return cur.depth;

        if (cur.depth >= 10) continue;

        for (int i = 0; i < 4; i++) {
            pair<int, int> red = moveBall(cur.rx, cur.ry, i);
            pair<int, int> blue = moveBall(cur.bx, cur.by, i);

            if (red == blue) {
                if (board[red.first][red.second] == 'O' && board[blue.first][blue.second] == 'O') continue;
                else {
                    int red_dist = abs(red.first - cur.rx) + abs(red.second - cur.ry);
                    int blue_dist = abs(blue.first - cur.bx) + abs(blue.second - cur.by);

                    if (red_dist > blue_dist) {
                        red.first -= dx[i];
                        red.second -= dy[i];
                    }
                    else {
                        blue.first -= dx[i];
                        blue.second -= dy[i];
                    }
                }
            }

            if (!visited[red.first][red.second][blue.first][blue.second]) {
                q.push({red.first, red.second, blue.first, blue.second, cur.depth + 1});
                visited[red.first][red.second][blue.first][blue.second] = true;
            }
        }
    }

    return -1;
}

int main() {
    int rx, ry, bx, by;

    cin >> N >> M;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> board[i][j];
            if (board[i][j] == 'R') {
                rx = i;
                ry = j;
            } else if (board[i][j] == 'B') {
                bx = i;
                by = j;
            }
        }
    }

    int result = bfs(rx, ry, bx, by);
    cout << result << endl;

    return 0;
}