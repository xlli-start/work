#include <chrono>
#include <ctime>
#include <locale>
#include <sstream>
#include <string>
#include <iostream>
#include <ctime>
#include <iomanip>
using namespace std;

int main(int argc, char* argv[])
{
    // 时间字符串转格式化时间
    string begin = "20:00:00";
    tm m ={};
    istringstream ss(begin);
    ss >> get_time(&m, "%H:%M:%S");
    cout << m.tm_hour << endl;
    cout << m.tm_min << endl;
    cout << m.tm_sec << endl;
    // 取当前的系统时间 格式化时间 取小时 分钟 秒
    chrono::system_clock::time_point now = chrono::system_clock::now();
    time_t tt = chrono::system_clock::to_time_t(now);
    tm* p = localtime(&tt);
    cout << p->tm_hour << endl;
    cout << p->tm_min << endl;
    cout << p->tm_sec << endl;
    
    return 0;
}
