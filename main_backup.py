import boto3
import json
import base64

session = boto3.session.Session(
    profile_name="wardaa-admin1"
)

ec2_cli = session.client(
    service_name="ec2",
    region_name="us-east-1"
)

ec2_resource = session.resource(
    service_name="ec2",
    region_name="us-east-1"
)

print("AWS Session Created Successfully")


# Existing VPC

vpc_id = "vpc-05555d0700ed891bb"

print(f"Using existing VPC: {vpc_id}")


# Existing Public Subnets

public_subnet_ids = [
    "subnet-0d23357207f1115ba",
    "subnet-0a506932178ad2310"
]

print("Using existing public subnets")


# Enable auto-assign public IPv4

for subnet_id in public_subnet_ids:

    ec2_cli.modify_subnet_attribute(
        SubnetId=subnet_id,
        MapPublicIpOnLaunch={
            "Value": True
        }
    )

print("Auto-assign Public IPv4 has been enabled for public subnets")
availability_zones = [
    "us-east-1a",
    "us-east-1b"
]


# # 4- Create private subnets
#
# private_subnet_cidrs = [
#     "10.0.100.0/24",
#     "10.0.200.0/24"
# ]
#
# private_subnet_ids = []
#
# for cidr, az in zip(private_subnet_cidrs, availability_zones):
#
#     response = ec2_cli.create_subnet(
#         CidrBlock=cidr,
#         VpcId=vpc_id,
#         AvailabilityZone=az
#     )
#
#     private_subnet_ids.append(
#         response["Subnet"]["SubnetId"]
#     )
#
# print(
#     f"Private Subnets have been created successfully, "
#     f"their ids are {private_subnet_ids[0]} and {private_subnet_ids[1]}"
# )

# Existing Private Subnets

private_subnet_ids = [
    "subnet-0dbee4b8050480ba7",
    "subnet-09f9d059c263361b6"
]

print("Using existing private subnets")

#
# # 5- Create Internet Gateway
#
# igw_response = ec2_cli.create_internet_gateway()
#
 # igw_id = igw_response["InternetGateway"]["InternetGatewayId"]
#
# print(f"Internet Gateway has been created successfully with id {igw_id}")
#
#
# # Attach Internet Gateway to VPC
#
# ec2_cli.attach_internet_gateway(
#     InternetGatewayId=igw_id,
#     VpcId=vpc_id
# )
#
# print(f"Internet Gateway {igw_id} attached to VPC {vpc_id}")
# Find existing Internet Gateway

igw_response = ec2_cli.describe_internet_gateways(
    Filters=[
        {
            "Name": "attachment.vpc-id",
            "Values": [vpc_id]
        }
    ]
)

igw_id = igw_response["InternetGateways"][0]["InternetGatewayId"]

print(f"Using existing Internet Gateway: {igw_id}")
# 6- Create Public Route Table
#
# route_table_response = ec2_cli.create_route_table(
#     VpcId=vpc_id
# )
#
# public_route_table_id = route_table_response["RouteTable"]["RouteTableId"]
#
# print(
#     f"Public Route Table has been created successfully "
#     f"with id {public_route_table_id}"
# )
#
#
# # Add Internet route
#
# ec2_cli.create_route(
#     RouteTableId=public_route_table_id,
#     DestinationCidrBlock="0.0.0.0/0",
#     GatewayId=igw_id
# )
#
# print("Internet route has been added to Public Route Table")
public_route_table_id = "rtb-0c3c4a55ed155d51c"


# 7- Associate Public Route Table with Public Subnets

# for subnet_id in public_subnet_ids:
#
#     ec2_cli.associate_route_table(
#         RouteTableId=public_route_table_id,
#         SubnetId=subnet_id
#     )
#
# print("Public Route Table has been associated with both public subnets")
# 8 - Allocate Elastic IP for NAT Gateway A

# eip_response = ec2_cli.allocate_address(
#     Domain="vpc"
# )
#
# nat_eip_allocation_id = eip_response["AllocationId"]
# nat_eip_public_ip = eip_response["PublicIp"]
#
# print(f"NAT Gateway A Elastic IP: {nat_eip_public_ip}")
# print(f"Allocation ID: {nat_eip_allocation_id}")
# 9 - Create NAT Gateway A

