ARG PYTHON_VERSION=3.12

FROM python:${PYTHON_VERSION}-slim

ARG PDM_VERSION=2.22.2
RUN pip install --no-cache -U pip pdm==${PDM_VERSION}

ARG USERNAME=python_user
ARG USER_UID=1000
ARG USER_GID=${USER_UID}
ENV USER_UID=${USER_UID}
ARG PATH_APP=/home/${USERNAME}/app/bot
ENV PYTHONPATH=$PYTHONPATH:${PATH_APP}
ARG PATH_VENVS=/home/${USERNAME}/.local/share/pdm/venvs
ARG PATH_LOGS=/home/${USERNAME}/logs

RUN groupadd --gid $USER_GID $USERNAME && \
    useradd --uid $USER_UID --gid $USER_GID -m $USERNAME && \
    mkdir -p ${PATH_APP} && \
    mkdir -p ${PATH_VENVS} && \
    mkdir -p ${PATH_LOGS} && \
    chown -R ${USER_UID}:${USER_GID} /home/${USERNAME} && \
    chown -R ${USER_UID}:${USER_GID} ${PATH_APP} && \
    chown -R ${USER_UID}:${USER_GID} ${PATH_VENVS} && \
    chown -R ${USER_UID}:${USER_GID} ${PATH_LOGS} && \
    chsh -s /bin/bash ${USERNAME}

USER ${USERNAME}
