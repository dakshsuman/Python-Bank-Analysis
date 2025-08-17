import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import plotly.express as px 
from datetime import datetime
today = datetime.today()
df = pd.read_excel("C:/Users/Daksh/Desktop/dakshpy/bankloananalysis/financial_loan.xlsx")
print(df.head())
print(df.describe())
print(df.info())
print(df.shape)
print(df.dtypes)

total_loan_application= df['id'].count()
print(total_loan_application, "total_loan_application")


#MTD total Loan Applications
latest_issued_date = df['issue_date'].max()
latest_year = latest_issued_date.year
latest_month = latest_issued_date.month
mtd_data = df[(df['issue_date'].dt.year == latest_year) & (df['issue_date'].dt.month == latest_month)]
mtd_loan_application = mtd_data['id'].count()
print(f"MTD Loan Application (for {latest_issued_date.strftime('%B %Y')}):{mtd_loan_application}")


#Total Funded Amount
total_funded_amount=df['loan_amount'].sum()/1000000
print("total_funded_amount: ${:.2f}M".format(total_funded_amount))

#MTD total Funded Amount
latest_issued_date = df['issue_date'].max()
latest_year = latest_issued_date.year
latest_month = latest_issued_date.month
mtd_date = df[(df['issue_date']. dt.year == latest_year) & (df['issue_date'].dt.month == latest_month)]
mtd_funded_amount= mtd_date['loan_amount'].sum()/1000000
print("mtd_funded_amount: ${:.2f}M".format(mtd_funded_amount))

#Total Amount Received

total_amount_received = df['total_payment'].sum()/1000000
print("total_amount_received: ${: .2f}M" .format(total_amount_received))

#MTD total Amount Received
latest_issued_date = df['issue_date'].max()
latest_year = latest_issued_date.year
latest_month = latest_issued_date.month
mtd_date = df[(df['issue_date']. dt.year == latest_year) & (df['issue_date'].dt.month == latest_month)]
mtd_amount_recevied = mtd_date['total_payment'].sum()/1000000
print("mtd_amount_recevied: ${:.2f}M".format(mtd_amount_recevied))

#Average intrest Rate
avg_intrest = df['int_rate'].mean()*100
print("Average Intrest:{: .2f}%" .format(avg_intrest))

#Average Debt-to-Income Ratio
avg_dti = df['dti'].mean()*100
print("Average DTI :{:.2f}%" .format(avg_dti))

#Good loans 
good_loan = df[df['loan_status'].isin(["Fully Paid", "Current"])]
no_of_good_loan= good_loan['id'].count()
print("no_of_good_loan", no_of_good_loan)
good_loan_fund= good_loan['loan_amount'].sum()/1000000
print("good Loan fund:${: .2f}M" .format(good_loan_fund))
good_loan_amount= good_loan['total_payment'].sum()/1000000
print("good Loan amount:${: .2f}M" .format(good_loan_amount))
pct_good_loan = no_of_good_loan/total_loan_application*100
print("pct_good_loan: {:.2f}%".format(pct_good_loan))


#bad loans 
bad_loan = df[df['loan_status'].isin(["Charged Off"])]
no_of_bad_loan= bad_loan['id'].count()
print("no_of_bad_loan", no_of_bad_loan)
bad_loan_fund= bad_loan['loan_amount'].sum()/1000000
print("bad Loan fund:${: .2f}M" .format(bad_loan_fund))
bad_loan_amount= bad_loan['total_payment'].sum()/1000000
print("bad Loan amount:${: .2f}M" .format(bad_loan_amount))
pct_bad_loan = no_of_bad_loan/total_loan_application*100
print("pct_bad_loan: {:.2f}%".format(pct_bad_loan))


#Portfolio Default Rate
total_application = df['id'].count
defaul_rate= no_of_bad_loan/total_loan_application*100
print("Portfolio default rate = {:.2f}%".format(defaul_rate))

#Average Time to Repayment
average_time_repayment= (df['issue_date']-df['last_payment_date']).dt.days
mean_repayment= average_time_repayment.mean()
print("average time to repay {:.0f}Days".format(mean_repayment))


