import os, openai, requests, ffpyplayer

from elevenlabs import clone, generate, play, set_api_key
from elevenlabs.api import History

def pull_lyrics_from_chatgpt(rapper, bar):
    openai.api_key = "s"
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{
            "role": "user",
            "content": "Write a 3 line rap "
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
    set_api_key("s")
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
    print(audio)
    play(audio)

if '__main__' == __name__:
    main()
