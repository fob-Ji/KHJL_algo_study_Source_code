#include <string>
#include <vector>
#include <sstream>

using namespace std;

int parents[2601];
string tables[2601];

int calc_loc(int r, int c) {
    return r * 51 + c;
}

vector<string> solution(vector<string> commands) {
    vector<string> answer;

    for (int i = 0; i < 2601; i++) {
        parents[i] = i;
        tables[i] = "EMPTY";
    }

    for (string& command : commands) {
        vector<string> tokens;
        stringstream ss(command);
        string token;
        while (ss >> token) tokens.push_back(token);
        if (tokens[0] == "UPDATE") {
            if (tokens.size() == 4) { // UPDATE r1 c1 value
                int loc = calc_loc(stoi(tokens[1]), stoi(tokens[2]));
                string value = tokens[3];
                tables[parents[loc]] = value;
            }
            else { // UPDATE v1 v2
                string value1 = tokens[1];
                string value2 = tokens[2];
                for (int i = 0; i < 2601; i++) {
                    if (tables[i].compare(value1) == 0) tables[i] = value2;
                }
            }
        }
        else if (tokens[0] == "MERGE") {
            int pos1 = calc_loc(stoi(tokens[1]), stoi(tokens[2]));
            int pos2 = calc_loc(stoi(tokens[3]), stoi(tokens[4]));
            int parent1 = parents[pos1];
            int parent2 = parents[pos2];
            if (parent1 != parent2) {
                for (int i = 0; i < 2601; i++) {
                    if (parents[i] == parent2) {
                        parents[i] = parent1;
                    }
                }
                if (tables[parent1] == "EMPTY" && tables[parent2] != "EMPTY") {
                    tables[parent1] = tables[parent2];
                }
                else tables[parent2] = tables[parent1];
            }
        }
        else if (tokens[0] == "UNMERGE") {
            int pos = calc_loc(stoi(tokens[1]), stoi(tokens[2]));
            int parent = parents[pos];
            string value = tables[parent];
            for (int i = 0; i < 2601; i++) {
                if (parents[i] == parent) {
                    parents[i] = i;
                    tables[i] = "EMPTY";
                }
            }
            tables[pos] = value;
        }
        else { // PRINT
            int pos = calc_loc(stoi(tokens[1]), stoi(tokens[2]));
            int parent = parents[pos];
            answer.push_back(tables[parent]);
        }
    }
    
    return answer;
}