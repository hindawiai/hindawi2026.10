#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
/* concurrency: a bounded buffer of four slots between a producer and a consumer, with two semaphores and a mutex */
int buffer[4], head = 0, tail = 0;
long total = 0;
sem_t empty, full;
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
void *producer(void *unused) {
  for (int value = 1; value <= 100; value++) {
    sem_wait(&empty); pthread_mutex_lock(&lock);
    buffer[tail] = value; tail = (tail + 1) % 4;
    pthread_mutex_unlock(&lock); sem_post(&full);
  }
  return unused;
}
void *consumer(void *unused) {
  for (int count = 0; count < 100; count++) {
    sem_wait(&full); pthread_mutex_lock(&lock);
    total += buffer[head]; head = (head + 1) % 4;
    pthread_mutex_unlock(&lock); sem_post(&empty);
  }
  return unused;
}
int main(void) {
  pthread_t first, second;
  sem_init(&empty, 0, 4); sem_init(&full, 0, 0);
  pthread_create(&first, NULL, producer, NULL); pthread_create(&second, NULL, consumer, NULL);
  pthread_join(first, NULL); pthread_join(second, NULL);
  printf("%ld\n", total);
  return 0;
}