#Segmented Loss Rate (by grade, state, home ownership, purpose, term, verification sts, intrest rate, loan amount)
#grade
charge_off = df['loan_status'].isin(["Charged Off"]) 
charge_off_grade = df.groupby('grade')['loan_amount'].sum().sort_values()
plt.barh(charge_off_grade.index, charge_off_grade.values, color='blue')
plt.xlabel('Charged-Off Loan Amount')
plt.ylabel('grade')
plt.title('Charged-Off Loan Amount by grade')
plt.grid(axis='x')
plt.tight_layout()
plt.show()


#state

charge_off_state = df.groupby('address_state')['loan_amount'].sum().sort_values()
plt.figure(figsize=(8, 5))
plt.barh(charge_off_state.index, charge_off_state.values, color='blue')
plt.xlabel('Charged-Off Loan Amount')
plt.ylabel('state')
plt.title('Charged-Off Loan Amount by state')
plt.grid(axis='x')
plt.tight_layout()
plt.show()


#home ownership

charge_off_home_ownership = df.groupby('home_ownership')['loan_amount'].sum().sort_values()
plt.figure(figsize=(8, 5))
plt.barh(charge_off_home_ownership.index, charge_off_home_ownership.values, color='blue')
plt.xlabel('Charged-Off Loan Amount')
plt.ylabel('Home ownership')
plt.title('Charged-Off Loan Amount by Home ownership')
plt.grid(axis='x')
plt.tight_layout()
plt.show()

#purpose
charge_off_purpose = df.groupby('purpose')['loan_amount'].sum().sort_values()
plt.figure(figsize=(8, 5))
plt.barh(charge_off_purpose.index, charge_off_purpose.values, color='blue')
plt.xlabel('Charged-Off Loan Amount')
plt.ylabel('Purpose')
plt.title('Charged-Off Loan Amount by Purpose')
plt.grid(axis='x')
plt.tight_layout()
plt.show()

#term
charge_off_term = df.groupby('term')['loan_amount'].sum().sort_values()
plt.figure(figsize=(8, 5))
plt.barh(charge_off_term.index, charge_off_term.values, color='blue')
plt.xlabel('Charged-Off Loan Amount')
plt.ylabel('term')
plt.title('Charged-Off Loan Amount by term')
plt.grid(axis='x')
plt.tight_layout()
plt.show()

verification sts
charge_off_vfs = df.groupby('verification_status')['loan_amount'].sum().sort_values()
plt.figure(figsize=(8, 5))
plt.barh(charge_off_vfs.index, charge_off_vfs.values, color='blue')
plt.xlabel('Charged-Off Loan Amount')
plt.ylabel('#verification sts')
plt.title('Charged-Off Loan Amount by #verification sts')
plt.grid(axis='x')
plt.tight_layout()
plt.show()

#intrest rate
charge_off_int_rate = df.groupby('int_rate')['loan_amount'].sum().sort_values()
plt.figure(figsize=(8, 5))
plt.bar(charge_off_int_rate.index, charge_off_int_rate.values, color='blue')
plt.xlabel('Charged-Off Loan Amount')
plt.ylabel('int_rate')
plt.title('Charged-Off Loan Amount by int_rate')
plt.grid(axis='y')
plt.tight_layout()
plt.show()

charge_off = df[df['loan_status'] == 'Charged Off']

charge_off_int_rate = charge_off.groupby('int_rate')['loan_amount'].sum().sort_index()

plt.figure(figsize=(12, 6))
plt.bar(charge_off_int_rate.index, charge_off_int_rate.values, color='blue')
plt.xlabel('Interest Rate')
plt.ylabel('Charged-Off Loan Amount')
plt.title('Charged-Off Loan Amount by Interest Rate')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y')
plt.tight_layout()
plt.show()

#Portfolio Yield
portfolio_yield= total_funded_amount/total_funded_amount
print("Portfolio Yield = {:.2f}%".format(portfolio_yield *100))

