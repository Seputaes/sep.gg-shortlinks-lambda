# sep.gg - AWS Lambda Shortlinks

This is a simple script which processes AWS SQS messages in a queue,
and adds any shortlinks sent to a redis database.

This is the AWS lambda counterpart to the sep.gg functionality built
into a Red Discord Bot cog: https://github.com/seputaes/SepRedCogs