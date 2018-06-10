import boto3
import sys

if(len(sys.argv) < 2):
    print("Give the HITid as argument")
    sys.exit(-1)

hit_id = sys.argv[1]

mturk = boto3.client('mturk',
   region_name='us-east-1'
)

hit = mturk.get_hit(HITId=hit_id)
print('HIT with ID {} has current status: {}'.format(hit_id, hit['HIT']['HITStatus']))

response = mturk.list_assignments_for_hit(
    HITId=hit_id,
    AssignmentStatuses=['Submitted', 'Approved'],
    MaxResults = 100
)

assignments = response['Assignments']
print('The number of submitted assignments is {}'.format(len(assignments)))

for assignment in assignments:
    assignment_id = assignment['AssignmentId']
    if assignment['AssignmentStatus'] == 'Submitted':
        print ('Approving now: {}'.format(assignment_id))
        mturk.approve_assignment(
            AssignmentId=assignment_id,
            RequesterFeedback='Thank you very much!',
            OverrideRejection=False,
        )
    else:
        print('Already approved: {}'.format(assignment_id))
