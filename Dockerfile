FROM ubuntu:22.04
WORKDIR .
COPY main.py ./main.py
COPY credentials.json ./credentials.json
COPY s2dr3-20231220.1-cp310-cp310-linux_x86_64.whl ./s2dr3-20231220.1-cp310-cp310-linux_x86_64.whl

RUN apt-get update \
    && apt-get install -y python3-pip \
    && apt-get install -y python3-dev \
    && apt-get install -y gdal-bin \
    && apt-get install -y libgdal-dev \
    && apt-get install -y g++ \
    && export CPLUS_INCLUDE_PATH=/usr/include/gdal \
    && export C_INCLUDE_PATH=/usr/include/gdal

RUN pip install s2dr3-20231220.1-cp310-cp310-linux_x86_64.whl

RUN pip install uvicorn fastapi
RUN pip install --upgrade google-cloud-storage

RUN pip install s2dr3-20231220.1-cp310-cp310-linux_x86_64.whl
RUN gdalinfo --version
RUN python3 -c "from osgeo import gdal; print(gdal.__version__)"

EXPOSE 8080
ENTRYPOINT [ "python3", "main.py" ]