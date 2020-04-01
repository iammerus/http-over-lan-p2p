## What is this

Soooo. This thing is basically simple PoC of HTTP working over nodes on a peer to peer network. With the whole information sharing thing as a cherry on top

## Technology Stack

- Python 3.7
- 
- Flask (Web Framework)
- Elasticsearch

## Goals

Basically each node in the Peer To Peer network should expose an HTTP app (read the WEB.md file to understand the goals of the web app) through which other peers will communicate with said node through.

## 1. Explicit Goals

### A P2P infrastructure

Obviously we need some peer-to-peer infrastructure. Since this project is a PoC, we can save ourselves the stress of figuring out how to setup a P2P network over the internet and instead try and set it up within a local network space

#### How it works

So in a nutshell what we're going to do is this.

1. We're going to have peers connected to the same network. This is for the sake of the presentation of our PoC. They
need to be on the same network.
2. Since they are on the same network each peer's client (which is this app) will scan the network for other devices
connected to the same network (Refer to Discovering Network Devices section below for detail).
And try to test if those devices are part of the P2P network. Since not necessarily every device will be part of our
network. (Refer to Identifying Peers section below).
3. Once a peer is identified. We'll cache the peer's IP Address. We'll then add them to a local database of peers which
we will use the next time a peer needs to send information to other peers.



##### Discovering network devices

So this needs a bit of low level networking but this is as low as we'll go.

Honestly, I have no idea of how we're going to do this because, this system needs to be platform independent. Because of
that, I was thinking of following the following steps:

- We first get a list of all network interfaces on the current device our program is running on
- Once we have the list. We'll iterate through the interfaces and try to get the IP Address of the network's primary gateway.
- We'll then send an ARP packet to the gateway to try and get the devices on the network

Tbth, I don't want to do this. Working directly with sockets gave me nightmares in the past. This is just so we know
what's needed. If we can find a package that does that then that's preferred.



##### Identifying Peers

This is pretty simple. Each peer will expose a port where other peers can 'ping'. Basically, we send an HTTP response to
the pingback port and if we get a response we expect then hat device is a peer.

For example, let's say we have IP address 192.168.1.XX and we want to find out if that device is a peer. We'll just
send an HTTP request to the pingback port on the device, let's say port 8004 as an example, and if we get an expected
response, we'll know that that device is a peer and store their IP for later use.




----
### 2. A pretty simple HTTP server.

We'll need to write a simple HTTP server, well, not write write. Using the default http server code built into python,
we just modify a few things to suit our needs.


#### What should it do?

So we have to HTTP servers. The one for pingbacks and one for the actual information interchange

1. Pingback HTTP Server
 
 So this HTTP server will host a simple script that basically, exposes a port that when accessed will return a JSON string with some data (we'll decide what that data is later)

2. Main HTTP Server

This part is a little tricky now, because this main HTTP server needs to host a full blown web app (which is the actual API that will handle information interchange) 

I was thinking, to make our lives easier, the main HTTP server will just be a reverse proxy to an actual LAMPP stack that will host the actual web app. This will ensure that the main server code has nothing to do with information interchange app and that they can be worked on independantly and concurrently

And that's basically the HTTP server side of things.



## Ports Index

- Port 5800 - Pingback
- Port 5805 - Main HTTP Server Port
- Port 5810 - Application HTTP Server

---
---
## Conclusion
 All in all I think that there's not a lot of complex work. Just one or two challenges to kind of figure out. So once you're done with this, let me know what you think. Change what needs changing then we'll finally start working with a clear road map of what needs to be done