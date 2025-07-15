#include <string>
#include <vector>
#include <map>

using namespace std;

string solution(vector<string> survey, vector<int> choices) {
    int score[8] = { 0,3,2,1,0,1,2,3 };
string answer = "";
map <char, int> m;
for (int i = 0; i < survey.size(); i++) {
    string s = survey[i];
    int p = choices[i];
    m[s[p / 4]] += score[p];
}

answer += m['R'] >= m['T'] ? "R" : "T";
answer += m['C'] >= m['F'] ? "C" : "F";
answer += m['J'] >= m['M'] ? "J" : "M";
answer += m['A'] >= m['N'] ? "A" : "N";


return answer;
}