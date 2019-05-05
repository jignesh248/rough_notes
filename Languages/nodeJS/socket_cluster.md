##### https://socketcluster.io/#!/docs/getting-started
- Since worker process are configurable, how many worker process do we need to configure?

- how is socket.publish(event, data) different than socket.emit, note we are not mentioning channel name here
is the event name in this case taken as channel name?

##### https://blog.baasil.io/socketcluster-design-patterns-for-chat-69e76a4b1966


- while subscribing, if we want client to wait for authentication to get approved
```
var roomAChannel = socket.subscribe('room-a', {waitForAuth: true})
```

-  There is a separate middleware line for emit, subscribe, publish in (inbound), publish out (outbound), handshake and
 authenticate actions.

MIDDLEWARE_PUBLISH_IN - usage eg. filter curse words from clients
MIDDLEWARE_PUBLISH_OUT - publish based on filters

```
scServer.addMiddleware(scServer.MIDDLEWARE_PUBLISH_IN,
  function (req, next) {
    if (typeof req.data == 'string') {
      // You can modify req.data to whatever you want
      // and this is what will end up being published after
      // passing through this middleware function.
      req.data = req.data.replace(/hello/g, 'hi');
    }
    next();
  }
);
```

- channels in SC are practically free; when idle, consume no CPU and very little memory (less than few hundred bytes each)

- can potentially have hundreds of thousands of simultaneous unique active channels for each worker process.

- each client can be subscribed for up to 1000 unique channels by default.

- channels are created and destroyed automatically by SC based on client subscriptions

- back end middleware to control who is allowed to subscribe to a channel based on JWTs attached to each socket to 
make fine-grained decisions.

##### SC Channels

-  SC channels automatically scales across multiple worker processes 

- requires configuration to scale across multiple hosts //https://github.com/SocketCluster/socketcluster/blob/master/scc-guide.md //TODO

- for messenger applications create separate channels for each user and so that ack can be send back to the same channel

- Unlike with socket.emit, with pub/sub we do not need to do complex server-side look-ups to figure out which sockets 
belong to which user or group— The client-side subscription itself tells SC where the message needs to end up and SC takes care of the rest.

###### Best Practices

- avoid global state on each worker, if needed use global state in a common store like Redis

- use socket.emit(event, data) for one to one communication between client and server

- socket.publish(event, data) and channel.publish(data) : for many to many communication

