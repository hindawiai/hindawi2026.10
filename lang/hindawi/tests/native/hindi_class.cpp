#include <iostream>
class गणक {
    int मान;
public:
    गणक(int म) : मान(म) {}
    void जोड़(int म) { मान += म; }
    int प्राप्त() { return मान; }
};
int main() {
    गणक ग(10);
    ग.जोड़(5);
    std::cout << ग.प्राप्त() << std::endl;
    return 0;
}
