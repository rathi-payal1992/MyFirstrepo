FROM python:3.10.7-alpine
COPY requirements.txt .
#COPY allianz-ca.crt /usr/local/share/ca-certificates/
RUN pip3 install --upgrade pip
RUN apk add curl bash build-base git ca-certificates openssh-client
#RUN update-ca-certificates
#RUN pip3 install -r requirements.txt
RUN pip install -r ansible
RUN pip install -r ansible-lint==6.8.1
RUN ansible-galaxy collection install cisco.aci
RUN ansible-galaxy collection install cisco.mso
RUN ansible-galaxy collection install cisco.nd
RUN ansible-galaxy collection install cisco.nxos
RUN ansible-galaxy collection install community.vmware
RUN ansible-galaxy collection install community.general
RUN ansible-galaxy collection list
RUN pip3 list
