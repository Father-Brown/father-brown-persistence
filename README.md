[![Gitter chat](https://badges.gitter.im/father-brown/persistence/gitter.png)](https://gitter.im/father-brown/persistence/)

# Father Brown Persistence

## Overview

## Requirements
Python 3.5.2+

Before run the project it is nessesary run docker Ne4j container

```
docker run \
    --publish=7474:7474 --publish=7687:7687 \
    --volume=$HOME/neo4j/data:/data \
    --volume=$HOME/neo4j/logs:/logs \
    neo4j:3.0

```
## Usage
## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t father-brown-persistence .

# starting up a container
docker run father-brown-persistence