- Slightly off-topic: If you're using multiple brokers, each broker will only manage a subset of all available channels 
(this is the secret sauce to SC's scalability), so don't be surprised if you publish() to a broker and no one gets the 
message - You have to call publish() on the broker which is responsible for that particular channel.

##### Architecture

- https://socketcluster.io/#!/docs/basic-usage //TODO : ADD NOTES
##### http://socketcluster.io/#!/docs/middleware-and-authorization //TODO

#### API
- publish to pong channel : 

```
// Server code
scServer.exchange.publish('pong', count);
```

- Subscribe to a channel :

```
// Client code
// New API as of SocketCluster v1.0.0.
var pongChannel = socket.subscribe('pong');

pongChannel.watch(function (count) {
  console.log('Client received data from pong channel:', count);
});

```

- unsubscribe
```
- unsubscribe

```

- publishing to channel from client 
```
socket.publish('pong', 'This PONG event comes from a client');
```

- publish directly to channel object 

```
pongChannel.publish('This PONG event comes from a client');
```

##### Debugging

- --debug-workers and --debug-brokers CLI arguments to let you debug workers and brokers separately

- --inspect-workers and --inspect-brokers to avoid running an external debugger on the side

- node-inspector is not needed for node version 6.3.0+

e.g 
```
node server --inspect-workers
```

```
node server --inspect-brokers
```

- default debug port for the first worker is 5859, the second worker is 5860, ... (it increments by one for each worker)

- debug message get printed to the console telling you which debug ports are open.

- to open debug console in chrome for first worker, open http://127.0.0.1:8080/debug?ws=127.0.0.1:8080&port=5859

- Custom debug ports

With custom starting port for the workers - first port will be assigned to workerCluster master - the process which 
manages SC workers, subsequent workers will +1 increment:

```
// Our workerCluster process will be debuggable on port 5999.
// The first worker will be debuggable on port 6000.
node server --inspect-workers=5999
```

- same thing for borkers
```
// First broker will be debuggable on port 5999.
node server --inspect-brokers=5999
```

- debug master
```
node --inspect server
```

##### Authentication

 - authKey in options to [SocketCluster](https://socketcluster.io/#!/docs/api-socketcluster) constructor 
 
 - if socket on server has valid auth token attached to it (see socket.authToken), then we know that client's token was 
 signed by the server and data that is inside it is therefore valid
 
 - https://socketcluster.io/#!/docs/authentication //TODO
 
 - https://github.com/SocketCluster/socketcluster/issues/233 //TODO
 
 ###### Authentication flow

- Can be over HTTP (before establishing the WebSocket connection) or you can do it after over web-sockets

- Over HTTP :

On the client side, you can pass custom query parameters:
```javascript
socketCluster.connect({query: {someKey: someValue, anotherKey: anotherValue}});

```

^ We can pass the result of a previous HTTP get request as query parameters.
then, from the server-side, you can access those inside the 'connection' handler using something like:
```javascript

var url = require('url'); // The Node.js core url module

// ... then inside the 'connection' handler:

var urlParts = url.parse(socket.request.url, true);
console.log(urlParts.query);
```

- To change the default server auth engine, you can use : worker.setAuthEngine(myCustomServerAuthEngine) http://socketcluster.io/#!/docs/api-scworker

- To change the default client auth engine, you need to pass a custom authEngine option when creating the socket on the client. E.g. socketCluster.connect({authEngine: myCustomClientAuthEngine})

- Note that the server auth engine and the client auth engine are different
  https://github.com/SocketCluster/sc-auth/blob/master/index.js
  https://github.com/SocketCluster/socketcluster-client/blob/master/lib/auth.js
  
- Because HTTP-only cookies cannot be explicitly accessed (saved/loaded) on the client-side, they don't fit into SC's standard authentication flow but you can still authenticate sockets at a lower level during the handshake phase. This ensures that sockets are authenticated before they are connected. It's slightly less flexible but very widely used and suitable for most cases.

When using HTTP-based authentication using cookies, you can read the cookie from the HTTP request that is associated with the WebSocket object on the server-side.

You can use the scServer.MIDDLEWARE_HANDSHAKE_WS to access the HTTP upgrade request (and read any attached cookies) to determine the authentication state of the socket; from that middleware you can either block the connection or attach custom properties to the req object (which you will be able to access later using the socket.request object); so you can do the authentication yourself without relying on SC's JWT authentication mechanism. The main downside to this approach is that the socket's authentication state cannot change throughout the life of a single socket connection; but that limitation is inherent to HTTP cookies - You can just reconnect the socket if you want to use a new cookie.

Alternatively you can use the scServer.MIDDLEWARE_HANDSHAKE_SC middleware; this is the SC-protocol handshake which happens after the native WebSocket (WS) handshake; after the socket has been created; it gives you a bit more flexibility when it comes to sending back things like custom errors.

Also, some apps authenticate by passing a token using a ?token=... query string as part of the HTTP upgrade request URL; this follows the same principle as the cookie approach; and has the same downside that the authentication state cannot change throughout the lifetime of a single socket connection.


https://socketcluster.io/#!/docs/middleware-and-authorization

https://github.com/SocketCluster/socketcluster/issues/42

https://github.com/SocketCluster/socketcluster/blob/master/scc-guide.md

https://github.com/SocketCluster/baasil-cli //TODO

https://github.com/SocketCluster/sc-errors/blob/master/index.js //TODO
 
https://github.com/SocketCluster/socketcluster/issues/245#issuecomment-261041729 //TODO

https://github.com/SocketCluster/socketcluster/issues/245#issuecomment-261041729 //TODO



 