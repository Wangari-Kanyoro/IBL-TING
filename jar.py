class Jar:

 def __init__(self, capacity=12):
        if capacity < 0 :
              raise ValueError
        self.capacity = capacity 
        self.size = 0
        

def __str__(self):
        return "🍪" * self.size
        

def deposit(self, n):
        if n > self.capacity or  n + self.size > self.capacity:
                raise ValueError
        self.size += n
        

def withdraw(self, n):
        
        if n > self.capacity or  n + self.size > self.capacity:
                raise ValueError
        self.size -= n
@property
def capacity(self):
        return self.capacity
        

@property
def size(self):
       return self.size
        
def main ():
        jar = Jar(4)
        jar.deposit(2)
        jar.withdraw (1)

        print (jar.capacity)
        print (jar.size)


if __name__ == "__main__":
  main()