import boto3

# Initialize the EC2 client
ec2 = boto3.client('ec2', region_name='us-east-1')  # Replace with your region

def create_snapshot(volume_id, description='My snapshot'):
    response = ec2.create_snapshot(
        VolumeId=volume_id,
        Description=description
    )
    return response['SnapshotId']

# Example usage
volume_id = 'vol-03306352f1be28d21'  # Replace with your volume ID
snapshot_id = create_snapshot(volume_id)
print(f'Snapshot created with ID: {snapshot_id}')
