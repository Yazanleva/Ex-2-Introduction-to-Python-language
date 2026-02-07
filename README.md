Optional Bonus: Iterator Pipelines (Standard Library)

Why iterator pipelines are more memory-efficient
- Iterator pipelines are more memory-efficient because they process elements one at a time, instead of loading the entire dataset into memory.
- Each step in the pipeline consumes an item, transforms it, and passes it forward immediately.
- This approach avoids creating large intermediate lists, reduces peak memory usage, and allows programs to handle very large or even infinite data streams.
- Because of this, iterator-based pipelines are especially useful in data processing, streaming, and log analysis tasks.
- Iterator pipelines also improve performance by enabling early termination, since processing can stop as soon as a result is found without traversing the entire dataset.
