import re
from typing import Iterable, Set

# Define the ARN regex pattern
ARN_REGEX = r"^arn:[^:]+:[^:]+:[^:]*:(?P<account_id>\d{12}):.+$"

def collect_account_ids_from_arns(arns: Iterable[str]) -> Set[str]:
    """Given several ARNs in the form
        arn:partition:service:region:account-id:resource-id
    Collect the unique account IDs found on those strings, and return them.
    """
    collected_account_ids = set()
    for arn in arns:
        matched = re.match(ARN_REGEX, arn)
        print(matched)
        if matched is not None:
            account_id = matched.groupdict()["account_id"]
            collected_account_ids.add(account_id)
    return collected_account_ids

def collect_account_ids_from_arns1(arns):
    matched_arns = filter(None, (re.match(ARN_REGEX, arn) for arn in arns))
    return {m.groupdict()["account_id"] for m in matched_arns}




# Example ARNs
example_arns = [
    "arn:aws:s3:::123456789012:my-bucket",
    "arn:aws:lambda:us-east-1:987654321098:function:my-function",
    "arn:aws:dynamodb:us-west-2:123456789012:table/my-table",
    "arn:aws:sqs:us-east-1:555555555555:my-queue",
    "arn:aws:s3:::123456789012:another-bucket",
]

# Main execution
if __name__ == "__main__":
    unique_account_ids = collect_account_ids_from_arns(example_arns)
    print("Unique Account IDs:", unique_account_ids)
    unique_account_ids1 = collect_account_ids_from_arns1(example_arns)
    print("Unique Account IDs 1:", unique_account_ids1)
