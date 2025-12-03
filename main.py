class Process:
    def __init__(self, pid, priority, required_memory, cpu_time):
        self.pid = pid
        self.priority = priority
        self.required_memory = required_memory
        self.cpu_time = cpu_time


class ResourcePool:
    def __init__(self, total_memory):
        self.total_memory = total_memory

        self.allocated_memory = 0

    def allocate(self, process):
        self.allocated_memory += process.required_memory

    def release(self, process):
        self.allocated_memory -= process.required_memory