# nat_a_response = ec2_cli.create_nat_gateway(
#     SubnetId="subnet-0d23357207f1115ba",
#     AllocationId="eipalloc-038e8056afc4363ef",
#     ConnectivityType="public"
# )
#
# nat_gateway_a_id = nat_a_response["NatGateway"]["NatGatewayId"]
#
# print(f"NAT Gateway A created: {nat_gateway_a_id}")
# 10 - Check NAT Gateway A status

# nat_status_response = ec2_cli.describe_nat_gateways(
#     NatGatewayIds=["nat-0dda274852a23de39"]
# )
#
# nat_state = nat_status_response["NatGateways"][0]["State"]
#
# print(f"NAT Gateway A status: {nat_state}")
# 11 - Allocate Elastic IP for NAT Gateway B
#
# eip_b_response = ec2_cli.allocate_address(
#     Domain="vpc"
# )
#
# nat_eip_b_allocation_id = eip_b_response["AllocationId"]
# nat_eip_b_public_ip = eip_b_response["PublicIp"]
#
# print(f"NAT Gateway B Elastic IP: {nat_eip_b_public_ip}")
# print(f"Allocation ID: {nat_eip_b_allocation_id}")
# # 12 - Create NAT Gateway B
#
# nat_b_response = ec2_cli.create_nat_gateway(
#     SubnetId="subnet-0a506932178ad2310",
#     AllocationId="eipalloc-01065154312c163dd",
#     ConnectivityType="public"
# )
#
# nat_gateway_b_id = nat_b_response["NatGateway"]["NatGatewayId"]
#
# print(f"NAT Gateway B created: {nat_gateway_b_id}")

# 13 - Check NAT Gateway B status

# nat_b_status_response = ec2_cli.describe_nat_gateways(
#     NatGatewayIds=["nat-0e77f73b45fc4864e"]
# )
#
# nat_b_state = nat_b_status_response["NatGateways"][0]["State"]
#
# print(f"NAT Gateway B status: {nat_b_state}")
# 14 - Create Private Route Table A

# private_rt_a_response = ec2_cli.create_route_table(
#     VpcId=vpc_id
# )
#
# private_rt_a_id = private_rt_a_response["RouteTable"]["RouteTableId"]
#
# print(f"Private Route Table A created: {private_rt_a_id}")
# 16 - Associate Private Subnet A with Private Route Table A

# ec2_cli.associate_route_table(
#     RouteTableId="rtb-00196ab1f4f7a66aa",
#     SubnetId="subnet-0dbee4b8050480ba7"
# )
#
# print("Private Subnet A has been associated with Private Route Table A")
# 17 - Create Private Route Table B

# private_rt_b_response = ec2_cli.create_route_table(
#     VpcId=vpc_id
# )
#
# private_rt_b_id = private_rt_b_response["RouteTable"]["RouteTableId"]
#
# print(f"Private Route Table B created: {private_rt_b_id}")
# 18 - Add NAT Gateway B route to Private Route Table B

# ec2_cli.create_route(
#     RouteTableId="rtb-0b060b210869c1f4c",
#     DestinationCidrBlock="0.0.0.0/0",
#     NatGatewayId="nat-0e77f73b45fc4864e"
# )
#
# print("Private Route Table B now routes internet traffic through NAT Gateway B")

# 19 - Associate Private Subnet B with Private Route Table B

# ec2_cli.associate_route_table(
#     RouteTableId="rtb-0b060b210869c1f4c",
#     SubnetId="subnet-09f9d059c263361b6"
# )
#
# print("Private Subnet B has been associated with Private Route Table B")
# 20 - Create ALB Security Group

