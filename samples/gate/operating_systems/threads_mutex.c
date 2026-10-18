#include <stdio.h>
#include <pthread.h>
/* threads and synchronisation: four threads add to one total, a mutex making each addition whole */
long total = 0;
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
void *worker(void *unused) {
  for (int number = 1; number <= 1000; number++) { pthread_mutex_lock(&lock); total += number; pthread_mutex_unlock(&lock); }
  return unused;
}
int main(void) {
  pthread_t threads[4];
  for (int index = 0; index < 4; index++) pthread_create(&threads[index], NULL, worker, NULL);
  for (int index = 0; index < 4; index++) pthread_join(threads[index], NULL);
  printf("%ld\n", total);
  return 0;
}
