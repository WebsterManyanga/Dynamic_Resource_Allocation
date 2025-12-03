import heapq

class Process:
    def __init__(self, pid, priority, required_memory, cpu_time):
        self.pid = pid
        self.priority = priority
        self.required_memory = required_memory
        self.cpu_time = cpu_time

    # To allow for heap comparison
    def __lt__(self, other):
        return self.priority > other.priority


class ResourcePool:
    def __init__(self, total_memory):
        self.total_memory = total_memory

        self.allocated_memory = 0

    def allocate(self, process):
        self.allocated_memory += process.required_memory

    def release(self, process):
        self.allocated_memory -= process.required_memory

class Scheduler:
    def __init__(self, resource_pool):
        self.ready_queue = []
        self.waiting_queue = []
        self.resource_pool = resource_pool


    def add_process(self, process):
        heapq.heappush(self.ready_queue, process)

    def dispatch(self):
        if not self.ready_queue:
            return None
        return heapq.heappop(self.ready_queue)

    def run(self):
        while self.ready_queue or self.waiting_queue:
            if not self.ready_queue:
                for p in self.waiting_queue:
                    heapq.heappush(self.ready_queue, p)
                self.waiting_queue.clear()

            current = self.dispatch()
            if self.resource_pool.can_allocate(current):
                self.resource_pool.allocate(current)
                print(f"Running process {current.pid}")
                self.resource_pool.release(current)
            else:
                self.waiting_queue.append(current)


pool = ResourcePool(total_memory=3)
scheduler = Scheduler(pool)

# Sample processes (PID, priority, memory_needed, cpu_time)
processes = [
        Process("P1", priority=1, required_memory=1, cpu_time=4),
        Process("P2", priority=3, required_memory=1, cpu_time=2),
        Process("P3", priority=2, required_memory=2, cpu_time=5),
        Process("P4", priority=5, required_memory=3, cpu_time=1),
        Process("P5", priority=4, required_memory=2, cpu_time=3),
]

# Add processes to scheduler
for process in processes:
    scheduler.add_process(process)

# Run the scheduler
scheduler.run()
