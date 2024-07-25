import boto3

# Initialize the EC2 client
ec2 = boto3.client('ec2')

def create_volume(size, availability_zone, volume_type='gp2'):
    response = ec2.create_volume(
        Size=size,
        AvailabilityZone=availability_zone,
        VolumeType=volume_type
    )
    return response['VolumeId']

# Example usage
size = 3  # Size in GiB
availability_zone = 'us-east-1c'  # Replace with your desired availability zone
volume_id = create_volume(size, availability_zone)
print(f'Volume created with ID: {volume_id}')
