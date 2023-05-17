class Node:
    def __init__(self, customer):
        self.customer = customer
        self.next = None

class Customers_Queue:
    def __init__(self, customer):
        new_node = Node(customer)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp != None and self.length <= 5:
            print(temp.customer)
            temp = temp.next
        if self.length >= 5:
            print("====Full Queue====")

    def enqueue(self, customer):
        new_node = Node(customer)
        if self.first == None:
            self.first = new_node
            self.last = new_node
        elif self.length <= 4:
            self.last.next = new_node
            self.last = new_node
            self.length += 1
        else:
            None

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp

# Menambahkan antrian pelanggan pertama / menginisiasi pelanggan pertama
print('\nFirst Queue\n|Cashier|\n|_______|')
my_queue = Customers_Queue("    𖨆")
my_queue.print_queue()

# Menambahkan pelanggan kedua dan ketiga
print('\nEnqueue 2 Customers\n|Cashier|\n|_______|')
my_queue.enqueue("    𐀪")
my_queue.enqueue("    웃")
my_queue.print_queue()

# Menyelesaikan antrian 2 pelanggan pertama
print('\nDequeue 2 Customers\n|Cashier|\n|_______|')
my_queue.dequeue()
my_queue.dequeue()
my_queue.print_queue()

# Menambahkan 5 pelanggan
print('\nEnqueue 5 Customers\n|Cashier|\n|_______|')
my_queue.enqueue("    ጸ")
my_queue.enqueue("   🚶")
my_queue.enqueue("    𐀪")
my_queue.enqueue("    웃")
my_queue.enqueue("    🧑‍🤝‍🧑")
my_queue.print_queue()

print("")