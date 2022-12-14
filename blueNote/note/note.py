from blueNote.note.nomenclature import NoteName

class Note:

    def __init__(self, name, pitch):
        if not isinstance(name, NoteName):
            raise TypeError('note must be an instance of NoteName Enum')
        self.name = name
        self.pitch = pitch
        self.midiNumber =  self.name.value + 12 * (self.pitch + 1)

    def getName(self):
        match self.name:
            case other:
                return self.name.name

    def getPitch(self):
        return self.pitch

    def getMidiNumber(self) -> int:
        return self.midiNumber
