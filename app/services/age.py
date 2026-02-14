from datetime import date, datetime, timedelta

def calculate_age_detailed(birth_date: str) -> dict:
    """
    Retorna idade detalhada:
    - anos
    - meses
    - dias
    """

    try:
        birth = datetime.strptime(birth_date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Birth date must be in format YYYY-MM-DD")

    today = date.today()

    if birth > today:
        raise ValueError("Birth date cannot be in the future")

    # Cálculo base
    years = today.year - birth.year
    months = today.month - birth.month
    days = today.day - birth.day

    if days < 0:
        months -= 1
        last_month = today.replace(day=1) - timedelta(days=1)
        days += last_month.day

    if months < 0:
        years -= 1
        months += 12

    return {
        "years": years,
        "months": months,
        "days": days
    }
