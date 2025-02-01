loan_applications = {
    "App_001": {
        "Applicant": {
            "Age": 28,
            "Salary": 55000,
            "Credit_Score": 720
        },
        "Loan": {
            "Amount": 20000,
            "Rate": 5.5,
            "Term": 5
        },
        "Status": "Pending"
    },
    "App_002": {
        "Applicant": {
            "Age": 45,
            "Salary": 75000,
            "Credit_Score": 680
        },
        "Loan": {
            "Amount": 50000,
            "Rate": 4.2,
            "Term": 15
        },
        "Status": "Pending"
    },
    "App_003": {
        "Applicant": {
            "Age": 35,
            "Salary": 62000,
            "Credit_Score": 690
        },
        "Loan": {
            "Amount": 30000,
            "Rate": 6.0,
            "Term": 10
        },
        "Status": "Pending"
    }
}



if loan_applications["App_001"]["Applicant"]["Credit_Score"] > 700 and loan_applications["App_001"]["Applicant"]["Salary"] >50000:
    print("Loan Approved with Preferred Rate")
else:
    print("Loan Approved with Higher Interest")

if loan_applications["App_002"]["Applicant"]["Credit_Score"] > 700 or loan_applications["App_002"]["Applicant"]["Salary"] >70000:
    print("Eligible for Premium Loan")
else:
    print("Standard Loan Processing")

if loan_applications["App_003"]["Loan"]["Amount"] > 25000 and loan_applications["App_003"]["Loan"]["Rate"] > 5.5:
    print("High-Risk Loan Detected")
else:
    print("Loan Terms are Reasonable")

if loan_applications["App_001"]["Applicant"]["Age"] < 30 and loan_applications["App_001"]["Applicant"]["Credit_Score"] > 700:
    print("Young applicant with strong credit history")
else:
    print("Young applicant with moderate risk")

if loan_applications["App_002"]["Loan"]["Term"] > 10 and loan_applications["App_002"]["Applicant"]["Credit_Score"] < 680:
    print("Long-Term Loan with High Default Risk")
else:
    print("Long-Term Loan with Stable Credit")

if loan_applications["App_003"]["Loan"]["Amount"] > (0.5 * loan_applications["App_003"]["Applicant"]["Salary"]) and loan_applications["App_003"]["Applicant"]["Credit_Score"] < 690:
        print("Loan Amount Too High Compared to Income")
else:
        print("Loan-to-Income Ratio is Acceptable")

if loan_applications["App_001"]["Applicant"]["Credit_Score"] < 650 or loan_applications["App_001"]["Applicant"]["Salary"] < 50000:
    print("High-Risk Applicant")
else:
    print( "Applicant Meets Minimum Criteria")

if loan_applications["App_002"]["Applicant"]["Credit_Score"] > 700 and loan_applications["App_002"]["Loan"]["Amount"] > (0.4 * loan_applications["App_002"]["Applicant"]["Salary"]):
    print("Good Credit but Loan Amount High")

if loan_applications["App_003"]["Loan"]["Rate"] > 6 or loan_applications["App_003"]["Loan"]["Term"] < 5:
        print("Loan May Have High Monthly Payments")

if loan_applications["App_001"]["Applicant"]["Salary"] > 60000 and loan_applications["App_001"]["Applicant"]["Age"] < 35 and loan_applications["App_001"]["Applicant"]["Credit_Score"] > 700:
    print("Highly Eligible Applicant")
else:
    print("Applicant Needs Further Review")


