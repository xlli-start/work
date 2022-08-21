#include <iostream>
#include <fstream>
#include <string>
#include <assert.h>

using namespace std;

void segWord(ofstream& fp, int readline, const string line){
    int next = 0;
    int i = (readline > 1) ? 0 : 3;
    for(; i<line.length(); i += next){
    // 考虑 写循环是否会 写这样的 结果会是什么情况： 
    /*for(int i = 0; i<line.size(); i++){

    }*/
    // 也可以这样写 
    /*while (i < line.size()){

    }*/
        /*
            仿BOM的文件头写入 0xEF 0xBB 0xBF(写入顺序从左到右)
        */
        /*         
            if(((line[0] & 0xF0) == 0xE0) && ((line[1] & 0xFE) == 0xBA) && ((line[2] & 0xFC) == 0xBC)){
                i += 3;
            } 
        */
        if((line[i] & 0x80) == 0x00){
            next = 1;
        }
        else if((line[i] & 0xE0) == 0xC0){
            next = 2;
        }
        else if((line[i] & 0xF0) == 0xE0){
            next = 3;
        }
        else if((line[i] & 0xF8) == 0xF0){
            next = 4;
        }
        else if((line[i] & 0xFC) == 0xF8){
            next = 5;
        }
        else{
            continue; // 没有cntinue会在首行加上空格
        }
        string word = ((i + next + 1) < line.length()) ? (line.substr(i, next) + " ") : line.substr(i, next);
        fp << word;
    }
    fp << endl;
}

int main(int argc, char*argv[]){
    ifstream read(argv[1]);
    if(!read){
        return 0;
    }
    ofstream write(argv[2]);
    string line;
    int readline = 0;
    while(getline(read, line)){
        readline += 1;
        segWord(write, readline, line);
        // break;
    }
    return 0;
}
