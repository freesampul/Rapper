import os, openai, requests, ffpyplayer

from pydub import AudioSegment

from elevenlabs import clone, generate, play, set_api_key
from elevenlabs.api import History

def pull_lyrics_from_chatgpt(rapper, bar):
    openai.api_key = "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"
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{
            "role": "user",
            "content": "Write a rap song with one intro, one verse, one choruses, and one outro. Make each stanza 5 bars or less. Write it in the style of " + rapper + ". Include the bar: '" + bar + "'. Dont be afraid to get vulgar and outlandish."
        }]
    )
    return completion.choices[0].message.content

def manipulate_lyric_string(lyrics):
    lyrics = lyrics.split("\n\n")
    m_lyrics = "\n"
    for i in range(len(lyrics)):
        lyrics[i] = lyrics[i].split("\n", 1)
        m_lyrics = m_lyrics + lyrics[i][1] + "\n\n"
    return m_lyrics

def export_lyrics_to_mp3(lyrics, voice_id):
    set_api_key("ac0ef1c43902c5b7163ea0a285504a8d")
    audio = generate(
        text = lyrics,
        voice = voice_id,
        model = "eleven_monolingual_v1"
    )
    return audio

def main():
    raw_lyrics = pull_lyrics_from_chatgpt("Kanye West", "I dont care what it look like I'll eat blue waffles for breakfast")
    lyrics = manipulate_lyric_string(raw_lyrics)
    print(lyrics)
    audio = export_lyrics_to_mp3(lyrics, "SnpfyceEOrXnbRjMOh9d")
    with open("outputKanye.mp3", "wb") as file:
        file.write(audio)
    vocals = AudioSegment.from_file("outputKanye.mp3", "mp3")
    beat = AudioSegment.from_file("New_Composition_1.mp3", "mp3")
    combined = vocals.overlay(beat)

    combined.export("combined.mp3", format='mp3')

if '__main__' == __name__:
    main()
