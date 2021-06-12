from PyDictionary import PyDictionary
import streamlit as st
from googletrans import Translator, constants
from pprint import pprint

translator = Translator()

dictionary=PyDictionary()
word = st.text_input("please enter your word")
st.write(dictionary.meaning(word))

try:
	if word:
		wantto = st.checkbox('want to change the language?')
except:
	st.write(" ")
try:
	if wantto:
		Lang = st.text_input("please enter the language: ")
		Lang = Lang[0:2]
		if Lang:
			translation = translator.translate(word, dest=Lang)
			st.write(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
except:
	st.write("")
