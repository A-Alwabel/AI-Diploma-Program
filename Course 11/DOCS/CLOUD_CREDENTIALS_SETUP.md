# Cloud Credentials Setup Guide
## AIAT 125 — Unit 3: Cloud Deployment

> **For students:** Before running the cloud example notebooks (`02_aws_sagemaker`, `03_azure_ml_deployment`, `04_gcp_vertex_ai`), you need a free cloud account. This guide shows you exactly how to create one and connect it to the notebooks.

---

## Which Notebooks Need Credentials

| Notebook | Platform | What You Need |
|---|---|---|
| `02_aws_sagemaker.ipynb` | AWS | AWS Access Key ID + Secret Access Key |
| `03_azure_ml_deployment.ipynb` | Azure | Subscription ID + Service Principal |
| `04_gcp_vertex_ai.ipynb` | GCP | Service Account JSON key file |
| `01_cloud_deployment.ipynb` | Concept only | No credentials needed |
| `05_security_measures.ipynb` | Concept only | No credentials needed |
| `06_monitoring_logging_cloud.ipynb` | Concept only | No credentials needed |

---

## Option A — AWS Free Tier

**Cost:** Free for 12 months (750 hrs/month EC2 t2.micro, SageMaker Studio free tier)

### Step 1: Create Account
1. Go to **https://aws.amazon.com/free**
2. Click **"Create a Free Account"**
3. Enter your email and choose an account name
4. Enter a credit card (required for verification — you will NOT be charged if you stay in free tier)
5. Complete phone verification
6. Choose **"Basic support — Free"**

### Step 2: Create IAM Access Keys
1. Sign in to the AWS Console at **https://console.aws.amazon.com**
2. Click your account name (top right) → **"Security credentials"**
3. Scroll to **"Access keys"** → click **"Create access key"**
4. Choose **"Local code"** → click Next → Create
5. **Download the `.csv` file** — you cannot see the secret key again after this screen

### Step 3: Set Up Credentials in the Notebook
At the top of `02_aws_sagemaker.ipynb`, run this cell:

```python
import os
os.environ["AWS_ACCESS_KEY_ID"]     = "AKIA..."        # from the CSV
os.environ["AWS_SECRET_ACCESS_KEY"] = "your-secret"    # from the CSV
os.environ["AWS_DEFAULT_REGION"]    = "us-east-1"
```

Or create a file `~/.aws/credentials` with:
```
[default]
aws_access_key_id = AKIA...
aws_secret_access_key = your-secret
region = us-east-1
```

---

## Option B — Azure Free Account

**Cost:** $200 credit for 30 days + 12 months of free services

### Step 1: Create Account
1. Go to **https://azure.microsoft.com/free**
2. Click **"Start free"**
3. Sign in with a Microsoft account (or create one)
4. Enter a credit card for verification
5. Complete phone verification

### Step 2: Get Your Subscription ID
1. Go to **https://portal.azure.com**
2. Search for **"Subscriptions"** in the top search bar
3. Click your subscription → copy the **Subscription ID** (looks like `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`)

### Step 3: Create a Service Principal
In the Azure Cloud Shell (click `>_` icon in portal), run:

```bash
az ad sp create-for-rbac --name "aiat125-student" --role contributor \
    --scopes /subscriptions/YOUR_SUBSCRIPTION_ID
```

This outputs:
```json
{
  "appId": "...",       ← this is AZURE_CLIENT_ID
  "password": "...",    ← this is AZURE_CLIENT_SECRET
  "tenant": "..."       ← this is AZURE_TENANT_ID
}
```

### Step 4: Set Up Credentials in the Notebook
```python
import os
os.environ["AZURE_SUBSCRIPTION_ID"] = "your-subscription-id"
os.environ["AZURE_CLIENT_ID"]       = "appId from above"
os.environ["AZURE_CLIENT_SECRET"]   = "password from above"
os.environ["AZURE_TENANT_ID"]       = "tenant from above"
```

---

## Option C — Google Cloud Free Trial

**Cost:** $300 credit for 90 days

### Step 1: Create Account
1. Go to **https://cloud.google.com/free**
2. Click **"Get started for free"**
3. Sign in with a Google account
4. Enter billing info (credit card required — you will NOT be auto-charged after the trial)
5. Select your country → Accept terms → **"Start my free trial"**

### Step 2: Create a Project
1. Go to **https://console.cloud.google.com**
2. Click the project dropdown (top left) → **"New Project"**
3. Name it `aiat125-deployment` → Create

### Step 3: Enable the Vertex AI API
1. In the Cloud Console search bar, type **"Vertex AI API"**
2. Click **"Enable"**

### Step 4: Create a Service Account Key
1. Go to **IAM & Admin → Service Accounts**
2. Click **"Create Service Account"**
3. Name: `aiat125-student` → click **"Create and Continue"**
4. Role: **"Vertex AI User"** → Continue → Done
5. Click the service account you just created
6. Go to **"Keys"** tab → **"Add Key"** → **"Create new key"** → JSON → Create
7. A `.json` file downloads automatically — keep it safe

### Step 5: Set Up Credentials in the Notebook
```python
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/path/to/your-key.json"
os.environ["GOOGLE_CLOUD_PROJECT"]           = "aiat125-deployment"
```

---

## Important: Keep Credentials Safe

- **Never commit credentials to Git** — they are like passwords
- Never share your access keys in screenshots or messages
- When you finish the course, delete the IAM user (AWS), service principal (Azure), or service account key (GCP)
- All three platforms let you set spending alerts — do this as soon as you create your account

### Set a Spending Alert (Recommended)
- **AWS:** Billing → Budgets → Create budget → set $5 alert
- **Azure:** Cost Management → Budgets → set $10 alert  
- **GCP:** Billing → Budgets & alerts → set $10 alert

---

## No Credit Card? Use These Alternatives

| Option | Details |
|---|---|
| AWS Educate | Free for students — no credit card: **https://aws.amazon.com/education/awseducate** |
| Azure for Students | $100 free credit with `.edu` email — no credit card: **https://azure.microsoft.com/free/students** |
| Google for Students | Apply via your institution or use $300 trial |

---

## Quick Test: Verify Your Credentials Work

After setting up, run this in a notebook cell to confirm before starting the labs:

```python
# AWS
import boto3
sts = boto3.client("sts")
print("AWS identity:", sts.get_caller_identity()["Arn"])

# Azure
from azure.identity import ClientSecretCredential
cred = ClientSecretCredential(
    os.environ["AZURE_TENANT_ID"],
    os.environ["AZURE_CLIENT_ID"],
    os.environ["AZURE_CLIENT_SECRET"]
)
token = cred.get_token("https://management.azure.com/.default")
print("Azure token obtained:", bool(token.token))

# GCP
from google.cloud import aiplatform
aiplatform.init(project=os.environ["GOOGLE_CLOUD_PROJECT"], location="us-central1")
print("GCP initialized successfully")
```