# alb_sg_response = ec2_cli.create_security_group(
#     GroupName="ALBSG",
#     Description="Security Group for Application Load Balancer",
#     VpcId=vpc_id
# )
#
alb_sg_id = "sg-0ba1aec971d7606a7"
#
# print(f"ALBSG created: {alb_sg_id}")
# 21 - Allow HTTP traffic to ALB
#
# ec2_cli.authorize_security_group_ingress(
#     GroupId=alb_sg_id,
#     IpPermissions=[
#         {
#             "IpProtocol": "tcp",
#             "FromPort": 80,
#             "ToPort": 80,
#             "IpRanges": [
#                 {
#                     "CidrIp": "0.0.0.0/0"
#                 }
#             ]
#         }
#     ]
# )
#
# print("ALBSG HTTP port 80 rule added")
# 22 - Create Web Server Security Group
#
# web_sg_response = ec2_cli.create_security_group(
#     GroupName="webSG",
#     Description="Security Group for Web Servers",
#     VpcId=vpc_id
# )
#
# web_sg_id = web_sg_response["GroupId"]
#
# print(f"webSG created: {web_sg_id}")
web_sg_id="sg-085f945dbe755e664"
# # 23 - Allow HTTP from ALB to Web Servers
#
# ec2_cli.authorize_security_group_ingress(
#     GroupId=web_sg_id,
#     IpPermissions=[
#         {
#             "IpProtocol": "tcp",
#             "FromPort": 80,
#             "ToPort": 80,
#             "UserIdGroupPairs": [
#                 {
#                     "GroupId": alb_sg_id
#                 }
#             ]
#         }
#     ]
# )
#
# print("webSG HTTP access from ALBSG added")
# 24 - Create Database Security Group
#
# db_sg_response = ec2_cli.create_security_group(
#     GroupName="DBSG",
#     Description="Security Group for RDS Database",
#     VpcId=vpc_id
# )
#
# db_sg_id = db_sg_response["GroupId"]
#
# print(f"DBSG created: {db_sg_id}")
db_sg_id="sg-073bb15879d1e2c3a"

# 25 - Allow MySQL traffic from Web Servers to Database

# ec2_cli.authorize_security_group_ingress(
#     GroupId=db_sg_id,
#     IpPermissions=[
#         {
#             "IpProtocol": "tcp",
#             "FromPort": 3306,
#             "ToPort": 3306,
#             "UserIdGroupPairs": [
#                 {
#                     "GroupId": web_sg_id
#                 }
#             ]
#         }
#     ]
# )
#
# print("DBSG MySQL access from webSG added")
# Existing Security Groups

# alb_sg_id = "sg-0ba1aec971d7606a7"
# web_sg_id = "sg-085f945dbe755e664"
# db_sg_id = "sg-073bb15879d1e2c3a"
#
# print(f"Using ALBSG: {alb_sg_id}")
# print(f"Using webSG: {web_sg_id}")
# print(f"Using DBSG: {db_sg_id}")

# 27 - Create IAM Role for EC2

# iam_cli = session.client(
#     service_name="iam"
# )
#
# assume_role_policy = {
#     "Version": "2012-10-17",
#     "Statement": [
#         {
#             "Effect": "Allow",
#             "Principal": {
#                 "Service": "ec2.amazonaws.com"
#             },
#             "Action": "sts:AssumeRole"
#         }
#     ]
# }
#
# role_response = iam_cli.create_role(
#     RoleName="MyShopEC2Role",
#     AssumeRolePolicyDocument=json.dumps(assume_role_policy),
#     Description="IAM Role for MyShop EC2 instances"
# )
#
# role_arn = role_response["Role"]["Arn"]
#
# print(f"MyShopEC2Role created: {role_arn}")
# IAM Client

iam_cli = session.client(
    service_name="iam"
)
# 28 - Attach SSM policy to EC2 Role

# iam_cli.attach_role_policy(
#     RoleName="MyShopEC2Role",
#     PolicyArn="arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
# )
#
# print("AmazonSSMManagedInstanceCore attached to MyShopEC2Role")
# 29 - Create EC2 Instance Profile

# iam_cli.create_instance_profile(
#     InstanceProfileName="MyShopEC2Profile"
# )
#
# iam_cli.add_role_to_instance_profile(
#     InstanceProfileName="MyShopEC2Profile",
#     RoleName="MyShopEC2Role"
# )
#
# print("MyShopEC2Profile created and MyShopEC2Role added")
# 30 - Get latest Amazon Linux 2023 AMI
#
# ami_response = ec2_cli.describe_images(
#     Owners=["amazon"],
#     Filters=[
#         {
#             "Name": "name",
#             "Values": ["al2023-ami-2023*-x86_64"]
#         },
#         {
#             "Name": "state",
#             "Values": ["available"]
#         },
#         {
#             "Name": "architecture",
#             "Values": ["x86_64"]
#         },
#         {
#             "Name": "root-device-type",
#             "Values": ["ebs"]
#         }
#     ]
# )
#
# latest_ami = sorted(
#     ami_response["Images"],
#     key=lambda x: x["CreationDate"],
#     reverse=True
# )[0]
#
# ami_id = latest_ami["ImageId"]
#
# print(f"Latest Amazon Linux 2023 AMI: {ami_id}")
# 31 - EC2 User Data

