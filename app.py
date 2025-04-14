import openai
import sys
import pytubefix
import ffmpeg
import os
import subprocess
import whisper
from dotenv import load_dotenv

# --- Entrada da URL ---
url = sys.argv[1]
filename_mp4 = "audio.mp4"
filename_wav = "audio.wav"

# --- Baixa stream do YouTube ---
yt = pytubefix.YouTube(url)
stream = yt.streams.filter(only_audio=True).first()

print("Baixando áudio...")
stream.download(filename=filename_mp4)

# --- Converte para WAV com ffmpeg ---
print("Convertendo para WAV...")
subprocess.run(["ffmpeg", "-i", filename_mp4,
               filename_wav, "-y", "-loglevel", "error"])

if not os.path.exists(filename_wav):
    print(f"Erro: O arquivo {filename_wav} não foi encontrado.")
    sys.exit(1)

# --- Transcreve com Whisper local ---
print("Transcrevendo com Whisper local...")
model = whisper.load_model("base")
result = model.transcribe(filename_wav, language="pt")
transcript = result["text"]

# --- (Opcional) Salva transcrição completa ---
with open("transcricao.txt", "w", encoding="utf-8") as f:
    f.write(transcript)

# --- Gerar resumo com GPT usando OpenAI ---
load_dotenv()
api_key_openai = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key_openai)

print("Gerando resumo com GPT...")
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system",
         "content": """
            Você é um assistente especializado em ajudar os usuários a criar notas detalhadas e completas.
            Você auxilia extraindo as informações principais, 
            organizando-as em pontos estruturados e garantindo que as notas finais sejam abrangentes.
            Sempre resuma as informações de maneira clara e concisa.
            Mantenha o controle dos resultados das ferramentas e incorpore-os às notas conforme necessário.
            O resultado final deve estar em português brasileiro e formatado em Markdown.
        """},
        {"role": "user",
         "content": f"Descreva o seguinte vídeo:\n\n{transcript}"}
    ])

resumo = completion.choices[0].message.content.strip()
with open("resumo.md", "w", encoding="utf-8") as md:
    md.write(resumo)
    print("Resumo salvo com sucesso em resumo.md.")
