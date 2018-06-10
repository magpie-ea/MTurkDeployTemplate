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

## ToDo:
## - print a warning when no.of assignments is =100 because it is not clear whether this is true or due to the fact that we can maximally get 100 results before Pagination_Stuff kicks in (sort out how that would work)
## - list the number of assignments with different statuses in a nicely formatted table
