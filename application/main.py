import json
import random

import redis


ONE_MILION_ITERATIONS = 100000
PROBABILITY = 0.5


class ProbabilisticCache:
    """Check if """
    def __init__(self, client, probability):
        self.client = client
        self.probability = probability

    def get(self, key):
        if random.random() < self.probability:
            return self.client.get(key)
        else:
            self.client.delete(key)
            return None

    def set(self, key, value):
        self.client.set(key, value)



def redis_benchmark(client):
    print(f'Put {ONE_MILION_ITERATIONS} keys')
    
    for it in range(ONE_MILION_ITERATIONS):
        client.set(it, it)

    probabilistic_cache = ProbabilisticCache(client, PROBABILITY)
    hit, miss = 0, 0
    for it in range(ONE_MILION_ITERATIONS):
        val = probabilistic_cache.get(it)
        if val:
            hit += 1
        else:
            miss += 1
    print('Total hists:', hit, 'Total miss:', miss)


if __name__ == '__main__':
    print('Start...')
    client = redis.Redis(host='redis_m', port=6379, decode_responses=True)

    # Redis cluster benchmark
    redis_benchmark(client)
