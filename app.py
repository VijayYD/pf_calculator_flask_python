from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_pf(basic_salary, months, interest):
    employee_contribution = 0.12 * basic_salary
    employer_contribution_pf = 0.0367 * basic_salary
    employer_contribution_eps = 0.0833 * basic_salary

    total_employee = employee_contribution * months
    total_employer_pf = employer_contribution_pf * months
    total_employer_eps = employer_contribution_eps * months

    total_principal = total_employee + total_employer_pf

    # Convert annual interest rate to monthly
    r = interest / 100 / 12
    n = months

    # Compound interest formula: A = P*(1 + r)^n
    pf_with_interest = total_principal * ((1 + r) ** n)

    return {
        "employee_monthly": round(employee_contribution, 2),
        "employer_monthly": round(employer_contribution_pf, 2),
        "eps_monthly": round(employer_contribution_eps, 2),
        "pf_total": round(total_principal, 2),
        "eps_total": round(total_employer_eps, 2),
        "pf_with_interest": round(pf_with_interest, 2)
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        basic_salary = float(request.form['basic_salary'])
        months = int(request.form['months'])
        interest = float(request.form['interest'])
        result = calculate_pf(basic_salary, months, interest)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
