# HSA12
Redis Cluster 

This example provides redis claster for caching purposes built with 2 containers `master` (`redis-m`), `replica` (`redis-r`) and `sentinel`(`redis-s`)


### Max memory policy

In `redis.conf` for master node defined `maxmemory` and `maxmemory-policy` whic defines total size and eviction
stategy for case when max memory limit reached


### Probabilistic Cache

Python script in `application` folder push 100,000 keys in redis and than try to get them using probability of cache `0.5`

Execution example:

```
hsa12_test     | Start...
hsa12_test     | Put 100000 keys
hsa12_test     | Total hists: 49040 Total miss: 50960
```
