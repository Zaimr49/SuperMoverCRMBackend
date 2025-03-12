from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

def generate_random_lead():
    return {
        "tenant": {
            "firstName": fake.first_name(),
            "secondName": fake.last_name(),
            "email": fake.email(),
            "mobile": fake.phone_number(),
        },
        "address": {
            "text": fake.address(),
            "unit": str(random.randint(1, 50)),
            "streetNumber": str(random.randint(1, 500)),
            "streetName": fake.street_name(),
            "locality": fake.city(),
            "postCode": random.randint(1000, 9999),
            "state": fake.state(),
            "city": fake.city(),
            "country": fake.country(),
        },
        "referringAgent": {
            "name": fake.name(),
            "email": fake.email(),
            "partnerCode": fake.uuid4(),
        },
        "referringAgency": {
            "name": fake.company(),
            "email": fake.company_email(),
            "partnerCode": fake.uuid4(),
        },
        "services": {
            "gas": random.choice([True, False]),
            "electricity": random.choice([True, False]),
            "internet": random.choice([True, False]),
            "telephone": random.choice([True, False]),
            "payTV": random.choice([True, False]),
            "cleaning": random.choice([True, False]),
            "removalist": random.choice([True, False]),
            "movingBoxes": random.choice([True, False]),
            "vehicleHire": random.choice([True, False]),
            "water": random.choice([True, False]),
        },
        "submitted": fake.iso8601(),
        "leaseStartDate": (datetime.now() + timedelta(days=random.randint(1, 365))).strftime("%Y-%m-%d"),
        "renewal": random.choice([True, False]),
    }

leads = []
# Generate 5 random leads
random_leads = [generate_random_lead() for _ in range(100)]

# Add to existing leads list
leads.extend(random_leads)

# Print final leads list
import json
print(json.dumps(leads, indent=2))
