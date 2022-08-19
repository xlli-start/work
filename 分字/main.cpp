#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void segWord(ofstream& fp, const string line){
    int next = 0;
    for(int i = 0; i<line.length(); i += next){
    // while (i < line.size()){
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
        string word = line.substr(i, next);
        fp << word << " ";
    }
    fp << endl;
}

int main(){
    ifstream read("Sentence.txt");
    if(!read){
        return 0;
    }
    ofstream write("segSentence.txt");
    string line{};
    while(getline(read, line)){
        segWord(write, line);
        // break;
    }
    return 0;
}
