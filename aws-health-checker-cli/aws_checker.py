import boto3
import argparse
from datetime import datetime
from dateutil import parser as date_parser
import json

def create_health_client():
    return boto3.client('health', region_name='us-east-1')

def parse_arguments():
    parser = argparse.ArgumentParser(description="AWS Health Checker CLI")
    parser.add_argument('--region', help='AWS region to filter', required=False)
    parser.add_argument('--service', help='AWS service to filter', required=False)
    parser.add_argument('--start-time', help='Start time (YYYY-MM-DD)', required=True)
    parser.add_argument('--end-time', help='End time (YYYY-MM-DD)', required=True)
    parser.add_argument('--summary', action='store_true', help='Show summary only')
    return parser.parse_args()

def fetch_health_events(client, start_time, end_time, region=None, service=None):
    filters = {
        'startTimes': [{'from': start_time, 'to': end_time}]
    }
    if region:
        filters['regions'] = [region]
    if service:
        filters['services'] = [service]

    response = client.describe_events(filter=filters)
    return response.get('events', [])

def display_events(events, summary=False):
    if summary:
        print(f"\n Summary: {len(events)} event(s) found\n")
        return

    for event in events:
        print(f" [{event['region']}] {event['service']} - {event['eventTypeCode']}")
        print(f"    Status: {event['statusCode']}")
        print(f"    Start:  {event['startTime']}")
        if 'endTime' in event:
            print(f"    End:    {event['endTime']}")
        print("-" * 50)

def main():
    args = parse_arguments()
    client = create_health_client()
    start_time = date_parser.parse(args.start_time)
    end_time = date_parser.parse(args.end_time)

    try:
        events = fetch_health_events(
            client,
            start_time=start_time,
            end_time=end_time,
            region=args.region,
            service=args.service
        )
        display_events(events, summary=args.summary)
    except Exception as e:
        print(f" Error fetching AWS Health events: {e}")

if __name__ == '__main__':
    main()
