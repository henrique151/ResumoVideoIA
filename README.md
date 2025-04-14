## Sobre o projeto:
 
Este projeto automatiza o processo de transcrição e resumo de vídeos do YouTube, utilizando inteligência artificial de ponta.

A aplicação funciona da seguinte forma:

1) Entrada de URL do YouTube: o usuário fornece o link de um vídeo diretamente pelo terminal.
2) Extração do áudio: o áudio é baixado usando pytubefix e convertido para .wav com ffmpeg.
3) Transcrição com Whisper (OpenAI): o áudio é transcrito localmente, com suporte ao idioma português.
4) Resumo com ChatGPT: o conteúdo transcrito é enviado para a API da OpenAI, que gera um resumo estruturado e formatado em Markdown.
5) Exportação: a transcrição é salva em transcricao.txt e o resumo final em resumo.md.

## Tecnologias utilizadas:

- Python

## Como utilizar esse projeto de maneira local:

#### Pré requisitos:

- Ter o Python instalado
- Ter o FFmpeg instalado e configurado no sistema
- Criar um arquivo .env na raiz do projeto com a seguinte variável:
  
```bash
  OPENAI_API_KEY="sua-chave-da-openai"
```

### Passo a passo

Clone o repositório:
```bash
  git clone https://github.com/henrique151/ResumoVideoIA
```

Acesse o diretório do projeto:
```bash
  cd ResumoVideoIA
```

Instale as dependências:
```bash
  pip install openai pytubefix git+https://github.com/openai/whisper.git python-dotenv
```

Execute a aplicação:
```bash
  python app.py <link-do-video>
```
