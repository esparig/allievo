"""
Scale selection utilities for music students.
"""

MAJOR_SCALE_INTERVALS = [2, 2, 1, 2, 2, 2, 1]  # Whole and half steps
MINOR_SCALE_INTERVALS = [2, 1, 2, 2, 1, 2, 2]  # Natural minor


class Scale:
    """Represents a musical scale."""
    
    def __init__(self, root_note: str, intervals: list[int]):
        self.root_note = root_note
        self.intervals = intervals
    
    def get_notes(self) -> list[str]:
        """Get all notes in the scale."""
        # This is a simplified example - in a real implementation,
        # you'd handle chromatic notes, accidentals, etc.
        chromatic = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        
        try:
            start_index = chromatic.index(self.root_note)
        except ValueError:
            raise ValueError(f"Invalid root note: {self.root_note}")
        
        notes = [self.root_note]
        current_index = start_index
        
        for interval in self.intervals[:-1]:  # Skip the last interval (octave)
            current_index = (current_index + interval) % 12
            notes.append(chromatic[current_index])
        
        return notes


def get_major_scale(root_note: str) -> Scale:
    """Get a major scale starting from the given root note."""
    return Scale(root_note, MAJOR_SCALE_INTERVALS)


def get_minor_scale(root_note: str) -> Scale:
    """Get a natural minor scale starting from the given root note."""
    return Scale(root_note, MINOR_SCALE_INTERVALS)


def suggest_scale_for_beginner() -> Scale:
    """Suggest a good scale for beginners to start with."""
    return get_major_scale('C')  # C major has no sharps or flats