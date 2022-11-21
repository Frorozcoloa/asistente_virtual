# Asistente virtual.

Este es un proyecto para la creación de un asistente virtual.


## Pasos para e dockerfile

```
docker build -t virtualass .
docker tun --it --rm virtualass bash
```

Recuerda en name_canción, la ruta del archivo de música
```
whisper {{name_canción}}--language Spanish --model base
```