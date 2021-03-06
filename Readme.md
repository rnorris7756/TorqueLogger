# Torque Logger

I use the [Torque app](https://play.google.com/store/apps/details?id=org.prowl.torque&hl=en_US) to collect diagnostic information from my car as I'm driving.
Rather than have my data sent to the default server owned by the app author, I've opted to use the built-in custom URL feature to send the data to my own machine.

To do this, I have a very simple python web application built using [Falcon](https://github.com/falconry/falcon) that takes any request with valid URL parameters and shoves a JSON constructed from these parameters into a MongoDB collection.

There's no analysis or pretty charts.  No web interface, and minimal security.  I just wanted to start building a collection of my own driving data until I reach a point in time when I'm not too lazy to do so.

Naturally, it's all hosted in Docker, and I've included the dockerfile as well as a docker-compose file.
If you feel like copying this project to do something, please see [license.txt](license.txt) and remember that zero work went into security/stability, so use this at your own risk.

To run this project, you'll need docker-compose.  The setup process should look something like this:

```
git clone https://github.com/rnorris7756/TorqueLogger.git
cd TorqueLogger
cp mongo.env.sample mongo.env
cp torque.env.sample torque.env
# Change the password to something better than 'password' <- Actual important step
vim mongo.env # You can use another editor if you really want to.  Who am I to judge?
vim torque.env
docker-compose up -d
```

Things to keep in mind:
- You should have port 30000 open (you can change the port in `docker-compose.yml`)
- You need to configure the custom logging URL in the torque app (this is somewhere in the logging settings)
