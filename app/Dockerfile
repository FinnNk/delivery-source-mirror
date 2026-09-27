FROM python:3.13.7-alpine3.22@sha256:9ba6d8cbebf0fb6546ae71f2a1c14f6ffd2fdab83af7fa5669734ef30ad48844
WORKDIR /app
COPY app.py index.html test_app.py ./
RUN python -m unittest -v
USER 1000
EXPOSE 8080
CMD ["python", "app.py"]
