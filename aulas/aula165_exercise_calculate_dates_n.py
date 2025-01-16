# Mary takes a 1kk loan and she intends pay in 5y;
# She takes the loan on December/01/2020.

# - Create the loan date;
# - Create the final loan date; and
# - List all loan deadlines and list the value of each installment.

from datetime import datetime
from dateutil.relativedelta import relativedelta

installment_n = 1
installment_n_total = 12 * 5
delta_years = relativedelta(years=5)
debt = 1000000
installment_amount = debt / installment_n_total
loan_date = datetime(2020, 12, 20)
final_date = loan_date + delta_years


while installment_n <= installment_n_total:
    print(f" {loan_date.strftime('%Y/%m/%d')} \033[34mPayment amount: R$ {installment_amount:,.2f}\033[0m \033[31mDebt: R$  {debt - installment_amount:,.2f}\033[0m Parcela: {installment_n}/{installment_n_total}")
    debt -= installment_amount
    installment_n += 1
    loan_date += relativedelta(months=+1)

# print(loan_date + relativedelta(days=1))
