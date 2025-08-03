# 🩺 AWS Health Checker CLI

A lightweight Python tool that fetches AWS Health events using the AWS Health API, with optional filters by region, service, and time range.

##  Features

- Filter AWS Health events by:
  - Region (e.g., `us-east-1`)
  - Service (e.g., `EC2`)
  - Start/end time
- Optional summary mode for quick event count
- Uses `boto3` and standard Python libraries

##  Example Usage

```bash
# List all EC2 events in us-east-1
python aws_health_checker.py --region us-east-1 --service EC2 --start-time 2025-07-01 --end-time 2025-08-01

# Just show total number of events
python aws_health_checker.py --start-time 2025-07-01 --end-time 2025-08-01 --summary
⚙️ Requirements
Python 3.8+

AWS CLI configured with access to health:DescribeEvents

Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
 Purpose
This project demonstrates:

Practical use of AWS SDK (boto3)

CLI argument parsing with argparse

Working with date filtering, API response parsing, and output formatting

MIT License

Copyright (c) 2025 Anthony Gomez

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell      
copies of the Software, and to permit persons to whom the Software is         
furnished to do so, subject to the following conditions:                       

The above copyright notice and this permission notice shall be included in    
all copies or substantial portions of the Software.                           

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR    
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,      
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE   
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER        
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN     
THE SOFTWARE.