class सूची {
    int *तत्त्व;
    int आकार;
public:
    सूची(int अ) : आकार(अ) { तत्त्व = new int[अ]; }
    ~सूची() { delete[] तत्त्व; }
    void स्थापित(int इ, int म) { तत्त्व[इ] = म; }
    int प्राप्त(int इ) { return तत्त्व[इ]; }
};