user_data = """#!/bin/bash

dnf update -y

dnf install -y httpd

systemctl enable httpd
systemctl start httpd

cat > /var/www/html/index.html <<'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>MyShop</title>
</head>
<body>
    <h1>MyShop Web Server</h1>
    <p>Server is running successfully.</p>
</body>
</html>
EOF
"""

print("EC2 User Data prepared successfully")
ami_id = "ami-048da71c4d98f46b1"

print(f"Using Amazon Linux 2023 AMI: {ami_id}")
# 32 - Create Launch Template

# launch_template_response = ec2_cli.create_launch_template(
#     LaunchTemplateName="MyShopLaunchTemplate",
#     VersionDescription="MyShop web server template",
#     LaunchTemplateData={
#         "ImageId": ami_id,
#
#         "InstanceType": "t3.micro",
#
#         "SecurityGroupIds": [
#             web_sg_id
#         ],
#
#         "IamInstanceProfile": {
#             "Name": "MyShopEC2Profile"
#         },
#
#         "BlockDeviceMappings": [
#             {
#                 "DeviceName": "/dev/xvda",
#                 "Ebs": {
#                     "VolumeSize": 8,
#                     "VolumeType": "gp3",
#                     "Encrypted": True,
#                     "DeleteOnTermination": True
#                 }
#             }
#         ],
#
#         "UserData": base64.b64encode(
#             user_data.encode("utf-8")
#         ).decode("utf-8")
#     }
# )
#
# launch_template_id = launch_template_response[
#     "LaunchTemplate"
# ]["LaunchTemplateId"]
#
# print(f"MyShopLaunchTemplate created: {launch_template_id}")
# ELBv2 Client

elbv2_cli = session.client(
    service_name="elbv2",
    region_name="us-east-1"
)
# 33 - Create Target Group
# ELBv2 Client

elbv2_cli = session.client(
    service_name="elbv2",
    region_name="us-east-1"
)

# 33 - Create Target Group

# target_group_response = elbv2_cli.create_target_group(
#     Name="MyShopWebTG",
#     Protocol="HTTP",
#     Port=80,
#     VpcId=vpc_id,
#     TargetType="instance",
#     HealthCheckProtocol="HTTP",
#     HealthCheckPort="80",
#     HealthCheckPath="/",
#     HealthCheckIntervalSeconds=30,
#     HealthCheckTimeoutSeconds=5,
#     HealthyThresholdCount=2,
#     UnhealthyThresholdCount=3
# )
#
# target_group_arn = target_group_response["TargetGroups"][0]["TargetGroupArn"]
#
# print(f"MyShopWebTG created: {target_group_arn}")
# 34 - Create Application Load Balancer

# 34 - Create Application Load Balancer

# alb_response = elbv2_cli.create_load_balancer(
#     Name="MyShopALB",
#     Subnets=public_subnet_ids,
#     SecurityGroups=[
#         alb_sg_id
#     ],
#     Scheme="internet-facing",
#     Type="application",
#     IpAddressType="ipv4"
# )
#
# alb_arn = alb_response["LoadBalancers"][0]["LoadBalancerArn"]
# alb_dns_name = alb_response["LoadBalancers"][0]["DNSName"]
#
# print(f"MyShopALB created: {alb_arn}")
# print(f"MyShopALB DNS: {alb_dns_name}")

# 35 - Create ALB HTTP Listener
# Existing ALB
alb_arn = "arn:aws:elasticloadbalancing:us-east-1:631412642625:loadbalancer/app/MyShopALB/6d288f4238b06fd7"

print(f"Using existing ALB: {alb_arn}")
# Existing Target Group
target_group_arn = "arn:aws:elasticloadbalancing:us-east-1:631412642625:targetgroup/MyShopWebTG/073741f43666dde0"

print(f"Using existing Target Group: {target_group_arn}")

# 35 - Create ALB HTTP Listener
#
# listener_response = elbv2_cli.create_listener(
#     LoadBalancerArn=alb_arn,
#     Protocol="HTTP",
#     Port=80,
#     DefaultActions=[
#         {
#             "Type": "forward",
#             "TargetGroupArn": target_group_arn
#         }
#     ]
# )
#
# listener_arn = listener_response["Listeners"][0]["ListenerArn"]
#
# print(f"MyShopALB HTTP Listener created: {listener_arn}")
# Auto Scaling Client
autoscaling_cli = session.client(
    service_name="autoscaling",
    region_name="us-east-1"
)

print("Auto Scaling client created successfully")




