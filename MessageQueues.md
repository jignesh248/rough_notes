### AWS SQS

* SQS is distributed queuing system

* poll or pull message from Queues

* messages are processed independently (with message-level ack/fail semantics). Does not have to maintain a persistent checkpoint/cursor

* Supports persistent message with Message Retention Period: min 60secs, max: 14 days

* Default Visibility Timeout : If is set too low, duplicates can occur. Visibility timeout is the time from where you fetch the message, do nothing with it and it becomes visible in the queue again.

* Supports individual message delay for visibility

* Duplication : If you have multiple servers working against the same queue you have to handle duplicates. They will occur due to race conditions. To handle duplicates use Redis KV paid while consuming to avoid consuming duplicates.
 
* Use batch to insert and fetch : Amazon SQS is a service where you pay for each request and the bandwidth you use. To save cost you should try to send messages as batches of 10 messages. Bandwidth cost will remain same but requests cost will fall.

* Scales well horizontally : SQS queues seems to scale well as long as given time to heat up. They’re probably using auto scaling groups behind the scenes.  

* Same Messages can't be received by multiple receivers at the same time 
  
##### Pros
* Easy to get started.
* Easy to use.
* No manual maintenance.
* Good SDKs.
* Very good monitoring via Amazon Cloudwatch or an external tools such as DataDog.

##### Cons
* AWS can be overwhelming.
* Duplicate messages can occur.
* Expensive if traffic is huge.

### AWS SNS 

* distributed publish-subscribe system : Messages are pushed to subscribers as and when they are sent by publishers to SNS

* If you want unknown number and type of subscribers to receive messages, use SNS.

### AWS Kinesis Data Streams

* The throughput of an Amazon Kinesis data stream is designed to scale without limits via increasing the number of shards within a data stream

1 shard = 1 MBPS input speed, 2MBPS output speed, max 1000 puts/second

1 record : has sequence number, partition key, and data blob. Maximum size of data blob (data payload before Base64-encoding) is 1 MB.

partition key decides which shard the record goes in

* continuously processing the data, 
    1. to transform the data before emitting to a data store, 
    2. run real-time metrics and analytics, or
    3. derive more complex data streams for further processing
 
    
* eg use case.
    1. Accelerated log and data feed intake
    2. Real-time metrics and reporting
    3. Real-time data analytics : click-streams
    4. Complex stream processing: one or more Amazon Kinesis Applications can add data to another Amazon Kinesis data stream for further processing, enabling successive stages of stream processing.
    
#### Use Case Considerations 

- Multiple Kinesis Data Streams applications can consume data from a stream

- provides ordering of records

- supports read and/or replay records in same order to multiple Amazon Kinesis Applications

- Amazon Kinesis Client Library (KCL) delivers/routes all records for a given partition key to the same record processor
(as in streaming MapReduce), makes counting, aggregation, and filtering of records for the same partition-key easier

- scale up to a sufficient number of shards (note : need to provision enough shards ahead of time)

- Consumers can use enhanced fan-out for sub-200ms data delivery speeds between producers and consumers( average 70ms, ~65% faster delivery compared to GetRecords API) which subscribes Kinesis Streams over HTTP2
 
- Integrates well with Apache Storm using Amazon Kinesis Storm Spout

- Workers can be scaled if using KCL using ASG

- Scaling up or down takes few minutes

- UpdateShardCount doesn't need downtime

- only perform one resharding operation at a time

 For a data stream with 1 shard, it takes few seconds to double the throughput by splitting one shard
 
 For a data stream with 1000 shards, it takes 30K seconds (8.3 hours) to double the throughput by splitting 1000 shards. We recommend increasing the throughput of your data stream ahead of the time when extra throughput is needed

- 99.9 uptime SLA

#### Limitation

* default retention period 24 hrs, max retention period 7 days

* maximum size of a data blob (data payload before Base64-encoding) within one record is 1 megabyte (MB).

* Each shard can support up to 1000 PUT records per second. 

* Amazon Kinesis Agent currently only supports Amazon Linux or Red Hat Enterprise Linux. 

* Shard iterator can return empty results

* ApproximateArrivalTimestamp are probably prone to clock drifts as everything else in the world and can be out of order. 

#### Pricing 
 
- all stream-level metrics are free of charge, all enabled shard-level metrics are charged at Amazon CloudWatch Pricing.

- charged on multiples of 25KB PUT request, if payloads are small use put requests, as probably 1 KB payload will also be charged for 25KB if put request is used.

- When extended data retention is enabled, you pay the extended retention rate for each shard in your stream.

- Tracking data of Kinesis Application is stored in DynamoDB which incurs extra cost

- additional charges for Fanout : hourly charge and data retrieval cost/GB

    
#### Further reading :

* https://aws.amazon.com/kinesis/data-streams/faqs/
