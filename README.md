# Air Pressure System Fault Detection


### Step 1 - Install the requirements

```bash
pip install -r requirements.txt
```

### Step 2 - Run main.py file

```bash
python main.py
```

### Problem Statement:
```
The Air Pressure System (APS) is a critical component of a heavy-duty vehicle that uses compressed air to force a piston to provide pressure to the brake pads, slowing the vehicle down. The benefits of using an APS instead of a hydraulic system are the easy availability and long-term sustainability of natural air.

This is a Binary Classification problem, in which the affirmative class indicates that the failure was caused by a certain component of the APS, while the negative class indicates that the failure was caused by something else.

Solution Proposed
In this project, the system in focus is the Air Pressure system (APS) which generates pressurized air that are utilized in various functions in a truck, such as braking and gear changes. The datasets positive class corresponds to component failures for a specific component of the APS system. The negative class corresponds to trucks with failures for components not related to the APS system.

The problem is to reduce the cost due to unnecessary repairs. So it is required to minimize the false predictions (positives).
```
```
We can get the real-time data (streamed data) through the sensors or IOT devices that are embedded in the vehicles.
```
```
Kafka will be used to get that streaming data from vehicles. Vehicles will send the data in real time to the Kafka Cluster (Server) and then Kafka will send that data to our Database in Mongo DB. Kafka is horizontally scalable, capable to receiving and delivering data requests to any number of devices.
```
```
Why are we using Kafka? Can't we directly dump data into our MongoDB Database??
Search for this: Might create a performance issue in the MongoDB Server
```