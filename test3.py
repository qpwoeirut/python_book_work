class Exercise:

    def __init__(self, name, result):
        self.name = name
        self.result = result

    def displayExercise(self):
        print("Exercise:", self.name + ", Result:", self.result)


e1 = Exercise('Juggling', 5)
e2 = Exercise('Left Foot Cone Run', 16.2)
e3 = Exercise('Right Foot Cone Run', 15.4)
e4 = Exercise('Footwork', 'Scissors: 20 Right, 20 Left')
e1.displayExercise()
e2.displayExercise()
e3.displayExercise()
e4.displayExercise()