# 37 - Create Auto Scaling Group
#
# launch_template_id = "lt-07df1450c3061f298"
#
# private_subnet_ids = [
#     "subnet-0dbee4b8050480ba7",
#     "subnet-09f9d059c263361b6"
# ]
#
# asg_response = autoscaling_cli.create_auto_scaling_group(
#     AutoScalingGroupName="MyShopASG",
#
#     LaunchTemplate={
#         "LaunchTemplateId": launch_template_id,
#         "Version": "$Latest"
#     },
#
#     MinSize=2,
#     DesiredCapacity=2,
#     MaxSize=4,
#
#     VPCZoneIdentifier=",".join(private_subnet_ids),
#
#     TargetGroupARNs=[
#         target_group_arn
#     ],
#
#     HealthCheckType="ELB",
#     HealthCheckGracePeriod=300,
#
#     CapacityRebalance=False
# )
#
# print("MyShopASG created successfully")
# 38 - Create Target Tracking Scaling Policy
#
# scaling_policy_response = autoscaling_cli.put_scaling_policy(
#     AutoScalingGroupName="MyShopASG",
#
#     PolicyName="MyShopTargetTrackingPolicy",
#
#     PolicyType="TargetTrackingScaling",
#
#     TargetTrackingConfiguration={
#         "PredefinedMetricSpecification": {
#             "PredefinedMetricType": "ASGAverageCPUUtilization"
#         },
#         "TargetValue": 50.0
#     }
# )
#
# scaling_policy_arn = scaling_policy_response["PolicyARN"]
#
# print(f"MyShop Target Tracking Policy created: {scaling_policy_arn}")
# 39 - Create RDS Client

# rds_cli = session.client(
#     service_name="rds",
#     region_name="us-east-1"
# )
#
# print("RDS client created successfully")
# RDS Client

rds_cli = session.client(
    service_name="rds",
    region_name="us-east-1"
)

print("RDS client created successfully")
#
# # 40 - Create RDS DB Subnet Group
#
# db_subnet_group_response = rds_cli.create_db_subnet_group(
#     DBSubnetGroupName="myshop-db-subnet-group",
#
#     DBSubnetGroupDescription="Private subnet group for MyShop RDS",
#
#     SubnetIds=[
#         "subnet-0dbee4b8050480ba7",
#         "subnet-09f9d059c263361b6"
#     ]
# )
#
# db_subnet_group_name = db_subnet_group_response["DBSubnetGroup"]["DBSubnetGroupName"]
#
# print(f"MyShop DB Subnet Group created: {db_subnet_group_name}")
# 41 - Create RDS MySQL Multi-AZ

# db_identifier = "myshop-db"
#
# db_username = "admin"
# db_password = "MyShop2026Lab#"
# db_response = rds_cli.create_db_instance(
#     DBInstanceIdentifier=db_identifier,
#
#     Engine="mysql",
#     EngineVersion="8.0",
#
#     DBInstanceClass="db.t3.micro",
#
#     AllocatedStorage=20,
#     StorageType="gp3",
#
#     MasterUsername=db_username,
#     MasterUserPassword=db_password,
#
#     DBName="myshop",
#
#     MultiAZ=True,
#
#     PubliclyAccessible=False,
#
#     DBSubnetGroupName="myshop-db-subnet-group",
#
#     VpcSecurityGroupIds=[
#         db_sg_id
#     ],
#
#     BackupRetentionPeriod=1,
#
#     StorageEncrypted=True,
#
#     AutoMinorVersionUpgrade=True,
#
#     Port=3306
# )
#
# print(f"MyShop RDS creation started: {db_identifier}")

# 42 - Check RDS Status
#
# db_status_response = rds_cli.describe_db_instances(
#     DBInstanceIdentifier="myshop-db"
# )
#
# db_instance = db_status_response["DBInstances"][0]
#
# print(f"RDS Status: {db_instance['DBInstanceStatus']}")
# # 43 - Wait for RDS to become available
#
# print("Waiting for RDS to become available...")
#
# rds_waiter = rds_cli.get_waiter("db_instance_available")
#
# rds_waiter.wait(
#     DBInstanceIdentifier="myshop-db"
# )
#
# print("MyShop RDS is now available")
#
# 44 - Check Target Group Health

target_health_response = elbv2_cli.describe_target_health(
    TargetGroupArn=target_group_arn
)

for target in target_health_response["TargetHealthDescriptions"]:
    instance_id = target["Target"]["Id"]
    health_state = target["TargetHealth"]["State"]

    print(f"Instance {instance_id} health: {health_state}")