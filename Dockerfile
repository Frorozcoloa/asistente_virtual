FROM pytorch/pytorch
RUN apt update && apt upgrade -y && apt install ffmpeg -y && apt install git -y
RUN pip install -U update
RUN pip install git+https://github.com/openai/whisper.git 
