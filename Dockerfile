FROM python:3.8
RUN pip install streamlit
COPY src/app.py /app/
WORKDIR /app
ENTRYPOINT ["streamlit", "run", "app.py"]