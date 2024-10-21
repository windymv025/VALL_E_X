top_md = """
# VALL-E X  
VALL-E X can synthesize high-quality personalized speech with only a 3-second enrolled recording of 
an unseen speaker as an acoustic prompt, even in another language for a monolingual speaker.<br>
This implementation supports zero-shot, mono-lingual/cross-lingual text-to-speech functionality of three languages (English, Chinese, Japanese)<br>  
See this [demo](https://plachtaa.github.io/) page for more details.
"""

infer_from_audio_md = """
Upload a speech of 3~10 seconds as the audio prompt and type in the text you'd like to synthesize.<br>
The model will synthesize speech of given text with the same voice of your audio prompt.<br>
The model also tends to preserve the emotion & acoustic environment of your given speech.<br>
For faster inference, please use **"Make prompt"** to get a `.npz` file as the encoded audio prompt, and use it by **"Infer from prompt"**
"""

make_prompt_md = """
Upload a speech of 3~10 seconds as the audio prompt.<br>
Get a `.npz` file as the encoded audio prompt. Use it by **"Infer with prompt"**
"""

infer_from_prompt_md = """
Faster than **"Infer from audio"**.<br>
You need to **"Make prompt"** first, and upload the encoded prompt (a `.npz` file)
"""

long_text_md = """
Very long text is chunked into several sentences, and each sentence is synthesized separately.<br>
Please make a prompt or use a preset prompt to infer long text.
"""

long_text_example = "Speech processing is a field in computer science and artificial intelligence that involves the analysis, processing, and understanding of human spoken language. The main goal of speech processing is to enable computers to recognize, analyze, and respond to human speech in a natural and efficient manner."