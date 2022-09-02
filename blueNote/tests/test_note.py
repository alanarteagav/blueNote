import unittest

from blueNote.note.note import Note
from blueNote.note.nomenclature import NoteName

class TestNote(unittest.TestCase):

    def setUp(self):
        self.test_note = Note(name=NoteName.A, pitch=4)

    def test_get_name(self):
        self.assertEqual(self.test_note.getName(), 'A', 'getName fail') 

    def test_get_pitch(self):
        self.assertEqual(self.test_note.getPitch(), 4, 'getPitch fail') 

    def test_get_midi_number(self):
        self.assertEqual(self.test_note.getMidiNumber(), 69, 'getMidiNumber fail')

if __name__ == '__main__':
    try:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestNote)
    except:
        pass
    unittest.TextTestRunner(verbosity=2).run(suite)