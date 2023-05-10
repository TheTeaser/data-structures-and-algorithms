from .Queue import Queue

class AnimalShelter:
    def __init__(self):
        self.queue_cats = Queue()
        self.queue_dogs = Queue()

    def enqueue(self, animal):
        '''
        This function adds the animal to the end of the queue following FIFO principle.
        '''
        if animal["species"] == "cat":
            self.queue_cats.enqueue(animal)
        elif animal["species"] == "dog":
            self.queue_dogs.enqueue(animal)
        else:
            raise ValueError("Invalid species!")

    def dequeue(self, specie):
        '''
        This function removes a value based on the given specie from the queue's front.
        '''
        if specie == "cat":
            if not self.queue_cats.is_Empty():
                return self.queue_cats.dequeue()
            else:
                return "No cats in the queue"
        elif specie == "dog":
            if not self.queue_dogs.is_Empty():
                return self.queue_dogs.dequeue()
            else:
                return "No dogs in the queue"
        else:
            raise ValueError("Invalid!")
        

shelter = AnimalShelter()
animal1 = {
    "species" : "cat", "name" : "Whiskers"
}

animal2 = {
    "species" : "cat", "name" : "Garfield"
}

animal3 = {
    "species" : "dog" , "name" : "Bolt"
}

animal4 = {
    "species" : "dog" , "name" : "Netanyahu"
}

shelter.enqueue(animal1)
shelter.enqueue(animal2)
shelter.enqueue(animal3)
shelter.enqueue(animal4)
