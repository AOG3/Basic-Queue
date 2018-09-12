










class Queue(object):

    def __init__(self):
        self.queue_data = []

    
    def push(self, data):
        
        self.queue_data.append(data)

    def pop(self):
        
        if self.depth() == 0:
            return None

        return self.queue_data.pop(0)


    def depth(self):
        return len(self.queue_data)



def add_to_queue():
    q = Queue()

    q.push('Hello')
    q.push('World')
    print(q.depth())
    print(q.pop())
    print(q.depth())

def main():
    add_to_queue()

if __name__ == '__main__':
    main()
