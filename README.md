# idworker
Snowflake idworker

## 1. How does it work?

```python
from idworker import IdWorker


if __name__ == '__main__':
    id_worker = IdWorker(1, 2)
    new_id = id_worker.get_id()
```