#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(){

    string songs [] = {
         "Come Alive",
         "Rock DJ",
         "Another Day of the Sun",
         "Whiplash", 
         "怪獣", 
         "We Are Confidence Men"
    };

    vector<int> bpms  = {118, 103, 126, 107, 130, 118,};
    sort(bpms.begin(), bpms.end());
    // for (int i : bpms) {
    //     cout << i << " \n";
    // }


    for(int i = 0; i < 5; i++){
        cout << songs[i] << " is " << bpms[i] << " ";
    }


    return 0;
}
