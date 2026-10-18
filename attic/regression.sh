#!/bin/bash
export PATH="/tmp/flexroot/usr/bin:$PATH"
export LD_LIBRARY_PATH="/tmp/flexroot/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH"
cd "$(dirname "$0")/.."

echo "=== Hindi ==="
flex -8 -o /tmp/h2c.c lang/hindawi/upstream/chintamani/guru/h2c.uhin 2>/dev/null
gcc -o /tmp/h2c /tmp/h2c.c -L/tmp/flexroot/usr/lib/x86_64-linux-gnu -lfl 2>/dev/null
echo 'पूर्णांक मुख्य() { वापस 42; }' | /tmp/h2c

echo "=== Bengali ==="
flex -8 -o /tmp/bn.c lang/hindawi/upstream/chintamani/bengali/h2c.uhin 2>/dev/null
gcc -o /tmp/bn /tmp/bn.c -L/tmp/flexroot/usr/lib/x86_64-linux-gnu -lfl 2>/dev/null
echo 'পূর্ণসংখ্যা প্রধান() { ফেরত 42; }' | /tmp/bn

echo "=== Multi-file ==="
echo 'int add(int a, int b) { return a + b; }' > /tmp/lib.c
echo 'int add(int, int); int main() { return add(20, 22); }' > /tmp/main.c
gcc -o /tmp/mf /tmp/lib.c /tmp/main.c && /tmp/mf
echo "exit: $?"

echo "=== DONE ==="
