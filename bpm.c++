#include <iostream>

#include <algorithm>
#include <vector>
using namespace std;


int main(){

    map <int, string> songBpm =
    {
        {118, "Come Alive"},
        {103, "Rock DJ"},
        {126, "Another Day of The Sun"},
        {107, "Whiplash"},
        {130, "怪獣"},
        {118, "We Are Confidense Men"}
    };


    for(auto i: songBpm){
        cout << i.second << ": " << i.first <<endl;
    }



    return 0;

}
