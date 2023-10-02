#!/usr/bin/env python

class Rotor:
    def __init__(self, seq):
        self.sequence = seq.upper()
        self.position = 0
        self.offsets = []
        if type(seq) != str or len(seq) != 26:
            raise Exception('Sequence needs to be a 26 character string')
        seen = ''
        seq = self.sequence
        for i in range(len(seq)):
            if seen.find(seq[i]) != -1:
                raise Exception(f'Sequence has more than one instance of {seq[i]}')
            index = ord(seq[i]) - 65
            if index < 0 or index > 25:
                raise Exception(f'Invalid sequence character {seq[i]}')
            self.offsets.append(index)
            seen += seq[i]

    def rotateTo(self, letter):
        index = ord(letter.upper()) - 65
        if index < 0 or index > 25:
            raise Exception(f"Can't rotate to {letter}")
        self.position = index

    def increment(self):
        self.position = (self.position + 1) % 26

    def currentLetter(self):
        return chr(self.position + 65)

    def encodeIn(self, index):
        self.increment()
        return self.offsets[(index + self.position) % 26]

    def encodeOut(self, index):
        return self.sequence.find(chr(index + 65))

class Reflector:
    def encodeIn(self, index):
        return 25 - index

class Enigma:

    defaultConfig = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self,
                    rotorConfigs = [defaultConfig, defaultConfig, defaultConfig],
                    startingLetters = ['A', 'A', 'A']):
        self.reflector = Reflector()

        self.rotor1 = Rotor(rotorConfigs[0])
        self.rotor1.rotateTo(startingLetters[0])

        self.rotor2 = Rotor(rotorConfigs[1])
        self.rotor2.rotateTo(startingLetters[1])

        self.rotor3 = Rotor(rotorConfigs[2])
        self.rotor3.rotateTo(startingLetters[2])

    def setTo(self, r1='A', r2='A', r3='A'):
        self.rotor1.rotateTo(r1)
        self.rotor2.rotateTo(r2)
        self.rotor3.rotateTo(r3)

    def reset(self):
        self.setTo()

    def currentSetting(self):
        return f'{self.rotor1.currentLetter()}{self.rotor2.currentLetter()}{self.rotor3.currentLetter()}'

    def run(self, message):
        for i in range(len(message)):
            if message[i] == ' ':
                print()
            else:
                index = ord(message[i].upper()) - 65
                value = self.rotor3.encodeOut(
                    self.rotor2.encodeOut(
                        self.rotor1.encodeOut(
                            self.reflector.encodeIn(
                                self.rotor1.encodeIn(
                                    self.rotor2.encodeIn(
                                        self.rotor3.encodeIn(
                                            index)))))))
                print(f'{chr(value + 65)}\t{self.currentSetting()}')