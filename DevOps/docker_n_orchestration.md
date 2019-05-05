https://eksworkshop.com/

https://stackoverflow.com/questions/24318543/how-to-set-ulimit-file-descriptor-on-docker-container-the-image-tag-is-phusion
https://askubuntu.com/questions/505506/how-to-get-bash-or-ssh-into-a-running-container-in-background-mode
https://docs.docker.com/engine/reference/commandline/commit/

#### CloudTrail

- https://docs.aws.amazon.com/config/latest/developerguide/view-manage-resource-console.html

#### ECS

- https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html
- https://docs.aws.amazon.com/AmazonECS/latest/developerguide/get-set-up-for-amazon-ecs.html
- https://docs.amazonaws.cn/en_us/AmazonECS/latest/developerguide/ecs_services.html

- https://docs.aws.amazon.com/autoscaling/application/userguide/what-is-application-auto-scaling.html
- https://docs.amazonaws.cn/en_us/AmazonECS/latest/developerguide/service-auto-scaling.html
- https://docs.amazonaws.cn/en_us/AmazonECS/latest/developerguide/service-autoscaling-targettracking.html
- https://docs.amazonaws.cn/en_us/AmazonECS/latest/developerguide/service-autoscaling-stepscaling.html

- https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-instance-draining.html 
- https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-strategies.html
- https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html

- https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html
- https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduled_tasks.html

- https://engineering.depop.com/ahead-of-time-scheduling-on-ecs-ec2-d4ef124b1d9e //TODO
- https://garbe.io/blog/2017/04/12/a-better-solution-to-ecs-autoscaling/ //TODO

- https://www.reddit.com/r/aws/comments/7r91ef/best_practices_regarding_ecs_clusters/
 -- ECS doesn't support editing of binpacking once the service is created
 -- A lot of people want to use subnets/security groups on a per task basis. They don't want container X being able to access the RDS of container Y. In November AWS came up with the awsvpc network mode to solve this, but there's still a limitation of ENIs per EC2 host
 
 
##### ECS scaling if load scaling isn't smooth but based on application events.
 
- If scaling up and down isn't smooth but predictable based on time of events scheduled by application, 
use lambda function to change minimum task count on ECS, trigger lambda function 
on some event like dynamoDB record expiration, to increase minimum count of machines needed. 

- Sample the load requirements for various kind of events, and make different categories of 
events, to use it as multiplication factor on existing task count.

- Sampling can also be made dynamic, average of max tasks used for last 5 match for the sport and manual too.
 
- Manual scaling up task count would override auto generated configs based on historical data.

- Should scaling up and down be on absolute number for events or on percentage, I believe percentage will work well.

- https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html



