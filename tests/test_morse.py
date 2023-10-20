# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 09:32:32 2023

@author: maggi
"""

MORSE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}


def morse_decoder(code):
    frase = ''
    parole = code.split('   ')
    for el in parole:
        lettere = el.split()
        for let in lettere:
            lettera = MORSE[let]
            frase = frase + lettera
        
        frase = frase + ' '
    frase = frase[:-1]
    return frase.capitalize()

def test_answer():
    assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
    assert (
        morse_decoder("..   .-- .- ...   -... --- .-. -.   .. -.   .---- ----. ----. -----")
        == "I was born in 1990"
    )
