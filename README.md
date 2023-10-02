![](enigma.png)

Some Python fun in the spirit of the German wartime [Enigma machine](https://en.wikipedia.org/wiki/Enigma_machine).

```python
>>> from enigma import *
>>>
>>> e=Enigma() # can optionally set a three-element array of a-z rotor mappings and/or starting letters
>>>
>>> e.setTo('r','x','g')
>>>
>>> e.run('here is a test')
V       SYH
V       TZI
F       UAJ
P       VBK

I       WCL
V       XDM

K       YEN

O       ZFO
A       AGP
J       BHQ
F       CIR
>>> e.currentSetting()
'CIR'
>>> e.setTo('r','x','g') # to decrypt, use the same starting letters (and implicitly here, the same rotors)
>>> e.run('vvfp iv k oajf')
H       SYH
E       TZI
R       UAJ
E       VBK

I       WCL
S       XDM

A       YEN

T       ZFO
E       AGP
S       BHQ
T       CIR
```