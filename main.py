class Process:
    def __init__(self, pid, priority, required_memory, cpu_time):
        self.pid = pid
        self.priority = priority
        self.required_memory = required_memory
        self.cpu_time = cpu_time


