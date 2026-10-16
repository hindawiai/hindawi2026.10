#include <iostream>
class Counter { public: int value; };
int main() { Counter counter; counter.value = 42; std::cout << counter.value << std::endl; return 0; }
