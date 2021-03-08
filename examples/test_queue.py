import multiprocessing

def impl(queue, len) : 
    a = 1
    for i in range(1000000) : 
        a *= a  

    if queue is not None : 
        queue.put([len])
    else : 
        return None 

class Agent(object) : 
    def __init__(self, len, num_threads) : 
        self.len = len 
        self.num_threads = num_threads

    def impl(self, test_mode) : 
        print("Now is", test_mode)
        queue = multiprocessing.Queue()
        workers = []

        for i in range(self.num_threads - 1) : 
            args = (queue, self.len)
            workers.append(multiprocessing.Process(target=impl, args=args))

        impl(None, 10) 

        for worker in workers : 
            worker.start()

        for _ in workers : 
            len = queue.get()

if __name__ == "__main__" : 
    agent = Agent(2, 2) 
    agent.impl(True)
    agent.impl(False)
<<<<<<< HEAD
=======

>>>>>>> f6d5f833a77c9bbc6fdf4ee3ed5223f82fd1aa01
