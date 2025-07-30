# AWS Health Checker CLI

A simple command-line interface tool to check the health and availability of AWS services in a specific region using the AWS Health API.

## 📌 Features

- Check AWS service health by region  
- View open and recent AWS Health events  
- Option to filter by service, event status, or time range  
- Lightweight and easy to use  
- Built with Python and Boto3

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- AWS credentials configured via:
  - `~/.aws/credentials`, or
  - Environment variables, or
  - IAM role (if running in AWS)

You also need to enable the **AWS Health API** for your account (part of AWS Business or Enterprise support plans).

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/AnthonyGomez98/aws-health-checker-cli.git
   cd aws-health-checker-cli
Create and activate a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Usage
Basic command:

bash
Copy
Edit
python aws_checker.py
Optional flags:

Flag	Description
--region	Specify AWS region (e.g. us-east-1)
--service	Filter by AWS service (e.g. EC2, S3)
--status	Filter by event status (open, closed)
--days	Limit to events within the last X days

Example:

bash
Copy
Edit
python health_check.py --region us-east-1 --service EC2 --status open --days 3
🛠 Project Structure
bash
Copy
Edit
aws-health-checker-cli/
├── health_check.py        # Main CLI logic
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
✅ Example Output
yaml
Copy
Edit
[✓] Found 2 open events for EC2 in us-east-1

- [Open] EC2 degraded performance in us-east-1
  Start: 2025-07-27 10:32 UTC
  Last Update: 2025-07-27 11:10 UTC
  Event ARN: arn:aws:health:...

- [Open] EC2 instance launch delays in us-east-1
  Start: 2025-07-27 08:00 UTC
  Last Update: 2025-07-27 09:45 UTC
  Event ARN: arn:aws:health:...
🧩 Future Enhancements
Export to JSON/CSV

Email or Slack alerts

Health dashboard view

Unit tests and CI/CD pipeline

📄 License
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