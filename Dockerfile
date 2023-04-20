FROM debian
RUN apt update && apt dist-upgrade -y
RUN apt install python3 python3-pip git -y
RUN git clone https://github.com/Ashraf-wan/Legend-Bistro
WORKDIR "Legend-Bistro"
RUN pip install -r requirements.txt
WORKDIR "Legend-Bistro/main"
EXPOSE "5000"
