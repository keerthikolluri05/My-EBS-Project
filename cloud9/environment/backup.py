import boto3

# Initialize the EC2 client
ec2 = boto3.client('ec2', region_name='us-east-1')  # Replace with your region

def create_volume_from_snapshot(snapshot_id, availability_zone, volume_type='gp2'):
    response = ec2.create_volume(
        SnapshotId=snapshot_id,
        AvailabilityZone=availability_zone,
        VolumeType=volume_type
    )
    volume_id = response['VolumeId']
    print(f'Volume created from snapshot with ID: {volume_id}')
    return volume_id

def attach_volume(volume_id, instance_id, device_name='/dev/sdb'):
    response = ec2.attach_volume(
        VolumeId=volume_id,
        InstanceId=instance_id,
        Device=device_name
    )
    print(f'Volume {volume_id} attached to instance {instance_id} as {device_name}.')
    return response

# Example usage
snapshot_id = 'snap-0897548edd8eb8b15'  # Replace with your snapshot ID
availability_zone = 'us-east-1c'  # Replace with your desired availability zone
instance_id = 'i-05c8807042644319c'  # Replace with your instance ID

# Create a volume from the snapshot
new_volume_id = create_volume_from_snapshot(snapshot_id, availability_zone)

# Wait for the volume to become available
ec2.get_waiter('volume_available').wait(VolumeIds=[new_volume_id])

# Attach the volume to the instance
attach_volume(new_volume_id, instance_id)