# Weighted Average Loan Age
df['issue_date'] = pd.to_datetime(df['issue_date'], format='%d-%m-%Y')
today = datetime.today()
df['loan_age_days'] = (today - df['issue_date']).dt.days
weighted_avg_age_days = (df['loan_age_days'] * df['loan_amount']).sum() / df['loan_amount'].sum()
weighted_avg_age_years = weighted_avg_age_days / 365

print("Weighted Average Loan Age (days) {:.0f} Days".format(weighted_avg_age_days))
print("Weighted Average Loan Age (years) {:.0f} Years".format(weighted_avg_age_years))


 #Monthly trends by issue data for total funded amount 
monthly_funded= (df.sort_values('issue_date').assign(month_name=lambda x: x['issue_date'].dt.strftime('%b %Y')).groupby('month_name', sort=False)
                 ['loan_amount'].sum().div(1000000).reset_index(name='loan_amount_millions'))

plt.figure(figsize=(10,5))
plt.fill_between(monthly_funded['month_name'], monthly_funded['loan_amount_millions'], color='skyblue', alpha=0.5)
plt.plot(monthly_funded['month_name'], monthly_funded['loan_amount_millions'], color='blue', linewidth=2)
for i, row in monthly_funded.iterrows():
    plt.text(i, row['loan_amount_millions'] + 0.1, f"{row['loan_amount_millions']:.2f}",
             ha='center', va='bottom', fontsize=9, rotation=0, color='black')
    
plt.title('Total Funded Amount by Month', fontsize=14)
plt.xlabel('Month')
plt.ylabel('Funded Amount ( $ millions)')
plt.xticks(ticks=range(len(monthly_funded)), labels= monthly_funded['month_name'], rotation=45)
plt.grid(True, linestyle= '--', alpha=0.6)
plt.tight_layout
plt.show()

 #Monthly trends by issue data for total  amount recevied
monthly_recevied= (df.sort_values('issue_date').assign(month_name=lambda x: x['issue_date'].dt.strftime('%b %Y')).groupby('month_name', sort=False)
                 ['total_payment'].sum().div(1000000).reset_index(name='recevied_amount_millions'))

plt.figure(figsize=(10,5))
plt.fill_between(monthly_recevied['month_name'], monthly_recevied['recevied_amount_millions'], color='skyblue', alpha=0.5)
plt.plot(monthly_recevied['month_name'], monthly_recevied['recevied_amount_millions'], color='blue', linewidth=2)
for i, row in monthly_recevied.iterrows():
    plt.text(i, row['recevied_amount_millions'] + 0.1, f"{row['recevied_amount_millions']:.2f}",
             ha='center', va='bottom', fontsize=9, rotation=0, color='black')
    
plt.title('Total Recevied Amount by Month', fontsize=14)
plt.xlabel('Month')
plt.ylabel('Recevied Amount ( $ millions)')
plt.xticks(ticks=range(len(monthly_funded)), labels= monthly_recevied['month_name'], rotation=45)
plt.grid(True, linestyle= '--', alpha=0.6)
plt.tight_layout
plt.show()


 #Monthly trends by issue data for total loan application
total_application= (df.sort_values('issue_date').assign(month_name=lambda x: x['issue_date'].dt.strftime('%b %Y')).groupby('month_name', sort=False)
                 ['id'].count().reset_index(name='total_loan_application'))

plt.figure(figsize=(10,5))
plt.fill_between(total_application['month_name'], total_application['total_loan_application'], color='skyblue', alpha=0.5)
plt.plot(total_application['month_name'], total_application['total_loan_application'], color='blue', linewidth=2)
for i, row in total_application.iterrows():
    plt.text(i, row['total_loan_application'] + 0.5, f"{row['total_loan_application']:.2f}",
             ha='center', va='bottom', fontsize=9, rotation=0, color='black')
    
plt.title('Total Recevied Amount by Month', fontsize=14)
plt.xlabel('Month')
plt.ylabel('Recevied Amount ( $ millions)')
plt.xticks(ticks=range(len(monthly_funded)), labels= total_application['month_name'], rotation=45)
plt.grid(True, linestyle= '--', alpha=0.6)
plt.tight_layout
plt.show()

#Regional Analysis by State for total funded amount 

