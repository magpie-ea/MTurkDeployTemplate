import boto3

MTURK_SANDBOX = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'

mturk = boto3.client('mturk',
   region_name='us-east-1',
#   endpoint_url = MTURK_SANDBOX # include this for sandbox mode
)

your_url = "https://babe-project.github.io/MTurkDeployTemplate/index.html" # insert your URL

external_question = """<ExternalQuestion xmlns='http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2006-07-14/ExternalQuestion.xsd'>
  <ExternalURL>""" + your_url + """</ExternalURL>
  <FrameHeight>600</FrameHeight>
</ExternalQuestion>"""

new_hit = mturk.create_hit(
    Title = 'Quick and easy sentence judgements',
    Description = 'Judge whether 10 short sentences are true; very simple and quick but fun study!',
    Keywords = 'linguistics, psychology, truth',
    Reward = '0.5', # how much to pay
    MaxAssignments = 1, # how many participants
    LifetimeInSeconds = 172800, 
    AssignmentDurationInSeconds = 600,
    AutoApprovalDelayInSeconds = 600,
    Question = external_question,
)

print("A new HIT has been created. You can preview it here:")
# print("https://workersandbox.mturk.com/mturk/preview?groupId=" + new_hit['HIT']['HITGroupId']) # comment in for sandbox mode
print("https://worker.mturk.com/mturk/preview?groupId=" + new_hit['HIT']['HITGroupId']) # use this otherwise
print("HITID = " + new_hit['HIT']['HITId'] + " (for your reference)")
