from aws_cdk import (
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_lambda as _lambda,
    aws_dynamodb as dynamodb,
    aws_sns_subscriptions as subs,
    core
)


class CbsappStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        queue = sqs.Queue(
            self, "CbsappQueue",
            visibility_timeout=core.Duration.seconds(300),
        )

        topic = sns.Topic(
            self, "CbsappTopic"
        )

        table = dynamodb.Table(self, id='dynamoTable',table_name='testcdktable'
                               ,partition_key=dynamodb.Attribute(name='lastname',type=dynamodb.AttributeType.STRING))


        function = _lambda.Function(
            scope         = self,
            id            = 'lambdafunction',
            function_name = '_lambda',
            code          = _lambda.Code.asset('lambdacode'),
            handler       = 'lambdahandler.main',
            runtime       = _lambda.Runtime.PROVIDED,
            memory_size   = 512,
            timeout       = core.Duration.seconds(120)
        )
        topic.add_subscription(subs.SqsSubscription(queue))