state_funding = df.groupby('address_state')['loan_amount'].sum().sort_values(ascending=True)
state_funding_thousands= state_funding/1000

plt.figure(figsize=(10,8))
bars=plt.barh(state_funding_thousands.index, state_funding_thousands.values, color='blue')

for bar in bars:
    width= bar.get_width()
    plt.text(width + 10, bar.get_y() + bar.get_height()/2,
             f'{width:,.0f}k', va='center', fontsize=9)
plt.title('Total fund amount by state in  thousands')
plt.xlabel('state')
plt.tight_layout
plt.show()

#Regional Analysis by State for total amount recevied 

state_amount = df.groupby('address_state')['total_payment'].sum().sort_values(ascending=True)
state_amount_thousands= state_amount/1000

plt.figure(figsize=(10,8))
bars=plt.barh(state_amount_thousands.index, state_amount_thousands.values, color='blue')

for bar in bars:
    width= bar.get_width()
    plt.text(width + 10, bar.get_y() + bar.get_height()/2,
             f'{width:,.0f}k', va='center', fontsize=9)
plt.title('Total recevied amount by state in  thousands')
plt.xlabel('state')
plt.tight_layout
plt.show()

#Regional Analysis by State for application

state_application = df.groupby('address_state')['id'].count().sort_values(ascending=True)
state_applicationt_thousands= state_amount/1000

plt.figure(figsize=(10,8))
bars=plt.barh(state_applicationt_thousands.index, state_applicationt_thousands.values, color='blue')

for bar in bars:
    width= bar.get_width()
    plt.text(width + 10, bar.get_y() + bar.get_height()/2,
             f'{width:,.0f}k', va='center', fontsize=9)
plt.title('Total application by state in  thousands')
plt.xlabel('state')
plt.tight_layout
plt.show()

#Loan Term Analysis by total funded amount 
term_funding_millions= df.groupby('term')['loan_amount'].sum()/1000000
plt.figure(figsize=(5,5))
plt.pie(term_funding_millions, labels=term_funding_millions.index, autopct=lambda p: f"{p:.1f}%\n${p*sum(term_funding_millions)/100:.1f}M",startangle=99,wedgeprops={'width': 0.4})
plt.gca().add_artist(plt.Circle((0,0), 0.70,color= 'white'))
plt.title("total Funded Amount by Term")
plt.show()

#Loan Term Analysis by total Recevied amount 
term_recevied_millions= df.groupby('term')['total_payment'].sum()/1000000
plt.figure(figsize=(5,5))
plt.pie(term_recevied_millions, labels=term_recevied_millions.index, autopct=lambda p: f"{p:.1f}%\n${p*sum(term_recevied_millions)/100:.1f}M",startangle=99,wedgeprops={'width': 0.4})
plt.gca().add_artist(plt.Circle((0,0), 0.70,color= 'white'))
plt.title("total Recevied Amount by Term")
plt.show()

#Loan Term Analysis by total application
term_application_thousands= df.groupby('term')['id'].count()/1000
plt.figure(figsize=(5,5))
plt.pie(term_application_thousands, labels=term_application_thousands.index, autopct=lambda p: f"{p:.1f}\n${p*sum(term_application_thousands)/100:.1f}k",startangle=99,wedgeprops={'width': 0.4})
plt.gca().add_artist(plt.Circle((0,0), 0.70,color= 'white'))
plt.title("Total Application by Term in thousands")
plt.show()


Employee Length Analysis by funded amount 
emp_funding_thousands= df.groupby('emp_length')['loan_amount'].sum().sort_values()/1000
bars = plt.barh(emp_funding_thousands.index, emp_funding_thousands, color='blue')
for bar in bars:
    width= bar.get_width()
    plt.text(width + 10, bar.get_y() + bar.get_height()/2,
             f'{width:,.0f}k', va='center', fontsize=9)
plt.title('Total funded amount by employe length thousands')
plt.xlabel('Funded amount in thousands')
plt.grid(linestyle='--', alpha=0.35)
plt.tight_layout()
plt.show()

