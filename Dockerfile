FROM debian
RUN apt update && apt dist-upgrade -y
RUN apt install python3 python3-pip git -y
RUN git clone https://github.com/Ashraf-wan/legend-bistro
WORKDIR "legend-bistro"
RUN pip install -r requirements.txt
WORKDIR "legend-bistro/4.0"
EXPOSE "8080"