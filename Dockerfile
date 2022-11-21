FROM pytorch/pytorch
RUN apt update && apt upgrade -y && apt install ffmpeg -y && apt install git -y
RUN apt install libportaudio2 -y
RUN pip install -U update
RUN pip install pip-compile-multi
RUN pip install git+https://github.com/openai/whisper.git 
WORKDIR workspace
COPY ["requirements.in", "requirements.in"]
RUN pip-compile requirements.in
RUN pip install -r requirements.txt