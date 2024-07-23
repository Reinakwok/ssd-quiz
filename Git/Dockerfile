FROM node:alpine
RUN apk add --no-cache tini git openssh\
&& yarn global add git-http-server \
&& adduser -D -g git git
USER git
WORKDIR /home/git
RUN git init --bare repository.git
RUN mkdir .ssh && chmod 700 .ssh
RUN touch .ssh/authorized_keys && chmod 600 .ssh/authorized_keys
# Copy the entry point script into the container
COPY --chown=git:git ./Entry.sh /home/git/entrypoint.sh
# Set the entry point to the script
ENTRYPOINT ["tini", "--", "/home/git/entrypoint.sh"]