#Employee Length Analysis by recevied amount 
emp_recevied_thousands= df.groupby('emp_length')['total_payment'].sum().sort_values()/1000
bars = plt.barh(emp_recevied_thousands.index, emp_recevied_thousands, color='blue')
for bar in bars:
    width= bar.get_width()
    plt.text(width + 10, bar.get_y() + bar.get_height()/2,
             f'{width:,.0f}k', va='center', fontsize=9)
plt.title('Total Recevied amount by employe length thousands')
plt.xlabel('Funded Recevied in thousands')
plt.grid(linestyle='--', alpha=0.35)
plt.tight_layout()
plt.show()

Employee Length Analysis by application
emp_application= df.groupby('emp_length')['id'].count().sort_values()
bars = plt.barh(emp_application.index, emp_application, color='blue')
for bar in bars:
    width= bar.get_width()
    plt.text(width + 10, bar.get_y() + bar.get_height()/2,
             f'{width:,.0f}k', va='center', fontsize=9)
plt.title('Application by employe length thousands')
plt.xlabel('Application')
plt.grid(linestyle='--', alpha=0.35)
plt.tight_layout()
plt.show()


#Loan Purpose by funded amount 
loan_purpose_funded= df.groupby('purpose')['loan_amount'].sum().sort_values()/1000000
bars = plt.barh(loan_purpose_funded.index, loan_purpose_funded, color='blue')
for bar in bars:
    width= bar.get_width()
    plt.text(width + 10, bar.get_y() + bar.get_height()/2,
             f'{width:,.2f}M', va='center', fontsize=9)
plt.title('#Loan Purpose by funded amount in mill')
plt.xlabel('Purpose')
plt.grid(linestyle='--', alpha=0.35)
plt.tight_layout()
plt.show()

#Loan Purpose by recevied amount 
loan_purpose_recevied= df.groupby('purpose')['total_payment'].sum().sort_values()/1000000
bars = plt.barh(loan_purpose_recevied.index, loan_purpose_recevied, color='blue')
for bar in bars:
    width= bar.get_width()
    plt.text(width + 10, bar.get_y() + bar.get_height()/2,
             f'{width:,.2f}M', va='center', fontsize=9)
plt.title('Loan Purpose by recevied amount in Millions ')
plt.xlabel('Purpose')
plt.grid(linestyle='--', alpha=0.35)
plt.tight_layout()
plt.show()

#Loan Purpose by Application 
loan_purpose_application= df.groupby('purpose')['id'].count().sort_values()
bars = plt.barh(loan_purpose_application.index, loan_purpose_application, color='blue')
for bar in bars:
    width= bar.get_width()
    plt.text(width + 10, bar.get_y() + bar.get_height()/2,
             f'{width:,.2f}', va='center', fontsize=9)
plt.title('Loan Purpose by rApplication ')
plt.xlabel('Purpose')
plt.grid(linestyle='--', alpha=0.35)
plt.tight_layout()
plt.show()

#home ownership by funded Amount 
home_funding = df.groupby('home_ownership')['loan_amount'].sum().reset_index()
home_funding['loan_amount_millions']= home_funding['loan_amount']/1_000_000
fig = px.treemap(home_funding, path=['home_ownership'], values='loan_amount_millions', color='loan_amount_millions', color_continuous_scale='Blues',
                 title="total funded amount by home ownership (in millions)")
fig.show()


#home ownership by recevied Amount 
home_recevied = df.groupby('home_ownership')['total_payment'].sum().reset_index()
home_recevied['recevied_amount_millions']= home_recevied['total_payment']/1_000_000
fig = px.treemap(home_recevied, path=['home_ownership'], values='recevied_amount_millions', color='recevied_amount_millions', color_continuous_scale='Blues',
                 title="total recevied amount by home ownership (in millions)")
fig.show()


#home ownership by application
home_application = df.groupby('home_ownership')['id'].count().reset_index()
home_application['application_amount']= home_application['id']
fig = px.treemap(home_application, path=['home_ownership'], values='application_amount', color='application_amount', color_continuous_scale='Blues',
                 title="total application amount by home ownership (in millions)")
fig.show()
