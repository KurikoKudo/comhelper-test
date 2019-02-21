# ベースイメージの指定
FROM python:3.6.7

# ソースを置くディレクトリを変数として格納
ARG project_dir=/python_app/comhelper/

# 必要なファイルをローカルからコンテナにコピー
ADD . $project_dir
ADD requirements.txt $project_dir

# requirements.txtに記載されたパッケージをインストール
WORKDIR $project_dir
RUN pip3 install -r requirements.txt

# コミット用のテキストファイルの生成
RUN touch commit.txt

# （コンテナ内で作業する場合）必要なパッケージをインストール
RUN apt-get update
RUN apt-get install bash
RUN apt-get install git
RUN apt-get install tar

# gitの設定
RUN git config --global user.name "comhelper"
RUN git config --global user.email comhelper2018@gmail.com

# hubコマンドのインストール
RUN tar -xvf hub-linux-amd64-2.5.1.tgz
RUN cp hub-linux-amd64-2.5.1/bin/hub /usr/local/bin/

# GitHubのリモートリポジトリのクローン
# RUN git clone https://comhelper:comh2018@github.com/HazeyamaLab/SE18G1.git
# RUN git clone https://comhelper:comh2018@github.com/HazeyamaLab/SE18G2.git
RUN git clone https://comhelper:comh2018@github.com/KurikoKudo/comhelper-test.git

RUN mkdir /python_app/git
RUN mv /python_app/comhelper/comhelper-test /python_app/git

RUN cd /python_app/git/comhelper-test && git checkout -b comhelper
RUN cd /python_app/git/comhelper-test && git push origin comhelper

ENTRYPOINT ["python3","run.py"]
