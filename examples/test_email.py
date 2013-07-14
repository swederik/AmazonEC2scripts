"""
This file is an example of how to run a nipype pipeline on EC2.

The time module is used to send the running time of the pipeline.
An email is sent to the desired address when the pipeline is finished.

The email contains information on the instance so you know which one
to check
"""

"""
Import required functions and packages
"""
from ec2stuff.email_when_fin import send_email
from ec2stuff.ec2 import grab_metadata
import time

"""
Start the clock and get the current time
"""
start = time.strftime("%d-%m-%Y %H:%M:%S")
tic = time.clock()

"""
You should put your pipeline here and give it a name
"""
pipeline_name = "Example"

blah = 1 + 1
recipients = ["erik.ziegler@ulg.ac.be"]

"""
Stop the clock
"""
end = time.strftime("%d-%m-%Y %H:%M:%S")
toc = time.clock()
elapsed = toc - tic

"""
"""


block_text = grab_metadata()

msg_subject = pipeline_name + " completed"
msg_text =  "Started : " + start + "\n"
msg_text += "Finished : " + end + "\n"
msg_text += "Elapsed : " + str(elapsed) + "\n"
msg_text += "\n"
msg_text += block_text + "\n"

send_email(TO=recipients,SUBJECT=msg_subject, TEXT=msg_text)