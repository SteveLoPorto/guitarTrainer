import random





class Score():
    def __init__(self):
        self.correct = 0
        self.incorrect = 0
        self.total = 0

class GameController():

    def __init__(self, trials, difficulty, strings, scoreVar, noteVar, stringVar, octaveVar, sharpVar):
        self.trials = trials
        self.difficulty = difficulty
        self.strings = strings
        self.current_trial = 0
        self.score = Score()
        self.scoreVar = scoreVar
        self.noteVar = noteVar
        self.stringVar = stringVar
        self.octaveVar = octaveVar
        self.sharpVar = sharpVar

        
        
    def get_note_list(self):

        strings = self.strings
        note_list = []
        for string in strings:
            string.upper()
            starting_note = notes.index(string, 0, 11)
            for i in range(0, 22):
                note_list.append(notes[(starting_note + i) % 12])

    def get_trials(self):
        return self.trials
    
    def get_current_trial(self):
        return self.current_trial
    
    def get_score(self):
        return self.score


    def generate_note(self):
        pass


    def check_answer(self, answer):
        pass
    
    def start_game(self):
        pass
        
class Guitar():
    def __init__(self):
        self.strings = []
        self.get_strings()
    
    def get_strings(self):
        string_names_starting_note = [('E', 'E'), ('A', 'A'), ('D', 'D'), ('G', 'G'), ('B', 'B'), ('e', 'E')]
        for currString in string_names_starting_note:
            self.strings.append(GuitarString(currString[0], currString[1]))

    def print_fretboard(self):
        for string in self.strings:
            print(f"{string.notes[0]}, {string.notes[1]}")


    
class GuitarString():
    def __init__(self, name, starting_note):
        self.name = name
        self.starting_note = starting_note
        self.first_octave_notes = []
        self.second_octave_notes = []
        self.notes = [self.first_octave_notes, self.second_octave_notes]
        self.get_notes()
    
    def get_notes(self):
        notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
        starting_note_index = notes.index(self.starting_note)
        for i in range(0, 12):
            self.first_octave_notes.append(notes[(starting_note_index + i) % 12])
        for i in range(0, 12):
            self.second_octave_notes.append(notes[(starting_note_index + i) % 12])
