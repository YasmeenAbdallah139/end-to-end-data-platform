from faker import Faker
import random
from datetime import date, timedelta
from tqdm import tqdm

fake = Faker()

NUM_EMPLOYEES = 120000
OUTPUT_FILE = "03_employees.sql"

# ==========================================
# Departments
# ==========================================

departments = {
    1: "Engineering",
    2: "HR",
    3: "Finance",
    4: "Marketing",
    5: "IT",
    6: "Sales",
    7: "Operations",
    8: "Legal",
    9: "Customer Support",
    10: "Research"
}

department_weights = [
    30,  # Engineering
    6,   # HR
    10,  # Finance
    8,   # Marketing
    12,  # IT
    15,  # Sales
    8,   # Operations
    2,   # Legal
    7,   # Customer Support
    2    # Research
]

# ==========================================
# Cities
# ==========================================

cities = {
    1: "Cairo",
    2: "Giza",
    3: "Alexandria",
    4: "Mansoura",
    5: "Tanta",
    6: "Zagazig",
    7: "Aswan",
    8: "Luxor",
    9: "Suez",
    10: "Port Said",
    11: "Ismailia",
    12: "Minya",
    13: "Assiut",
    14: "Damietta",
    15: "Fayoum"
}

city_weights = [
    40,
    20,
    15,
    5,
    3,
    2,
    2,
    2,
    2,
    2,
    1,
    2,
    1,
    1,
    2
]

# ==========================================
# Jobs
# ==========================================

jobs = {

    1: [
        ("Software Engineer", 18000, 24000),
        ("Senior Software Engineer", 25000, 32000),
        ("Tech Lead", 33000, 40000)
    ],

    2: [
        ("HR Specialist", 7000, 11000),
        ("HR Manager", 12000, 17000)
    ],

    3: [
        ("Accountant", 12000, 18000),
        ("Financial Analyst", 18000, 28000)
    ],

    4: [
        ("Marketing Specialist", 9000, 16000),
        ("Marketing Manager", 17000, 23000)
    ],

    5: [
        ("System Administrator", 15000, 22000),
        ("Cloud Engineer", 23000, 30000)
    ],

    6: [
        ("Sales Representative", 8000, 17000),
        ("Sales Manager", 18000, 26000)
    ],

    7: [
        ("Operations Analyst", 10000, 17000),
        ("Operations Manager", 18000, 24000)
    ],

    8: [
        ("Legal Advisor", 18000, 32000)
    ],

    9: [
        ("Support Engineer", 7000, 15000)
    ],

    10: [
        ("Research Scientist", 22000, 40000)
    ]
}

statuses = (
    ["Active"] * 92 +
    ["On Leave"] * 5 +
    ["Resigned"] * 3
)

print("Generating employees...")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:

    f.write("USE source_db;\n\n")

    batch = []
    batch_size = 500

    for emp_id in tqdm(range(1, NUM_EMPLOYEES + 1)):

        # ----------------------------------
        # Department
        # ----------------------------------

        department_id = random.choices(
            population=list(departments.keys()),
            weights=department_weights,
            k=1
        )[0]

        # ----------------------------------
        # City
        # ----------------------------------

        city_id = random.choices(
            population=list(cities.keys()),
            weights=city_weights,
            k=1
        )[0]

        # ----------------------------------
        # Job
        # ----------------------------------

        job_title, salary_min, salary_max = random.choice(
            jobs[department_id]
        )

        salary = random.randint(
            salary_min,
            salary_max
        )

        # ----------------------------------
        # Performance
        # ----------------------------------

        perf_group = random.random()

        if perf_group < 0.05:
            performance = round(random.uniform(2.0, 3.0), 2)
        elif perf_group < 0.85:
            performance = round(random.uniform(3.0, 4.5), 2)
        else:
            performance = round(random.uniform(4.5, 5.0), 2)

        bonus = round(
            salary * (performance / 10),
            2
        )

        # ----------------------------------
        # Gender
        # ----------------------------------

        gender = random.choice(["M", "F"])

        if gender == "M":
            first = fake.first_name_male()
        else:
            first = fake.first_name_female()

        last = fake.last_name()

        # ----------------------------------
        # Age
        # ----------------------------------

        current_year = date.today().year

        age = random.randint(22, 60)

        birth_year = current_year - age

        birth = fake.date_between(
            start_date=date(birth_year, 1, 1),
            end_date=date(birth_year, 12, 31)
        )

        # ----------------------------------
        # Hire Date
        # ----------------------------------

        earliest_hire = birth + timedelta(days=22 * 365)

        if earliest_hire < date(2015, 1, 1):
            earliest_hire = date(2015, 1, 1)

        latest_hire = date(2025, 12, 31)

        if earliest_hire > latest_hire:
            earliest_hire = latest_hire

        hire = fake.date_between(
            start_date=earliest_hire,
            end_date=latest_hire
        )

        status = random.choice(statuses)

        batch.append(
            f"""({emp_id},
'{first}',
'{last}',
'{gender}',
'{birth}',
'{hire}',
{department_id},
{city_id},
'{job_title}',
{salary},
{bonus},
{performance},
'{status}')"""
        )

        if len(batch) == batch_size:

            f.write(
                "INSERT INTO employees "
                "(employee_id,first_name,last_name,gender,birth_date,hire_date,"
                "department_id,city_id,job_title,salary,bonus,"
                "performance_score,employment_status)\nVALUES\n"
            )

            f.write(",\n".join(batch))

            f.write(";\n\n")

            batch.clear()

    if batch:

        f.write(
            "INSERT INTO employees "
            "(employee_id,first_name,last_name,gender,birth_date,hire_date,"
            "department_id,city_id,job_title,salary,bonus,"
            "performance_score,employment_status)\nVALUES\n"
        )

        f.write(",\n".join(batch))

        f.write(";\n")

print(f"\nGenerated {NUM_EMPLOYEES:,} employees.")
print(f"Saved to {OUTPUT_FILE}")