import boto3

# Initialize the EC2 client
ec2 = boto3.client('ec2', region_name='us-east-1')  # Replace with your region

def attach_volume(volume_id, instance_id, device_name='/dev/sdb'):
    response = ec2.attach_volume(
        VolumeId=volume_id,
        InstanceId=instance_id,
        Device=device_name
    )
    return response

# Example usage
volume_id = 'vol-03306352f1be28d21'  # Replace with your volume ID
instance_id = 'i-05c8807042644319c'  # Replace with your EC2 instance ID
device_name = '/dev/sdb'  # Replace with the device name

response = attach_volume(volume_id, instance_id, device_name)
print(f'Volume attached: {response}')
